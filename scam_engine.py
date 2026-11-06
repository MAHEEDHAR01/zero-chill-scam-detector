"""
ZERO CHILL 3.0 – Advanced AI Scam Detection & Threat Heuristics Engine
Multi-vector natural language threat analysis across 15+ cybercrime attack vectors.
Supports English, Hindi (Devanagari & Hinglish), Telugu (Telugu Script & Romanized Telugu),
QR Code UPI payment payloads, and email header analysis.
"""

import re
from urllib.parse import urlparse, parse_qs
from typing import Dict, Any, List, Tuple, Optional
from cyber_laws import get_relevant_laws_for_category
from gov_services import get_services_for_category
from url_intelligence import audit_url_deep

# ----------------- MULTILINGUAL THREAT PATTERNS -----------------

# 1. Credential Harvesting (OTP, PIN, Password, Aadhaar, CVV)
CREDENTIAL_PATTERNS = [
    # English
    (r'\b(otp|one time password|verification code)\b', 'OTP / Verification Code Request', 45, 'CRITICAL'),
    (r'\b(atm pin|upi pin|mpin|security pin|card pin)\b', 'Banking PIN / MPIN Request', 50, 'CRITICAL'),
    (r'\b(cvv|cvv2|security code on card)\b', 'Card CVV Security Number', 45, 'CRITICAL'),
    (r'\b(netbanking password|login password|bank password)\b', 'Banking Password Theft', 50, 'CRITICAL'),
    (r'\b(aadhaar card details|pan card details|credit card number)\b', 'Identity Number Harvesting', 35, 'HIGH'),
    # Hindi (Devanagari & Hinglish)
    (r'(ओटीपी|पासवर्ड|पिन नंबर|सीवीवी)', 'Hindi: OTP / PIN Theft Request', 45, 'CRITICAL'),
    (r'\b(otp share|otp bataye|pin dale|password bhejo|apna otp)\b', 'Hinglish: Request to Share OTP / PIN', 45, 'CRITICAL'),
    # Telugu (Script & Romanized)
    (r'(ఓటీపీ|పిన్|పాస్‌వర్డ్)', 'Telugu: OTP / PIN Request', 45, 'CRITICAL'),
    (r'\b(otp cheppandi|pin enter cheyandi|otp ivvandi|password pampandi)\b', 'Telugu (Romanized): OTP / PIN Sharing Request', 45, 'CRITICAL')
]

# 2. Urgency, Panic & Coercion (Account Block, Disconnection, Police Arrest)
URGENCY_PATTERNS = [
    # English
    (r'\b(account.*(block|suspend|deactivat|freez|clos))\b', 'Threat of Account Block / Suspension', 35, 'HIGH'),
    (r'\b(blocked today|within 24 hours|within 2 hours|within 10 minutes|immediately|urgent action)\b', 'Extreme Time Urgency / Artificial Panic', 30, 'HIGH'),
    (r'\b(power.*disconnect|electricity.*disconnected tonight|bill unpaid.*disconnect)\b', 'Electricity Disconnection Threat', 40, 'HIGH'),
    (r'\b(arrest warrant|cbi inquiry|police custody|digital arrest|fir registered|customs detention)\b', 'Law Enforcement / Digital Arrest Threat', 50, 'CRITICAL'),
    (r'\b(verify.*kyc|update.*pan|pan link.*sbi|kyc pending|kyc suspended)\b', 'Urgent KYC / PAN Update Coercion', 35, 'HIGH'),
    # Hindi (Devanagari & Hinglish)
    (r'(खाता ब्लॉक|खाता बंद|बिजली कट|गिरफ्तारी वारंट|तुरंत कवाईसी)', 'Hindi: Account Block / Arrest Threat', 40, 'HIGH'),
    (r'\b(account band ho jayega|turant kyc|aaj hi block|bijli cut jayegi|police case darj)\b', 'Hinglish: Coercive Panic Threat', 40, 'HIGH'),
    # Telugu (Script & Romanized)
    (r'(ఖాతా బ్లాక్|కరెంట్ కట్|అరెస్ట్ వారెంట్|వెంటనే కేవైసీ)', 'Telugu: Account Block / Arrest Coercion', 40, 'HIGH'),
    (r'\b(account block avthundi|current cut avthundi|ventane kyc|police case register)\b', 'Telugu (Romanized): Panic Threat', 40, 'HIGH')
]

