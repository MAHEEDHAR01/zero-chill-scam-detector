# ZERO CHILL 3.0 – Ultimate AI Cybersecurity, Cybercrime Prevention & Legal Action Platform

🏆 **National Hackathon Edition** | Built for Citizen Protection, Digital Evidence Management & Legal Awareness in India.

---

## 🛡️ Executive Summary & Vision

**ZERO CHILL 3.0** is an enterprise-grade, civic cybersecurity platform that transforms how Indian citizens detect digital fraud, preserve forensic-quality evidence, understand their rights under the **Information Technology Act, 2000** and the **Bharatiya Nyaya Sanhita, 2023 (BNS)**, and access official government remediation services.

Unlike basic keyword scanners, ZERO CHILL 3.0 is a complete end-to-end cyber defense ecosystem:
1. **Detects**: 15+ scam categories across English, हिन्दी (Hindi), and తెలుగు (Telugu).
2. **Educates**: Maps specific scams directly to statutory offenses (IT Act Sec 66C, 66D, 43; BNS Sec 318, 351).
3. **Preserves**: Digital Evidence Vault with automated sensitive PII redaction and formal police dockets.
4. **Responds**: Step-by-step guidance on the **2-Hour Golden Window** to freeze funds via **1930** and file at **cybercrime.gov.in**.

---

## ⚡ Quick Start & Live Demonstration

### 1. Prerequisites
- Python 3.10+ (Tested on Python 3.14)
- Google Chrome, Microsoft Edge, Brave, or Firefox

### 2. Start Application
```powershell
cd c:\Users\HP\Downloads\hack
python app.py
```

