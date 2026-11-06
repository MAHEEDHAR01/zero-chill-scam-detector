"""
ZERO CHILL 3.0 – Ultimate AI Cybersecurity, Cybercrime Prevention & Legal Action Platform
Main Flask Application Server
"""

import os
import sys
import json
from datetime import datetime
from flask import Flask, request, jsonify, render_template, send_from_directory, Response
from flask_cors import CORS

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

import database
from scam_engine import analyze_scam_advanced
from cyber_laws import CYBER_LAWS_DIRECTORY, get_relevant_laws_for_category, LEGAL_DISCLAIMER
from gov_services import GOV_SERVICES_DIRECTORY, get_services_for_category
from news_advisories import get_all_advisories
from url_intelligence import audit_url_deep
from ai_assistant import chat_with_assistant
from evidence_manager import (
    save_uploaded_file, extract_text_from_file, redact_sensitive_pii,
    generate_incident_docket_html, MAX_CONTENT_LENGTH
)

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH
CORS(app)

# Initialize database schema on startup
database.init_db()

# Preloaded Hackathon Demo Benchmarks
BENCHMARK_SAMPLES = [
    {
        "id": "sample-safe",
        "category": "SAFE",
        "label": "SAFE: Electricity Bill Payment Confirmation",
        "language": "en",
        "text": "Your electricity bill payment of Rs. 850 was successfully received. Thank you.",
        "description": "Standard transactional receipt without malicious hyperlinks, urgency, or credential demands."
    },
    {
        "id": "sample-suspicious",
        "category": "SUSPICIOUS",
        "label": "SUSPICIOUS: Work-From-Home Job Offer",
        "language": "en",
        "text": "Congratulations! You have been selected for a work-from-home job. Contact us immediately for more details.",
        "description": "Unsolicited employment notification with artificial urgency and lack of verified employer details."
    },
    {
        "id": "sample-high-risk",
        "category": "HIGH-RISK SCAM",
        "label": "HIGH-RISK: Bank Phishing & OTP Trap",
        "language": "en",
        "text": "Your bank account will be blocked today! Verify your account immediately by clicking http://fake-bank-example.com and entering your OTP.",
        "description": "Severe phishing: Account block panic threat, spoofed multi-hyphen HTTP link, and explicit OTP credential harvesting."
    },
    {
        "id": "sample-hindi-threat",
        "category": "HIGH-RISK SCAM",
        "label": "HIGH-RISK: Hindi Bank KYC Expiry Phishing",
        "language": "hi",
        "text": "प्रिय ग्राहक, आपका एसबीआई बैंक खाता आज रात बंद हो जाएगा! तुरंत http://sbi-kyc-update.xyz पर जाकर पैन कार्ड और ओटीपी दर्ज करें।",
        "description": "Hindi Devanagari smishing targeting SBI account holders with fake KYC urgency and .xyz phishing link."
    },
    {
        "id": "sample-telugu-lottery",
        "category": "HIGH-RISK SCAM",
        "label": "HIGH-RISK: Telugu KBC Prize Scam",
        "language": "te",
        "text": "మీ మొబైల్ నంబర్ KBC లక్కీ డ్రాలో 25 లక్షల రూపాయలు గెలుచుకుంది! నగదును క్లెయిమ్ చేయడానికి వెంటనే 499 రూపాయల రిజిస్ట్రేషన్ ఫీజు చెల్లించండి.",
        "description": "Telugu language advance-fee lottery scam demanding ₹499 upfront registration fee to claim fake ₹25 Lakhs."
    },
    {
        "id": "sample-digital-arrest",
        "category": "HIGH-RISK SCAM",
        "label": "HIGH-RISK: FedEx / CBI Digital Arrest Extortion",
        "language": "en",
        "text": "FedEx Security Alert: Your parcel containing fake passports has been detained at Mumbai Customs. CBI FIR registered. To avoid police arrest, join immediate Skype call with Cyber Crime Cell.",
        "description": "Digital arrest extortion scam exploiting fear of law enforcement to coerce victims into video calls."
    },
    {
        "id": "sample-qr-upi",
        "category": "HIGH-RISK SCAM",
        "label": "HIGH-RISK: UPI QR Code 'Receive Money' Scam",
        "language": "en",
        "text": "upi://pay?pa=scammer99@okhdfcbank&pn=State%20Bank%20of%20India&am=5000&cu=INR",
        "description": "Fake merchant QR payload: Claims to credit money, but scanning and entering MPIN debits ₹5,000 from the victim."
    }
]