# 3. Work-from-Home, Task Scams & Job Fraud
JOB_SCAM_PATTERNS = [
    # English
    (r'\b(work from home|part[- ]time job|online job)\b.*\b(earn|salary|daily|per day)\b', 'Unsolicited Work-From-Home Hook', 30, 'MEDIUM'),
    (r'\b(earn\s*(rs\.?|inr|₹)\s*[1-9]\d{2,4}\s*(daily|per day|hourly))\b', 'Unrealistic Daily Wage Claim', 35, 'HIGH'),
    (r'\b(like youtube videos|subscribe channels|review hotels|telegram task)\b', 'Task-Based YouTube/Telegram Review Scam', 45, 'CRITICAL'),
    (r'\b(contact.*hr.*whatsapp|message on telegram|contact.*@\w+)\b', 'Directing to Unregulated Messaging Apps', 25, 'MEDIUM'),
    (r'\b(no investment|no experience required|flexible hours.*earn.*daily)\b', 'Too-Good-To-Be-True Employment Pitch', 25, 'MEDIUM'),
    # Hindi & Telugu
    (r'(घर बैठे कमाए|रोजाना कमाए|यूट्यूब लाइक|पार्ट टाइम जॉब)', 'Hindi: Work-from-Home Scam Hook', 35, 'HIGH'),
    (r'\b(ghar baithe kamayein|rojana kamaye|youtube like karke|part time kaam)\b', 'Hinglish: Fake Daily Wage Task', 35, 'HIGH'),
    (r'(ఇంటి నుండి పని|రోజువారీ సంపాదన|యూట్యూబ్ లైక్)', 'Telugu: Fake Work-from-Home Task', 35, 'HIGH'),
    (r'\b(intlo kurchuni|rojuna sampadinchandi|part time udyogam)\b', 'Telugu (Romanized): Work-from-Home Bait', 35, 'HIGH')
]

# 4. Lottery, Prizes, Rewards & Financial Windfalls
REWARD_PATTERNS = [
    # English
    (r'\b(won|winner|winning)\b.*\b(rs\.?|inr|lakh|crore|prize|lottery|\$)\b', 'Unsolicited Lottery / Cash Prize Claim', 35, 'HIGH'),
    (r'\b(congratulations|lucky winner|selected in lucky draw)\b', 'Fake Congratulatory Hook', 25, 'MEDIUM'),
    (r'\b(kbc lucky draw|kaun banega crorepati lottery|tata safari winner|iphone 1[4-6] winner)\b', 'High-Profile Lottery Impersonation (KBC)', 45, 'CRITICAL'),
    (r'\b(double your money|100% guaranteed profit|daily return.*%|risk-free investment)\b', 'Unrealistic Investment / Crypto Doubling', 40, 'HIGH'),
    # Hindi & Telugu
    (r'(बधाई हो|इनाम जीता|लॉटरी निकली|केबीसी लकी ड्रॉ)', 'Hindi: Lottery / Prize Claim', 35, 'HIGH'),
    (r'\b(badhai ho|inaam jeeta|kbc lottery nikli|lakh rupaye jeete)\b', 'Hinglish: Unverified Prize Hook', 35, 'HIGH'),
    (r'(అభినందనలు|బహుమతి గెలుచుకున్నారు|లాటరీ)', 'Telugu: Unverified Prize Claim', 35, 'HIGH'),
    (r'\b(abhinandanalu|bahumathi gelicharu|lottery vachindi)\b', 'Telugu (Romanized): Fake Prize Bait', 35, 'HIGH')
]

# 5. Predatory Loans & Unverified Financing
LOAN_PATTERNS = [
    (r'\b(instant loan.*approved|pre-approved loan of.*(lakh|inr)|loan without cibil|zero interest loan)\b', 'Predatory Instant Loan Offer', 35, 'HIGH'),
    (r'\b(disbursed in 5 mins|no income proof loan|instant cash loan.*apply)\b', 'Unverified Instant Cash Loan Pitch', 30, 'HIGH'),
    (r'(बिना सिबिल लोन|तुरंत लोन स्वीकृत|जीरो ब्याज लोन)', 'Hindi: Predatory Instant Loan', 35, 'HIGH'),
    (r'(సిబిల్ లేకుండా లోన్|తక్షణ రుణం ఆమోదించబడింది)', 'Telugu: Predatory Loan Pitch', 35, 'HIGH')
]

