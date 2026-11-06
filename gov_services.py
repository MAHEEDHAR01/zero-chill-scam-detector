"""
ZERO CHILL 3.0 – Indian Government Cyber Safety & Reporting Services Directory
Verified official government portals, responsible departments, and step-by-step reporting protocols.
"""

from typing import Dict, Any, List

GOV_SERVICES_DIRECTORY: List[Dict[str, Any]] = [
    {
        "id": "helpline-1930",
        "serviceName": "National Cyber Financial Fraud Helpline (1930)",
        "responsibleDept": "Indian Cyber Crime Coordination Centre (I4C), Ministry of Home Affairs",
        "category": "Immediate Financial Emergency",
        "isEmergency": True,
        "phone": "1930",
        "officialUrl": "https://cybercrime.gov.in/",
        "lastVerified": "2026-11-01",
        "whatItDoes": (
            "Operates the Citizen Financial Cyber Fraud Reporting and Management System (CFCFRMS). "
            "Coordinates in real-time with over 250 banks, payment aggregators, and wallets to place an immediate "
            "temporary hold (freeze) on the fraudster's bank account before money is withdrawn at an ATM or converted to crypto."
        ),
        "whenToUse": (
            "Use IMMEDIATELY when money has been unauthorizedly debited or transferred due to OTP fraud, phishing, "
            "fake UPI links, investment scams, or predatory loan extortion. The first 2 hours are the 'Golden Window'."
        ),
        "stepByStepInstructions": [
            "Dial 1930 from your mobile phone immediately after the unauthorized transaction.",
            "Provide the police operator with your Name, Mobile Number, Bank Name, Account Number, and Transaction Amount.",
            "Share the UTR (Unique Transaction Reference) / Ref ID number from your bank's debit SMS.",
            "The operator records a formal ticket in the CFCFRMS and sends an automated SMS with your Complaint Reference Number.",
            "Log onto cybercrime.gov.in within 24 hours using the Reference Number to complete the detailed incident submission."
        ],
        "requiredDocuments": [
            "Bank account number and debit card details",
            "Transaction reference number (UTR / IMPS / UPI Ref ID)",
            "Bank SMS alert showing amount, date, and timestamp",
            "Suspect's mobile number, UPI ID, or account number if known"
        ]
    },
    {
        "id": "cybercrime-portal",
        "serviceName": "National Cyber Crime Reporting Portal",
        "responsibleDept": "Ministry of Home Affairs (MHA), Government of India",
        "category": "Official Police Reporting",
        "isEmergency": False,
        "officialUrl": "https://cybercrime.gov.in/",
        "lastVerified": "2026-11-01",
        "whatItDoes": (
            "The official central government portal to lodge online cybercrime complaints. "
            "Routes complaints directly to the State Cyber Crime Police Station having territorial jurisdiction."
        ),
        "whenToUse": (
            "Use to register formal police complaints for financial cyber fraud, impersonation, social media harassment, "
            "extortion, identity theft, malware/ransomware attacks, and cyber offences against women and children."
        ),
        "stepByStepInstructions": [
            "Visit cybercrime.gov.in and click on 'Report Cyber Crime'.",
            "Select 'Report Financial Fraud' or 'Report Other Cyber Crime' (or Women/Child related crime).",
            "Accept the terms, enter your state and mobile number to receive an OTP login.",
            "Fill in incident details: Date, Time, Suspect Details (Phone, Website, Social Profile), and Loss Amount.",
            "Upload digital evidence (screenshots, bank statements, chat exports) and submit.",
            "Download and save the PDF Complaint Acknowledgment with your unique Complaint ID."
        ],
        "requiredDocuments": [
            "Government photo ID (Aadhaar / Voter ID / PAN)",
            "Bank statement showing the fraudulent transaction with UTR number",
            "Full screenshots of suspicious SMS, WhatsApp chats, or phishing email headers",
            "URLs of fraudulent websites or social media profiles"
        ]
    },
    {
        "id": "chakshu-sancharsaathi",
        "serviceName": "Sanchar Saathi – Chakshu (चक्षु)",
        "responsibleDept": "Department of Telecommunications (DoT), Ministry of Communications",
        "category": "Telecom & Number Disconnection",
        "isEmergency": False,
        "officialUrl": "https://sancharsaathi.gov.in/sfc/",
        "lastVerified": "2026-11-01",
        "whatItDoes": (
            "A citizen-centric facility enabling telecom users to report suspected fraudulent calls, SMS, and WhatsApp "
            "messages. Triggers telecommunication carrier investigations leading to blacklisting of IMEI and permanent mobile disconnection."
        ),
        "whenToUse": (
            "Use when you receive suspicious SMS, calls, or WhatsApp messages claiming KYC expiry, electricity power disconnection, "
            "fake lottery wins, or fraudulent job offers, EVEN IF you have NOT lost money."
        ),
        "stepByStepInstructions": [
            "Navigate to sancharsaathi.gov.in/sfc/.",
            "Choose medium: 'Call', 'SMS', or 'WhatsApp'.",
            "Select the scam category (e.g. Bank/KYC update, Job offer, Lottery/Prize, Electricity disconnection).",
            "Enter the suspect mobile number, date & time, and paste the exact message text.",
            "Attach a screenshot of the message/call log and submit with your verified mobile OTP."
        ],
        "requiredDocuments": [
            "Suspect mobile number or sender ID (e.g. +91-9876543210)",
            "Screenshot of the SMS, WhatsApp chat, or call history log",
            "Exact date and time of the unsolicited communication"
        ]
    },
    {
        "id": "rbi-sachet",
        "serviceName": "RBI Sachet Portal",
        "responsibleDept": "Reserve Bank of India (RBI)",
        "category": "Financial & Loan Apps",
        "isEmergency": False,
        "officialUrl": "https://sachet.rbi.org.in/",
        "lastVerified": "2026-11-01",
        "whatItDoes": (
            "RBI's dedicated supervisory portal to detect and deter illegal deposit schemes, unauthorized financial entities, "
            "fraudulent investment apps, and unregistered predatory digital loan applications."
        ),
        "whenToUse": (
            "Use to check whether a loan app/entity is genuinely registered with RBI, or to lodge complaints against "
            "unauthorized digital lenders, Ponzi investment schemes, and harassing loan recovery agents."
        ),
        "stepByStepInstructions": [
            "Visit sachet.rbi.org.in.",
            "Click 'File a Complaint' on the homepage.",
            "Select whether the entity is registered with RBI or an unverified / unauthorized company.",
            "Provide the company name, app link, bank account where payments were demanded, and describe the harassment or fraud.",
            "Upload sanction letters, repayment receipts, or threatening WhatsApp chats, then submit."
        ],
        "requiredDocuments": [
            "Name of the suspicious loan/investment app or website",
            "Bank statement or UPI transaction proof of payment",
            "Screenshots of loan app permissions, agreements, or recovery threats"
        ]
    },
    {
        "id": "cert-in",
        "serviceName": "CERT-In (Indian Computer Emergency Response Team)",
        "responsibleDept": "Ministry of Electronics and Information Technology (MeitY)",
        "category": "Cyber Threat & Incident Response",
        "isEmergency": False,
        "officialUrl": "https://www.cert-in.org.in/",
        "lastVerified": "2026-11-01",
        "whatItDoes": (
            "National nodal agency for cybersecurity incident response under IT Act Section 70B. "
            "Tracks large-scale phishing campaigns, collects telemetry on active malware infrastructure, and issues binding advisories."
        ),
        "whenToUse": (
            "Use when reporting malicious Android APK links, widespread phishing campaigns mimicking government portals, "
            "ransomware outbreaks, or website defacements."
        ),
        "stepByStepInstructions": [
            "Visit cert-in.org.in and locate the 'Incident Reporting' section.",
            "Alternatively, send an email directly to incident@cert-in.org.in.",
            "Provide technical indicators: malicious URL, APK package name/hash, phishing domain whois, email headers.",
            "CERT-In incident analysts examine the telemetry and coordinate domain takedowns with registries and ISPs."
        ],
        "requiredDocuments": [
            "Full URL / Domain address of the phishing page",
            "Original RFC 822 email headers (if email phishing)",
            "Sample of suspicious APK file or installation URL"
        ]
    },
    {
        "id": "rbi-main",
        "serviceName": "Reserve Bank of India (RBI Banking Ombudsman)",
        "responsibleDept": "Reserve Bank of India",
        "category": "Banking Redressal",
        "isEmergency": False,
        "officialUrl": "https://www.rbi.org.in/",
        "lastVerified": "2026-11-01",
        "whatItDoes": (
            "Administers the Reserve Bank - Integrated Ombudsman Scheme (RB-IOS). "
            "Handles consumer grievances regarding unauthorized electronic banking transactions and bank deficiency of service."
        ),
        "whenToUse": (
            "Use if your bank fails to resolve unauthorized electronic debits within 30 days under RBI's Limited Customer Liability Circular (2017)."
        ),
        "stepByStepInstructions": [
            "Lodge a formal written dispute with your bank first and note the Complaint Reference Number.",
            "If unresolved after 30 days, visit cms.rbi.org.in (RBI Complaint Management System).",
            "Submit the complaint against your bank with date of dispute and transaction proofs."
        ],
        "requiredDocuments": [
            "Copy of the initial complaint made to the bank",
            "Bank's reply or proof of 30 days lapse",
            "Account statement and transaction proofs"
        ]
    },
    {
        "id": "trai-dnd",
        "serviceName": "TRAI – Telecom Commercial Communication Regulations (DND)",
        "responsibleDept": "Telecom Regulatory Authority of India",
        "category": "Spam SMS & Telemarketing",
        "isEmergency": False,
        "officialUrl": "https://www.trai.gov.in/",
        "lastVerified": "2026-11-01",
        "whatItDoes": (
            "Regulates Unsolicited Commercial Communications (UCC). Enforces strict telemarketer registration "
            "and penalizes unregistered senders sending spam SMS and promotional calls."
        ),
        "whenToUse": (
            "Use to register Do Not Disturb (DND) preferences or report recurring promotional spam messages and robocalls."
        ),
        "stepByStepInstructions": [
            "SMS 'START 0' to 1909 to enable full DND on any Indian mobile connection.",
            "To report spam SMS: Forward the message within 3 days to 1909 in format: 'Spam SMS text, Sender Number, Date (dd/mm/yy)'."
        ],
        "requiredDocuments": [
            "Sender ID / Phone number",
            "Date and time of spam receipt"
        ]
    },
    {
        "id": "pib-factcheck",
        "serviceName": "PIB Fact Check Unit",
        "responsibleDept": "Press Information Bureau, Ministry of Information & Broadcasting",
        "category": "Government Scheme Verification",
        "isEmergency": False,
        "officialUrl": "https://pib.gov.in/",
        "lastVerified": "2026-11-01",
        "whatItDoes": (
            "Official fact-checking body that identifies and debunks fake government notifications, "
            "fraudulent recruitment drives, fake subsidy schemes, and morphed official circulars."
        ),
        "whenToUse": (
            "Use when you receive messages claiming the government is offering free laptops, cash under PM schemes, "
            "or hiring for government departments via unofficial channels."
        ),
        "stepByStepInstructions": [
            "Verify debunked claims at factcheck.pib.gov.in or twitter.com/PIBFactCheck.",
            "Submit suspicious circulars for verification via WhatsApp to +91 8799711259 or email socialmedia@pib.gov.in."
        ],
        "requiredDocuments": [
            "Screenshot of the viral claim or circular",
            "Text or link of the viral message"
        ]
    },
    {
        "id": "india-code",
        "serviceName": "India Code – Digital Legal Repository",
        "responsibleDept": "Legislative Department, Ministry of Law and Justice",
        "category": "Official Statutes & Legal Texts",
        "isEmergency": False,
        "officialUrl": "https://www.indiacode.nic.in/",
        "lastVerified": "2026-11-01",
        "whatItDoes": (
            "The official central digital repository of all Central and State Acts, providing unamended and "
            "up-to-date authoritative legal texts of Indian legislation including the IT Act 2000 and BNS 2023."
        ),
        "whenToUse": (
            "Use to inspect the official, authentic wording, sections, and legal definitions of Indian statutes."
        ),
        "stepByStepInstructions": [
            "Visit indiacode.nic.in and search by Act Name (e.g. 'Information Technology Act, 2000').",
            "Read full section text, official footnotes, and legal amendment histories."
        ],
        "requiredDocuments": []
    }
]