# ----------------- ROUTE HANDLERS -----------------

@app.route('/')
def index():
    """Serve the main ZERO CHILL 3.0 single-page application."""
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    """Multi-method threat analysis endpoint (Text, Screenshot text, Email, QR)."""
    data = request.get_json(silent=True) or {}
    text = data.get('text', '').strip()
    scan_type = data.get('scanType', 'text')
    api_key = data.get('apiKey', '').strip() or None

    if not text:
        return jsonify({
            'error': 'Message text is required for analysis.',
            'riskLevel': 'SAFE',
            'riskScore': 0
        }), 400

    custom_keys = {}
    if api_key:
        custom_keys['safe_browsing'] = api_key

    # Run multi-vector evaluation
    result = analyze_scam_advanced(text, custom_api_keys=custom_keys)

    # Persist scan to SQLite database
    scan_record = {
        'input_text': text,
        'scan_type': scan_type,
        'snippet': text[:110] + '...' if len(text) > 110 else text,
        'riskLevel': result['riskLevel'],
        'riskScore': result['riskScore'],
        'scamType': result['scamType'],
        'indicators': result['indicators'],
        'highlightedPhrases': result['highlightedPhrases'],
        'explanation': result['explanation'],
        'recommendedSteps': result['recommendedSteps'],
        'legalSections': result.get('legalSections', []),
        'govServices': result.get('govServices', []),
        'confidenceScore': result.get('confidenceScore', 0.92),
        'uncertaintyRating': result.get('uncertaintyRating', 'Low'),
        'language': result.get('language', 'en'),
        'engine': result.get('engine', 'ZERO CHILL 3.0 Threat Engine')
    }
    saved_id = database.save_scan(scan_record)
    result['id'] = saved_id

    return jsonify(result)

@app.route('/api/audit-url', methods=['POST'])
def audit_url():
    """Dedicated URL & Threat Intelligence audit endpoint."""
    data = request.get_json(silent=True) or {}
    url = data.get('url', '').strip()
    api_key = data.get('apiKey', '').strip() or None

    if not url:
        return jsonify({'error': 'URL address is required for inspection.'}), 400

    custom_keys = {}
    if api_key:
        custom_keys['safe_browsing'] = api_key
        custom_keys['virustotal'] = api_key

    url_result = audit_url_deep(url, custom_keys)

    # Also evaluate full scam engine heuristics on the URL
    engine_eval = analyze_scam_advanced(url, custom_api_keys=custom_keys)

    # Persist as 'url' scan
    scan_record = {
        'input_text': url,
        'scan_type': 'url',
        'snippet': url[:110],
        'riskLevel': url_result['riskLevel'],
        'riskScore': url_result['riskScore'],
        'scamType': 'Web Link & Domain Inspection',
        'indicators': url_result['warnings'],
        'highlightedPhrases': [url],
        'explanation': url_result['summary'],
        'recommendedSteps': [
            "Never submit banking credentials, passwords, or OTPs on unverified domains.",
            "Verify official Indian portals at cybercrime.gov.in, indiacode.nic.in, or sancharsaathi.gov.in.",
            "If this domain mimicked your bank, contact your branch immediately."
        ],
        'legalSections': engine_eval.get('legalSections', []),
        'govServices': engine_eval.get('govServices', []),
        'confidenceScore': 0.94,
        'uncertaintyRating': 'Low',
        'language': 'en',
        'engine': url_result['engineType']
    }
    saved_id = database.save_scan(scan_record)

    response_data = {
        **url_result,
        'id': saved_id,
        'legalSections': engine_eval.get('legalSections', []),
        'govServices': engine_eval.get('govServices', [])
    }
    return jsonify(response_data)

@app.route('/api/chat', methods=['POST'])
def chat():
    """Conversational AI Cyber Safety Assistant endpoint."""
    data = request.get_json(silent=True) or {}
    message = data.get('message', '').strip()
    history = data.get('history', [])
    api_key = data.get('apiKey', '').strip() or None

    if not message:
        return jsonify({'error': 'Message content cannot be empty.'}), 400

    response = chat_with_assistant(message, api_key=api_key, history=history)
    return jsonify(response)