# 6. Upfront Advance Fees & Processing Charges
ADVANCE_FEE_PATTERNS = [
    (r'\b(pay\s*(rs\.?|inr|₹)\s*\d+.*(registration|processing|clearance|tax|refundable|vip))\b', 'Upfront Fee / Registration Charge Request', 45, 'CRITICAL'),
    (r'\b(customs duty|clearance fee|delivery fee.*parcel|release charge)\b', 'Fake Customs / Courier Fee Demand', 40, 'HIGH'),
    (r'\b(deposit.*before release|claim fee|security deposit to withdraw)\b', 'Advance-Fee Fraud Pre-condition', 40, 'HIGH'),
    (r'(रजिस्ट्रेशन फीस|प्रोसेसिंग शुल्क|कस्टम ड्यूटी भरो)', 'Hindi: Upfront Fee Demand', 40, 'HIGH'),
    (r'(రిజిస్ట్రేషన్ ఫీజు|ప్రాసెసింగ్ ఛార్జీలు చెల్లించండి)', 'Telugu: Upfront Charge Demand', 40, 'HIGH')
]

# 7. Brand Impersonation Targets
IMPERSONATION_TARGETS = [
    ('State Bank of India (SBI)', [r'\bsbi\b', r'\bstate bank\b', r'\byono\b', r'\bsbiinb\b', r'एसबीआई', r'స్టేట్ బ్యాంక్']),
    ('HDFC Bank', [r'\bhdfc\b', r'\bhdfcbank\b', r'एचडीएफसी']),
    ('ICICI Bank', [r'\bicici\b', r'\bimobile\b', r'आईसीआईसीआई']),
    ('Axis Bank', [r'\baxis\b', r'\baxisbank\b']),
    ('Punjab National Bank (PNB)', [r'\bpnb\b', r'\bpunjab national\b', r'पीएनबी']),
    ('Paytm / UPI Wallet', [r'\bpaytm\b', r'\bphonepe\b', r'\bgpay\b', r'\bgoogle pay\b', r'पेटीएम']),
    ('Income Tax Department', [r'\bincome tax\b', r'\bit department\b', r'\btax refund\b', r'आयकर विभाग']),
    ('Electricity Board', [r'\belectricity\b', r'\bbescom\b', r'\btneb\b', r'\bmsedcl\b', r'\bbill unpaid\b', r'बिजली विभाग', r'విద్యుత్ బోర్డు']),
    ('India Post / FedEx / Courier', [r'\bindia post\b', r'\bfedex\b', r'\bdhl\b', r'\bcourier parcel\b', r'डाक विभाग']),
    ('Police / Cyber Crime / CBI', [r'\bcyber police\b', r'\bpolice\b', r'\bcbi\b', r'\bcourt summons\b', r'\barrest warrant\b', r'\btrai\b', r'साइबर पुलिस', r'పోలీస్']),
    ('KBC Lottery Org', [r'\bkbc\b', r'\bkaun banega crorepati\b', r'केबीसी'])
]

# 8. Legitimate Mitigating Signals (Lowers risk if no critical threats exist)
SAFE_SIGNALS = [
    (r'\b(successfully received|payment received|credited to your a/c|debited from a/c)\b', 'Standard Transaction Confirmation', -15),
    (r'\b(available bal|clear bal|avl bal)\b', 'Bank Balance Notification Format', -10),
    (r'\ba/c\s*(no\.?)?\s*[*xX]{2,6}\d{3,4}\b', 'Masked Account Number (Standard Banking Practice)', -15),
    (r'\b(otp is.*never share|do not share this otp|bank never asks for otp)\b', 'Official Anti-Fraud Advisory Present', -20)
]


