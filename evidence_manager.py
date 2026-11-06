"""
ZERO CHILL 3.0 – Secure Digital Evidence Management Engine
Upload handling, sensitive PII redaction, PDF/TXT text extraction,
evidence metadata capture, and printable cybercrime incident docket generation.
"""

import os
import re
import uuid
from datetime import datetime
from werkzeug.utils import secure_filename
from typing import Dict, Any, Tuple, Optional
import pypdf

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf', 'txt'}
MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB limit


def is_allowed_file(filename: str) -> bool:
    """Check if uploaded file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def redact_sensitive_pii(text: str) -> str:
    """
    Redact sensitive credentials, full card numbers, Aadhaar, and OTPs 
    to preserve privacy in compliance with cybersecurity evidence standards.
    """
    if not text:
        return ""

    redacted = text

    # 1. Redact 16-digit credit/debit card numbers (preserve last 4 digits)
    def card_replacer(match):
        raw = match.group(0).replace('-', '').replace(' ', '')
        return f"[CARD REDACTED: ****-****-****-{raw[-4:]}]"
    redacted = re.sub(r'\b(?:\d{4}[-\s]?){3}\d{4}\b', card_replacer, redacted)

    # 2. Redact 12-digit Aadhaar Numbers (preserve last 4 digits)
    def aadhaar_replacer(match):
        raw = match.group(0).replace(' ', '')
        return f"[AADHAAR REDACTED: ********{raw[-4:]}]"
    redacted = re.sub(r'\b\d{4}\s\d{4}\s\d{4}\b', aadhaar_replacer, redacted)

    # 3. Redact explicit OTP codes (6 digits following OTP/code keyword)
    redacted = re.sub(
        r'(?i)\b(otp|code|pin|password|mpin)\s*(?:is|:|=)?\s*(\d{4,8})\b',
        r'\1: [REDACTED: ******]',
        redacted
    )

    # 4. Partially mask 10-digit Indian Mobile Numbers (preserve first 2 and last 3)
    def phone_replacer(match):
        p = match.group(0)
        return f"{p[:2]}*****{p[-3:]}"
    redacted = re.sub(r'\b[6-9]\d{9}\b', phone_replacer, redacted)

    return redacted


def extract_text_from_file(file_path: str, ext: str) -> str:
    """Extract readable text from PDF or TXT files."""
    if ext == 'txt':
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read().strip()
        except Exception as e:
            return f"[Error reading TXT file: {e}]"

    elif ext == 'pdf':
        try:
            reader = pypdf.PdfReader(file_path)
            extracted = []
            for i, page in enumerate(reader.pages):
                text = page.extract_text() or ''
                if text.strip():
                    extracted.append(f"--- Page {i+1} ---\n{text.strip()}")
            return "\n\n".join(extracted) if extracted else "[PDF contains scanned imagery. Use OCR tool.]"
        except Exception as e:
            return f"[Error parsing PDF: {e}]"

    return ""


def save_uploaded_file(file_storage) -> Tuple[Optional[str], Optional[str], Optional[str], int]:
    """
    Securely save uploaded evidence file with unique UUID prefix.
    Returns: (file_path, original_filename, file_ext, file_size)
    """
    if not file_storage or not file_storage.filename:
        return None, None, None, 0

    original_filename = secure_filename(file_storage.filename)
    if not is_allowed_file(original_filename):
        return None, None, None, 0

    ext = original_filename.rsplit('.', 1)[1].lower()
    unique_name = f"{uuid.uuid4().hex}_{original_filename}"
    file_path = os.path.join(UPLOAD_FOLDER, unique_name)

    file_storage.save(file_path)
    file_size = os.path.getsize(file_path)

    return file_path, original_filename, ext, file_size


def generate_incident_docket_html(incident_data: Dict[str, Any]) -> str:
    """
    Generate a formal, printable HTML Cybercrime Incident Docket
    ready for submission to cybercrime.gov.in and local cyber police stations.
    """
    ref_id = incident_data.get('id', f"ZC-{uuid.uuid4().hex[:8].upper()}")
    title = incident_data.get('incident_title', 'Cyber Incident Evidence Docket')
    incident_type = incident_data.get('incident_type', 'Financial Cyber Fraud')
    incident_date = incident_data.get('incident_date', datetime.now().strftime('%Y-%m-%d'))
    incident_time = incident_data.get('incident_time', datetime.now().strftime('%H:%M'))
    loss_amount = incident_data.get('financial_loss', 0.0)
    utr_no = incident_data.get('transaction_utr', 'N/A')
    suspect_info = incident_data.get('suspect_details', 'Not Provided')
    description = incident_data.get('description', 'No additional description provided.')
    redacted_evidence = incident_data.get('redacted_text', 'No extracted text.')
    checklist = incident_data.get('evidence_checklist', [])

    checklist_items = "".join([f"<li>✔ {item}</li>" for item in checklist]) if checklist else "<li>Evidence preserved on device.</li>"

    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Incident Docket - {ref_id}</title>
    <style>
        body {{ font-family: 'Segoe UI', Arial, sans-serif; margin: 40px; color: #1e293b; background: #fff; line-height: 1.6; }}
        .header {{ border-bottom: 3px solid #0284c7; padding-bottom: 15px; margin-bottom: 25px; display: flex; justify-content: space-between; align-items: center; }}
        .badge {{ background: #ef4444; color: #fff; padding: 4px 12px; border-radius: 6px; font-weight: bold; font-size: 12px; text-transform: uppercase; }}
        .meta-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 15px; background: #f8fafc; padding: 18px; border-radius: 8px; border: 1px solid #e2e8f0; margin-bottom: 25px; }}
        .meta-item {{ font-size: 13px; }}
        .meta-label {{ font-weight: bold; color: #64748b; font-size: 11px; text-transform: uppercase; }}
        h2 {{ color: #0f172a; font-size: 18px; margin-top: 25px; border-bottom: 1px solid #cbd5e1; padding-bottom: 6px; }}
        .evidence-box {{ background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 6px; padding: 15px; font-family: monospace; font-size: 12px; white-space: pre-wrap; }}
        .disclaimer {{ margin-top: 40px; border-top: 1px dashed #94a3b8; padding-top: 15px; font-size: 11px; color: #64748b; }}
        .print-btn {{ background: #0284c7; color: #fff; border: none; padding: 10px 20px; border-radius: 6px; font-weight: bold; cursor: pointer; }}
        @media print {{ .no-print {{ display: none; }} }}
    </style>
</head>
<body>
    <div class="no-print" style="margin-bottom: 20px; text-align: right;">
        <button class="print-btn" onclick="window.print()">🖨️ Print / Save as PDF</button>
    </div>

    <div class="header">
        <div>
            <h1 style="margin: 0; font-size: 24px; color: #0369a1;">ZERO CHILL 3.0</h1>
            <p style="margin: 2px 0 0 0; font-size: 13px; color: #64748b;">Digital Cybercrime Incident Evidence Docket</p>
        </div>
        <div style="text-align: right;">
            <span class="badge">Preserved Evidence</span>
            <div style="font-family: monospace; font-weight: bold; margin-top: 6px;">Ref: {ref_id}</div>
        </div>
    </div>

    <div class="meta-grid">
        <div class="meta-item"><div class="meta-label">Incident Classification</div><strong>{incident_type}</strong></div>
        <div class="meta-item"><div class="meta-label">Report Generated Date</div>{datetime.now().strftime('%d %B %Y, %I:%M %p')}</div>
        <div class="meta-item"><div class="meta-label">Date & Time of Occurrence</div>{incident_date} at {incident_time}</div>
        <div class="meta-item"><div class="meta-label">Financial Loss Reported</div><strong style="color: #dc2626;">₹{loss_amount:,.2f}</strong></div>
        <div class="meta-item"><div class="meta-label">Transaction UTR / Ref Number</div><code>{utr_no}</code></div>
        <div class="meta-item"><div class="meta-label">Suspect Phone / UPI / ID</div><code>{suspect_info}</code></div>
    </div>

    <h2>1. Incident Description & Narrative</h2>
    <p style="font-size: 14px;">{description}</p>

    <h2>2. Preserved Digital Evidence Checklist</h2>
    <ul style="font-size: 13px;">
        {checklist_items}
    </ul>

    <h2>3. Extracted & Redacted Evidence Content</h2>
    <p style="font-size: 12px; color: #64748b;">(Sensitive 16-digit card numbers, OTPs, and Aadhaar identifiers automatically redacted for privacy):</p>
    <div class="evidence-box">{redacted_evidence}</div>

    <h2>4. Statutory Framework (Applicable Indian Laws)</h2>
    <ul style="font-size: 13px; color: #334155;">
        <li><strong>IT Act, 2000 - Section 66D:</strong> Cheating by personation by using computer resource (up to 3 years imprisonment + fine).</li>
        <li><strong>IT Act, 2000 - Section 66C:</strong> Identity theft, unauthorized use of passwords, OTPs, or electronic signatures.</li>
        <li><strong>Bharatiya Nyaya Sanhita, 2023 - Section 318(4):</strong> Cheating and dishonestly inducing delivery of property (up to 7 years imprisonment + fine).</li>
    </ul>

    <h2>5. Recommended Next Steps for Citizen</h2>
    <ol style="font-size: 13px; color: #334155;">
        <li><strong>Financial Fraud (Within 2 Hours):</strong> Immediately call the National Cyber Crime Helpline <strong>1930</strong>.</li>
        <li><strong>Formal Police Complaint:</strong> Submit this docket at <strong>https://cybercrime.gov.in</strong> under Financial Fraud or Other Cybercrime.</li>
        <li><strong>Bank Dispute:</strong> Contact your home branch within 3 days with this complaint copy to initiate zero-liability dispute under RBI rules.</li>
    </ol>

    <div class="disclaimer">
        <strong>Notice:</strong> This document was prepared using ZERO CHILL 3.0 Civic Cybersecurity Platform. It does not replace an official FIR or police investigation. The complainant certifies that all statements and uploaded documents are genuine records preserved for formal submission to law enforcement authorities.
    </div>
</body>
</html>"""
    return html