@app.route('/api/laws', methods=['GET'])
def get_laws():
    """Return verified Indian Cyber Law and Legal Rights directory."""
    category = request.args.get('category', '').strip()
    if category and category != 'ALL':
        laws = get_relevant_laws_for_category(category)
    else:
        laws = CYBER_LAWS_DIRECTORY

    return jsonify({
        'disclaimer': LEGAL_DISCLAIMER,
        'laws': laws,
        'count': len(laws)
    })

@app.route('/api/gov-services', methods=['GET'])
def get_gov_services():
    """Return verified Indian Government Services & Reporting Directory."""
    category = request.args.get('category', '').strip()
    if category and category != 'ALL':
        services = get_services_for_category(category)
    else:
        services = GOV_SERVICES_DIRECTORY

    return jsonify({
        'disclaimer': "ZERO CHILL 3.0 is an independent civic defense tool. It is not affiliated with the Government of India and does not auto-submit complaints without user consent.",
        'services': services,
        'count': len(services)
    })

@app.route('/api/advisories', methods=['GET'])
def get_advisories():
    """Return verified advisories from CERT-In, RBI, TRAI, MHA, PIB."""
    cat = request.args.get('category', 'ALL')
    search = request.args.get('search', '')
    advisories = get_all_advisories(category=cat, search=search)
    return jsonify({
        'advisories': advisories,
        'count': len(advisories)
    })

@app.route('/api/evidence/upload', methods=['POST'])
def upload_evidence():
    """Upload digital evidence (JPG, PNG, PDF, TXT), extract text, redact PII, and record metadata."""
    if 'file' not in request.files:
        # Check if text-only evidence submission
        incident_title = request.form.get('incident_title', 'Cyber Incident Evidence')
        incident_type = request.form.get('incident_type', 'General Cyber Fraud')
        raw_text = request.form.get('extracted_text', '')
        checklist = json.loads(request.form.get('checklist', '[]'))

        redacted = redact_sensitive_pii(raw_text)
        evidence_id = database.save_evidence({
            'incident_title': incident_title,
            'incident_type': incident_type,
            'incident_date': request.form.get('incident_date', datetime.now().strftime('%Y-%m-%d')),
            'incident_time': request.form.get('incident_time', datetime.now().strftime('%H:%M')),
            'description': request.form.get('description', ''),
            'suspect_details': request.form.get('suspect_details', ''),
            'financial_loss': float(request.form.get('financial_loss', 0.0) or 0.0),
            'transaction_utr': request.form.get('transaction_utr', ''),
            'file_name': 'Text Log / Chat Export',
            'file_type': 'text/plain',
            'file_size': len(raw_text.encode('utf-8')),
            'extracted_text': raw_text,
            'redacted_text': redacted,
            'evidence_checklist': checklist
        })
        return jsonify({'success': True, 'id': evidence_id, 'message': 'Evidence text preserved and redacted.'})

    file = request.files['file']
    file_path, original_name, ext, file_size = save_uploaded_file(file)

    if not file_path:
        return jsonify({'error': 'Invalid file format. Supported: JPG, PNG, PDF, TXT (up to 10MB)'}), 400

    # Extract text from PDF or TXT
    extracted_text = extract_text_from_file(file_path, ext)
    client_ocr = request.form.get('extracted_text', '').strip()
    if client_ocr:
        extracted_text = client_ocr + ("\n\n" + extracted_text if extracted_text else "")

    # Redact sensitive PII (card numbers, Aadhaar, OTPs)
    redacted_text = redact_sensitive_pii(extracted_text)

    checklist = []
    try:
        checklist = json.loads(request.form.get('checklist', '[]'))
    except Exception:
        pass

    evidence_id = database.save_evidence({
        'incident_title': request.form.get('incident_title', original_name),
        'incident_type': request.form.get('incident_type', 'Financial Cyber Fraud'),
        'incident_date': request.form.get('incident_date', datetime.now().strftime('%Y-%m-%d')),
        'incident_time': request.form.get('incident_time', datetime.now().strftime('%H:%M')),
        'description': request.form.get('description', ''),
        'suspect_details': request.form.get('suspect_details', ''),
        'financial_loss': float(request.form.get('financial_loss', 0.0) or 0.0),
        'transaction_utr': request.form.get('transaction_utr', ''),
        'file_path': file_path,
        'file_name': original_name,
        'file_type': ext,
        'file_size': file_size,
        'extracted_text': extracted_text,
        'redacted_text': redacted_text,
        'evidence_checklist': checklist
    })

    return jsonify({
        'success': True,
        'id': evidence_id,
        'fileName': original_name,
        'extractedText': extracted_text,
        'redactedText': redacted_text,
        'message': 'Digital evidence safely preserved in Local Evidence Vault.'
    })