### 3. Open in Browser
👉 Navigate to **[http://localhost:5000](http://localhost:5000)**

---

## 🏛️ The 8 Core Pillars of ZERO CHILL 3.0

### 1. 🛡️ Multi-Method Threat Scanner
- **Text & Message Scanner**: Instant natural language threat evaluation for SMS, WhatsApp chats, and social messages.
- **Screenshot OCR Scanner**: Optical character recognition (Tesseract.js) extracting text from uploaded JPG, PNG, and JPEG screenshots with live progress.
- **Web Link & Domain Threat Intelligence**: Protocol auditing (HTTP vs HTTPS), domain lookalikes/typosquatting, high-risk TLDs (`.xyz`, `.top`, `.click`), URL shortener expansion, and IP host checks.
- **Email Phishing Scanner**: Analyzes email headers, sender address spoofing, and urgent verification traps.
- **QR Code & UPI Destination Scanner**: Inspects `upi://pay?pa=...` payloads. Warns if a "Receive Money" request will actually DEBIT funds from the victim.

### 2. ⚡ Real-World Cybercrime Action Center
Contextual, step-by-step containment playbooks:
- **Bank Phishing & OTP Compromise**: Emergency card freezing, UPI MPIN reset, 1930 Golden Window reporting.
- **Fake Work-from-Home Task Scams**: Halting deposits, documenting Telegram recruiter handles, Sanchar Saathi reporting.
- **Predatory Loan Apps**: Revoking storage/contact permissions, verifying against the RBI Sachet NBFC registry, filing extortion complaints.
- **Digital Arrest Extortion**: Identifying fake Skype/WhatsApp police trials, preserving video evidence, contacting I4C.

### 3. 🏛️ Verified Indian Government Services Directory
Direct integration with verified official portals:
- **National Cyber Crime Reporting Portal** (`cybercrime.gov.in`)
- **Cyber Financial Fraud Helpline** (`1930`) – 24x7 Citizen Financial Cyber Fraud Reporting System
- **Sanchar Saathi – Chakshu** (`sancharsaathi.gov.in/sfc/`) – Suspected fraud call/SMS reporting
- **RBI Sachet** (`sachet.rbi.org.in/`) – Complaints against unauthorized digital lending apps
- **CERT-In** (`cert-in.org.in`) – Incident reporting & malware advisories
- **RBI Ombudsman** (`rbi.org.in`) – Banking deficiency & unauthorized transaction redressal
- **TRAI DND** (`trai.gov.in`) – Commercial spam SMS regulations
- **PIB Fact Check** (`pib.gov.in`) – Debunking fake government scheme circulars
- **India Code** (`indiacode.nic.in`) – Authoritative legislative repository

### 4. ⚖️ Indian Cyber Law & Legal Rights Center
Authoritative statutory provisions with simple English & vernacular explanations, realistic scenarios, and penalties:
- **IT Act, 2000 Section 43**: Unauthorized data access & APK malware damage (civil compensation up to ₹1 Crore).
- **IT Act, 2000 Section 66**: Computer-related offences (up to 3 years imprisonment + ₹5 Lakh fine).
- **IT Act, 2000 Section 66C**: Identity theft, OTP, and PIN theft (up to 3 years imprisonment + fine).
- **IT Act, 2000 Section 66D**: Cheating by personation using computer resource (up to 3 years imprisonment + fine).
- **IT Act, 2000 Section 66E**: Violation of privacy & sextortion (up to 3 years imprisonment + fine).
- **IT Act, 2000 Section 70B**: CERT-In national incident response powers.
- **Bharatiya Nyaya Sanhita, 2023 Section 316**: Criminal breach of trust.
- **Bharatiya Nyaya Sanhita, 2023 Section 318(4)**: Cheating & dishonestly inducing delivery of property (up to 7 years imprisonment).
- **Bharatiya Nyaya Sanhita, 2023 Section 336 & 338**: Forgery of electronic records & fake government notices.
- **Bharatiya Nyaya Sanhita, 2023 Section 351**: Criminal intimidation & extortion (Digital Arrest threats).

### 5. 📂 Secure Digital Evidence Vault
- **Multi-Format Support**: Upload SMS screenshots, WhatsApp exports, bank receipts, PDFs, and TXT files (up to 10MB).
- **Automated PII Redaction**: Masks 16-digit card numbers, strips OTPs, and partially redacts phone numbers.
- **Metadata Recording**: Incident title, category, date/time, monetary loss, transaction UTR number, and suspect details.
- **Printable Police Docket**: One-click generation of a formal HTML Complaint Docket ready for printing or saving as PDF for police submission.

### 6. 📰 Cyber News & Verified Advisories
- Real, authentic advisories from CERT-In, RBI, TRAI, and PIB Fact Check.
- Category filters (Extortion, UPI, Malware, Phishing, Job Fraud) and search.
- Verified publication dates and direct links to official bulletins.

### 7. 🤖 Multilingual AI Safety Assistant
- Conversational chat assistant in **English**, **हिन्दी (Hindi)**, and **తెలుగు (Telugu)**.
- Powered by Google Gemini 2.5 Flash with an intelligent offline cyber defense knowledge fallback.
- Explains scams, emergency 1930 procedures, and legal rights in natural, empathetic language.

### 8. 📊 Telemetry & Analytics Dashboard
- Backed by an **SQLite database** (`zero_chill.db`).
- Live metrics: Total scans, Safe/Suspicious/High-Risk breakdown, average risk score.
- Dynamic threat distribution charts and searchable scan logs.

---

## 🎯 Hackathon Demonstration Benchmarks

Test these scenarios using the one-click buttons on the main screen:

| Benchmark | Sample Text | Expected Classification | Key Indicators |
| :--- | :--- | :--- | :--- |
| **SAFE** | *"Your electricity bill payment of Rs. 850 was successfully received. Thank you."* | **SAFE (Score: 0)** | Standard receipt, no hyperlinks, no calls to action. |
| **SUSPICIOUS** | *"Congratulations! You have been selected for a work-from-home job. Contact us immediately for more details."* | **SUSPICIOUS (Score: 55)** | Unsolicited job offer, artificial urgency (`immediately`). |
| **HIGH-RISK SCAM** | *"Your bank account will be blocked today! Verify your account immediately by clicking http://fake-bank-example.com and entering your OTP."* | **HIGH-RISK (Score: 100)** | Account block threat, multi-hyphen spoofed domain, OTP theft. |
| **HINDI SMISHING** | *"प्रिय ग्राहक, आपका एसबीआई बैंक खाता आज रात बंद हो जाएगा! तुरंत http://sbi-kyc-update.xyz पर जाएं और अपना ओटीपी दर्ज करें।"* | **HIGH-RISK (Score: 100, Lang: hi)** | Devanagari KYC threat, .xyz phishing domain, OTP demand. |
| **TELUGU LOTTERY** | *"మీ మొబైల్ నంబర్ KBC లక్కీ డ్రాలో 25 లక్షల రూపాయలు గెలుచుకుంది! నగదును క్లెయిమ్ చేయడానికి వెంటనే 499 రూపాయల రిజిస్ట్రేషన్ ఫీజు చెల్లించండి."* | **HIGH-RISK (Score: 100, Lang: te)** | Telugu KBC prize claim, upfront ₹499 fee demand. |
| **UPI QR TRAP** | *`upi://pay?pa=scammer99@okhdfcbank&pn=State%20Bank%20of%20India&am=5000&cu=INR`* | **HIGH-RISK (Score: 70)** | Debit intent masquerading as credit, personal VPA posing as bank. |

---

## 🏗️ Technical Architecture

```
hack/
├── app.py                      # Flask REST API server & static router
├── database.py                 # SQLite schema (scans, evidence, advisories, telemetry)
├── scam_engine.py              # Multilingual threat heuristics & legal mapping
├── cyber_laws.py               # IT Act 2000 & BNS 2023 legal rights repository
├── gov_services.py             # 9+ verified Indian government services directory
├── news_advisories.py          # Real advisories from CERT-In, RBI, TRAI, MHA
├── url_intelligence.py         # Domain reputation, lookalike, shortener engine
├── evidence_manager.py         # Evidence upload, PII redaction, PDF/TXT parsing, dockets
├── ai_assistant.py             # Gemini 2.5 Flash multilingual conversational agent
├── requirements.txt            # Python dependencies
├── uploads/                    # Secure local evidence vault directory
├── static/
│   ├── css/
│   │   └── style.css           # Glassmorphism, animations, cyber grid styling
│   └── js/
│       ├── app.jsx             # React 18 single-page application
│       ├── data/
│       │   └── samples.js      # Hackathon demo benchmarks & safety rules
│       └── utils/
│           └── localAnalyzer.js # Client-side instant heuristic fallback engine
└── templates/
    └── index.html              # HTML shell loading React 18, Tailwind, Tesseract.js
```

---

## 🔒 Privacy, Security & Responsible AI Guarantees

- **Non-Affiliation Notice**: ZERO CHILL 3.0 is an independent civic defense tool. It clearly discloses it is not an official government agency and never auto-submits complaints without explicit user action.
- **Zero Sensitive Data Storage**: Passwords, OTPs, and UPI PINs are never stored. The evidence module automatically redacts card numbers, Aadhaar, and OTPs.
- **No Automatic Link Traversal**: Suspect URLs are never auto-clicked or triggered.
- **Anti-Complacency Rule**: The platform never guarantees that a "SAFE" scan implies 100% authenticity.