def detect_language(text: str) -> str:
    """Detect dominant language: English, Hindi, Telugu, or Mixed."""
    devanagari = len(re.findall(r'[\u0900-\u097F]', text))
    telugu = len(re.findall(r'[\u0C00-\u0C7F]', text))
    total_chars = len(text) or 1

    if devanagari / total_chars > 0.15:
        return 'hi'
    elif telugu / total_chars > 0.15:
        return 'te'
    elif devanagari > 0 or telugu > 0:
        return 'mixed'
    
    # Check for Romanized Hinglish / Teluglish keywords
    hinglish_words = ['aapka', 'turant', 'karein', 'jeeta', 'badhai', 'bijli', 'hoga', 'bataye']
    teluglish_words = ['mee', 'ventane', 'cheyandi', 'avthundi', 'kurchuni', 'ivvandi']
    lower = text.lower()
    
    if any(w in lower for w in hinglish_words):
        return 'mixed'
    if any(w in lower for w in teluglish_words):
        return 'mixed'
        
    return 'en'


def parse_qr_upi_payload(text: str) -> Optional[Dict[str, Any]]:
    """Inspect and decode UPI payment intent URIs (e.g. upi://pay?pa=...)."""
    if 'upi://pay' not in text.lower():
        return None

    try:
        parsed = urlparse(text.strip())
        qs = parse_qs(parsed.query)
        vpa = qs.get('pa', [''])[0]
        payee_name = qs.get('pn', [''])[0]
        amount = qs.get('am', [''])[0]
        note = qs.get('tn', [''])[0]

        is_suspicious_vpa = False
        warning = None

        if '@' in vpa:
            handle = vpa.split('@')[1].lower()
            # Personal handles posing as official organizations
            if any(k in payee_name.lower() for k in ['sbi', 'bank', 'police', 'lottery', 'electricity', 'customs']):
                if handle in ['okaxis', 'okhdfcbank', 'oksbi', 'ybl', 'paytm']:
                    is_suspicious_vpa = True
                    warning = f"Payee claims to be '{payee_name}' but the UPI VPA is a personal mobile account ({vpa})."

        return {
            'isUpiPayload': True,
            'vpa': vpa,
            'payeeName': payee_name,
            'amount': amount or 'Unspecified (Dynamic/Variable)',
            'note': note,
            'isSuspiciousVpa': is_suspicious_vpa,
            'warning': warning
        }
    except Exception as e:
        return None