@app.route('/api/evidence', methods=['GET'])
def get_evidence():
    """Retrieve all preserved evidence items."""
    evidence_list = database.get_evidence_list()
    return jsonify({
        'evidence': evidence_list,
        'count': len(evidence_list)
    })

@app.route('/api/evidence/<evidence_id>', methods=['DELETE'])
def delete_evidence_item(evidence_id):
    """Delete an evidence record and its file."""
    deleted = database.delete_evidence(evidence_id)
    return jsonify({'success': deleted})

@app.route('/api/evidence/<evidence_id>/docket', methods=['GET'])
def get_evidence_docket(evidence_id):
    """Generate and return formal printable HTML Incident Docket."""
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM evidence WHERE id = ?', (evidence_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return "Evidence record not found", 404

    incident_data = dict(row)
    incident_data['evidence_checklist'] = json.loads(incident_data.get('evidence_checklist') or '[]')

    html = generate_incident_docket_html(incident_data)
    return Response(html, mimetype='text/html')

@app.route('/api/history', methods=['GET'])
def get_history():
    """Retrieve scan history from SQLite database with optional filter."""
    risk_filter = request.args.get('filter', 'ALL')
    scans = database.get_scans(limit=50, filter_risk=risk_filter)
    return jsonify({
        'scans': scans,
        'count': len(scans)
    })

@app.route('/api/history/<scan_id>', methods=['DELETE'])
def delete_history_item(scan_id):
    """Delete single scan from history."""
    deleted = database.delete_scan(scan_id)
    return jsonify({'success': deleted})

@app.route('/api/history', methods=['DELETE'])
def clear_history():
    """Clear all scans from history."""
    count = database.clear_all_scans()
    return jsonify({'success': True, 'clearedCount': count})

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Return database telemetry stats for the dashboard."""
    stats = database.get_telemetry_stats()
    return jsonify(stats)

@app.route('/api/samples', methods=['GET'])
def get_samples():
    """Return preloaded demo scenarios for hackathon demonstration."""
    return jsonify({
        'samples': BENCHMARK_SAMPLES
    })

@app.route('/api/health', methods=['GET'])
def health():
    """System health check and configuration telemetry."""
    has_gemini_key = bool(os.environ.get("GEMINI_API_KEY", "").strip())
    has_safebrowsing_key = bool(os.environ.get("GOOGLE_SAFE_BROWSING_KEY", "").strip())
    has_vt_key = bool(os.environ.get("VIRUSTOTAL_KEY", "").strip())

    stats = database.get_telemetry_stats()

    return jsonify({
        'status': 'healthy',
        'application': 'ZERO CHILL 3.0 – Ultimate AI Cyber Safety Platform',
        'version': '3.0.0',
        'database': 'SQLite Connected (zero_chill.db)',
        'totalScansInDb': stats['totalScans'],
        'engines': {
            'rule_based_ai': 'Active (Ready)',
            'gemini_llm': 'Active (Key in environment)' if has_gemini_key else 'Standby (User key / Offline Fallback Engine)',
            'safe_browsing': 'Active' if has_safebrowsing_key else 'Offline Deep Domain Heuristics',
            'virustotal': 'Active' if has_vt_key else 'Offline Vendor Signatures'
        }
    })

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("==================================================")
    print(f"[ZERO CHILL 3.0] Server online on http://localhost:{port}")
    print("[ZERO CHILL 3.0] Threat Heuristics & Multilingual Engine: READY")
    print("[ZERO CHILL 3.0] Indian Cyber Law & Gov Services Engine: READY")
    print("[ZERO CHILL 3.0] Evidence Vault & SQLite Database: ONLINE")
    print("==================================================")
    app.run(host='0.0.0.0', port=port, debug=False)