def get_services_for_category(scam_category: str) -> List[Dict[str, Any]]:
    """Recommend the most effective official government services based on detected scam category."""
    cat_lower = (scam_category or "").lower()
    selected_ids = []

    # Financial loss / Banking phishing / UPI
    if any(k in cat_lower for k in ["bank", "phishing", "otp", "upi", "financial", "credential"]):
        selected_ids = ["helpline-1930", "cybercrime-portal", "chakshu-sancharsaathi", "rbi-main"]
    # Loan scams
    elif "loan" in cat_lower:
        selected_ids = ["rbi-sachet", "cybercrime-portal", "helpline-1930", "chakshu-sancharsaathi"]
    # Job / Task / Lottery scams
    elif any(k in cat_lower for k in ["job", "work", "lottery", "prize", "advance", "kbc"]):
        selected_ids = ["cybercrime-portal", "chakshu-sancharsaathi", "helpline-1930"]
    # Digital arrest / Extortion / Police
    elif any(k in cat_lower for k in ["arrest", "police", "extortion", "threat", "customs", "cbi"]):
        selected_ids = ["helpline-1930", "cybercrime-portal", "chakshu-sancharsaathi"]
    # Government impersonation
    elif any(k in cat_lower for k in ["government", "income tax", "electricity", "subsidy", "challan"]):
        selected_ids = ["pib-factcheck", "chakshu-sancharsaathi", "cybercrime-portal"]
    else:
        selected_ids = ["helpline-1930", "cybercrime-portal", "chakshu-sancharsaathi"]

    services = [s for s in GOV_SERVICES_DIRECTORY if s["id"] in selected_ids]
    return services if services else GOV_SERVICES_DIRECTORY[:3]