def analyze_scam_advanced(text: str, custom_api_keys: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """
    ZERO CHILL 3.0 Unified Threat Evaluation.
    Combines multilingual NLP heuristics, URL threat intelligence,
    UPI QR payload inspection, and legal mapping.
    """
    if not text or not text.strip():
        return {
            'riskLevel': 'SAFE',
            'riskScore': 0,
            'color': 'green',
            'scamType': 'Empty Input',
            'confidenceScore': 0.99,
            'uncertaintyRating': 'Low',
            'language': 'en',
            'indicators': [],
            'highlightedPhrases': [],
            'explanation': 'No message text provided for analysis.',
            'recommendedSteps': ['Enter, paste, or upload message text to begin evaluation.'],
            'legalSections': [],
            'govServices': [],
            'detectedUrls': [],
            'qrAnalysis': None,
            'engine': 'ZERO CHILL 3.0 Threat Engine'
        }

    raw_text = text.strip()
    lower_text = raw_text.lower()
    detected_lang = detect_language(raw_text)

    score = 0
    indicators = []
    highlighted_phrases = []
    detected_scam_types = []

    # 1. Inspect QR / UPI Payloads if present
    qr_data = parse_qr_upi_payload(raw_text)
    if qr_data:
        score += 30
        indicators.append({
            'name': 'UPI Payment Intent Payload Detected',
            'severity': 'HIGH',
            'category': 'UPI Payment Trap',
            'description': f"Contains UPI pay command for VPA: {qr_data['vpa']}. Scanning this QR code will DEBIT money from your account."
        })
        if qr_data.get('isSuspiciousVpa'):
            score += 40
            indicators.append({
                'name': 'Spoofed Official Identity on Personal UPI VPA',
                'severity': 'CRITICAL',
                'category': 'Identity Spoofing',
                'description': qr_data['warning']
            })
            detected_scam_types.append('UPI Payment Impersonation')

    # 2. Inspect URLs with Deep Threat Intelligence
    url_pattern = re.compile(
        r'(https?://[^\s<>"\',;]+|www\.[^\s<>"\',;]+|[a-zA-Z0-9-]+\.(?:com|org|net|in|xyz|top|live|click|club|loan|info|biz|me|online|site|app)[^\s<>"\',;]*)',
        re.IGNORECASE
    )
    raw_urls = url_pattern.findall(raw_text)
    analyzed_urls = []

    for u in raw_urls:
        highlighted_phrases.append(u)
        url_audit = audit_url_deep(u, custom_api_keys)
        analyzed_urls.append(url_audit)

        if url_audit['riskScore'] >= 60:
            score += 40
            indicators.append({
                'name': f"High-Risk Phishing URL: {url_audit['domain']}",
                'severity': 'CRITICAL',
                'category': 'Malicious URL',
                'description': url_audit['summary']
            })
            detected_scam_types.append('Phishing URL Attack')
        elif url_audit['riskScore'] >= 25:
            score += 25
            indicators.append({
                'name': f"Suspicious Link: {url_audit['domain']}",
                'severity': 'HIGH',
                'category': 'Untrusted Link',
                'description': url_audit['summary']
            })

    has_links = len(analyzed_urls) > 0

    # 3. Helper pattern scanner
    def scan_pattern_list(patterns, category, default_type=None):
        nonlocal score
        matched_any = False
        for pattern, name, weight, severity in patterns:
            match = re.search(pattern, raw_text, re.IGNORECASE)
            if match:
                matched_any = True
                matched_str = match.group(0)
                highlighted_phrases.append(matched_str)
                score += weight
                indicators.append({
                    'name': name,
                    'severity': severity,
                    'category': category,
                    'description': f"Detected suspicious marker: '{matched_str}'."
                })
        if matched_any and default_type:
            detected_scam_types.append(default_type)

    # Scan all major pattern categories
    scan_pattern_list(CREDENTIAL_PATTERNS, 'Credential Harvesting', 'Credential & OTP Theft')
    scan_pattern_list(URGENCY_PATTERNS, 'Psychological Urgency', 'Coercive Social Engineering')
    scan_pattern_list(JOB_SCAM_PATTERNS, 'Job Fraud', 'Fake Work-From-Home Task Scam')
    scan_pattern_list(REWARD_PATTERNS, 'Financial Bait', 'Lottery / Prize Bait Fraud')
    scan_pattern_list(LOAN_PATTERNS, 'Predatory Lending', 'Predatory Instant Loan Fraud')
    scan_pattern_list(ADVANCE_FEE_PATTERNS, 'Advance-Fee Fraud', 'Advance-Fee Fraud')

    # 4. Check Brand & Authority Impersonation
    impersonated = []
    for org_name, org_patterns in IMPERSONATION_TARGETS:
        for p in org_patterns:
            m = re.search(p, raw_text, re.IGNORECASE)
            if m:
                impersonated.append(org_name)
                highlighted_phrases.append(m.group(0))
                break

    if impersonated and (has_links or any(i['category'] in ['Credential Harvesting', 'Psychological Urgency', 'UPI Payment Trap'] for i in indicators)):
        score += 35
        orgs_str = ', '.join(set(impersonated[:2]))
        indicators.append({
            'name': f"Brand Impersonation ({orgs_str})",
            'severity': 'CRITICAL' if has_links else 'HIGH',
            'category': 'Identity Spoofing',
            'description': f"Poses as {orgs_str} alongside high-pressure demands, unverified links, or credential requests."
        })
        detected_scam_types.append(f"{impersonated[0]} Phishing")

    # 5. Compound Multipliers
    if has_links and any(i['category'] == 'Psychological Urgency' for i in indicators):
        score += 20
    if has_links and any(i['category'] == 'Credential Harvesting' for i in indicators):
        score += 25

    # 6. Safe Mitigating Signals (Applied only if NO critical indicators exist)
    has_critical = any(ind['severity'] == 'CRITICAL' for ind in indicators)
    if not has_critical and not has_links:
        for pattern, name, reduction in SAFE_SIGNALS:
            if re.search(pattern, raw_text, re.IGNORECASE):
                score += reduction

    # Normalize Score (0 - 100)
    risk_score = max(0, min(100, int(score)))

    # Deduplicate Highlights
    unique_highlights = list(set([h.strip() for h in highlighted_phrases if len(h.strip()) > 2]))
    unique_highlights.sort(key=lambda s: len(s), reverse=True)

    # Determine Classification & Primary Category
    if risk_score >= 60:
        risk_level = 'HIGH-RISK SCAM'
        color = 'red'
        primary_category = detected_scam_types[0] if detected_scam_types else 'Phishing / Financial Extortion'
        explanation = (
            f"This message exhibits strong characteristics of a {primary_category}. "
            "It combines artificial panic, requests for secret credentials, or unverified links "
            "designed to compromise bank accounts, steal funds, or harvest personal identity."
        )
        recommendations = [
            "DO NOT click any link in this message, scan any QR code, or call any provided telephone number.",
            "NEVER share your OTP, UPI PIN, ATM PIN, or banking passwords with anyone under any circumstances.",
            "Block and report the sender immediately in your SMS or messaging application.",
            "If this claims to be your bank, verify directly via your official banking app or the phone number behind your debit card.",
            "If financial loss occurred in India, immediately dial the National Cybercrime Helpline 1930 or lodge an incident at cybercrime.gov.in within the 2-Hour Golden Window."
        ]
        confidence = 0.96 if len(indicators) >= 2 else 0.88
        uncertainty = 'Low'
    elif risk_score >= 25:
        risk_level = 'SUSPICIOUS'
        color = 'amber'
        primary_category = detected_scam_types[0] if detected_scam_types else 'Unverified Promotional / Coercive Pitch'
        explanation = (
            "One or more warning signs were detected in this message. "
            "Cyber fraudsters routinely use unsolicited job invitations, easy loan promises, "
            "or artificial deadlines to initiate contact before demanding upfront fees or sensitive data."
        )
        recommendations = [
            "Do not click links or call numbers sent in unsolicited messages.",
            "Verify any job offer, loan, or service update directly through the company's verified website.",
            "Never pay upfront 'processing fees', 'registration charges', or 'VIP task deposits'.",
            "Do not download any APK files, AnyDesk, or TeamViewer apps suggested by the sender.",
            "Report suspicious messages to Sanchar Saathi Chakshu (sancharsaathi.gov.in/sfc/)."
        ]
        confidence = 0.86
        uncertainty = 'Moderate'
    else:
        risk_level = 'SAFE'
        color = 'green'
        primary_category = 'Legitimate Notification Pattern'
        explanation = (
            "No significant scam indicators, malicious URLs, or credential-harvesting patterns were detected. "
            "The message resembles routine informational or transactional communication."
        )
        recommendations = [
            "Important: Automated scanning cannot guarantee 100% authenticity.",
            "Never share OTPs, passwords, or PINs, even if a message seems genuine.",
            "Always inspect URLs carefully before entering any banking or personal details.",
            "If an unexpected payment request follows, verify directly with your bank."
        ]
        confidence = 0.90
        uncertainty = 'Low'

    # Filter out safe signals from user-facing indicators
    user_indicators = [ind for ind in indicators if ind['severity'] != 'SAFE_SIGNAL']

    # Retrieve relevant Indian Cyber Laws and Government Services
    relevant_laws = get_relevant_laws_for_category(primary_category)
    relevant_services = get_services_for_category(primary_category)

    return {
        'riskLevel': risk_level,
        'riskScore': risk_score,
        'color': color,
        'scamType': primary_category,
        'confidenceScore': confidence,
        'uncertaintyRating': uncertainty,
        'language': detected_lang,
        'indicators': user_indicators,
        'highlightedPhrases': unique_highlights,
        'explanation': explanation,
        'recommendedSteps': recommendations,
        'legalSections': relevant_laws,
        'govServices': relevant_services,
        'detectedUrls': analyzed_urls,
        'qrAnalysis': qr_data,
        'engine': 'ZERO CHILL 3.0 AI Threat Engine'
    }

# Backward compatibility alias
def analyze_scam_message(text: str) -> Dict[str, Any]:
    return analyze_scam_advanced(text)
