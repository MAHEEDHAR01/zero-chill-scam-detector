"""
ZERO CHILL 3.0 – Verified Cybercrime News & Official Advisories Library
Authentic, verified advisories from CERT-In, RBI, TRAI, MHA / I4C, and PIB Fact Check.
"""

from typing import Dict, Any, List, Optional

VERIFIED_ADVISORIES: List[Dict[str, Any]] = [
    {
        "id": "adv-mha-digital-arrest-2024",
        "title": "MHA & I4C National Advisory: Spurt in 'Digital Arrest' Extortion Scams",
        "source": "Ministry of Home Affairs / I4C",
        "sourceUrl": "https://cybercrime.gov.in/",
        "publishedDate": "2024-10-27",
        "category": "Extortion & Impersonation",
        "severity": "CRITICAL",
        "summary": (
            "The Indian Cyber Crime Coordination Centre (I4C) issued a high-priority national advisory warning citizens "
            "against 'Digital Arrest' scams. Fraudsters posing as CBI, Police, Customs, or TRAI officials intimidate victims "
            "over Skype and WhatsApp video calls from fake police stations, falsely claiming their Aadhaar/SIM is linked to "
            "money laundering or narcotics, and coercing them into liquidating bank deposits."
        ),
        "actionableAdvice": [
            "Indian law enforcement agencies NEVER place individuals under 'Digital Arrest' or hold video court sessions.",
            "Never transfer money to so-called 'RBI secret verification accounts' or 'Supreme Court clearing escrow accounts'.",
            "Immediately disconnect such video calls, dial 1930, and inform local police."
        ]
    },
    {
        "id": "adv-rbi-upi-pin-scams",
        "title": "RBI Kehta Hai: UPI PIN is Only Required to DEBIT Money, Never to Receive Funds",
        "source": "Reserve Bank of India (RBI)",
        "sourceUrl": "https://www.rbi.org.in/",
        "publishedDate": "2024-08-15",
        "category": "UPI & Payment Fraud",
        "severity": "HIGH",
        "summary": (
            "The Reserve Bank of India reiterated that UPI PIN is used strictly for authenticating outgoing payments "
            "(debits). Scammers on online classifieds (OLX, Facebook Marketplace) send 'Collect Requests' or QR codes claiming "
            "'Enter your UPI PIN to receive the advance payment'. Entering the PIN instantly transfers money to the scammer."
        ),
        "actionableAdvice": [
            "You NEVER need to enter your UPI PIN, MPIN, or scan a QR code to RECEIVE money.",
            "Decline all unexpected 'Collect Requests' in Google Pay, PhonePe, and Paytm.",
            "If an unauthorized debit occurs, immediately raise a dispute in the UPI app and call 1930."
        ]
    },
    {
        "id": "adv-cert-in-banking-trojans",
        "title": "CERT-In Advisory CIAD-2024-0038: Android Banking Trojans Mimicking Official Bank Apps",
        "source": "CERT-In (MeitY)",
        "sourceUrl": "https://www.cert-in.org.in/",
        "publishedDate": "2024-09-12",
        "category": "Malware & Phishing",
        "severity": "CRITICAL",
        "summary": (
            "CERT-In detected malicious campaigns delivering banking Trojans (variants of Chameleon and SOVA) "
            "via WhatsApp messages pretending to be official APK updates for SBI YONO, PNB, and HDFC netbanking. "
            "Once installed, the malware captures keystrokes, intercepts 2FA SMS OTPs, and executes automated fund transfers."
        ),
        "actionableAdvice": [
            "Never install Android APK files received via WhatsApp, SMS, or Telegram.",
            "Download banking apps exclusively from the official Google Play Store or Apple App Store.",
            "Enable Google Play Protect and verify app developer details before installation."
        ]
    },
    {
        "id": "adv-dot-electricity-sms-alert",
        "title": "DoT & Sanchar Saathi Alert: Fraudulent Electricity Disconnection SMS Targeting Consumers",
        "source": "Department of Telecommunications",
        "sourceUrl": "https://sancharsaathi.gov.in/",
        "publishedDate": "2024-06-20",
        "category": "SMS Phishing (Smishing)",
        "severity": "HIGH",
        "summary": (
            "The Department of Telecommunications warned of widespread fraudulent SMS sent from personal mobile numbers "
            "falsely claiming: 'Dear consumer, your electricity power will be disconnected tonight at 9:30 PM due to unpaid bill. "
            "Contact Officer at 98xxxxxx'. Callers persuade victims to install AnyDesk or TeamViewer to steal bank credentials."
        ),
        "actionableAdvice": [
            "Official power distribution companies (Discoms) NEVER send disconnection notices from personal 10-digit mobile numbers.",
            "Discom messages always carry registered 6-character alphanumeric headers (e.g. BESCOM, TNEB, MSEDCL).",
            "Report such numbers immediately on the Chakshu portal (sancharsaathi.gov.in/sfc/)."
        ]
    },
    {
        "id": "adv-pib-youtube-like-job-scam",
        "title": "PIB Fact Check: Beware of Fraudulent 'Like YouTube Videos & Earn ₹3,500 Daily' Job Scams",
        "source": "Press Information Bureau (PIB)",
        "sourceUrl": "https://pib.gov.in/",
        "publishedDate": "2024-04-18",
        "category": "Fake Job & Task Fraud",
        "severity": "HIGH",
        "summary": (
            "PIB Fact Check debunked viral WhatsApp recruitment messages offering lucrative part-time work reviewing hotels "
            "or liking YouTube videos. In this classic task scam, victims receive small payouts of ₹150–₹500 initially, then are "
            "trapped into depositing lakhs of rupees under 'VIP Prepaid Task Schemes' that freeze all funds."
        ),
        "actionableAdvice": [
            "No legitimate company pays money for simply liking social media videos or subscribing to channels.",
            "Never pay any 'registration fee', 'training kit charge', or 'VIP investment deposit' to claim job salaries.",
            "Report the recruiter's Telegram and WhatsApp numbers to cybercrime.gov.in."
        ]
    },
    {
        "id": "adv-rbi-unauthorized-loan-apps",
        "title": "RBI Comprehensive Advisory: Precautions Against Predatory Unregistered Digital Lending Apps",
        "source": "Reserve Bank of India (RBI)",
        "sourceUrl": "https://sachet.rbi.org.in/",
        "publishedDate": "2024-05-10",
        "category": "Predatory Loan Apps",
        "severity": "CRITICAL",
        "summary": (
            "RBI cautioned against fraudulent instant loan applications distributed via social media and third-party stores. "
            "These apps disburse short-term loans with 50% upfront deductions, then harass victims by accessing their photo gallery "
            "and contact lists to circulate morphed pictures and demand extortionate weekly interest."
        ),
        "actionableAdvice": [
            "Verify whether the lender is an RBI-registered Bank or NBFC using the official list on rbi.org.in.",
            "Never grant permission to your contacts list, photo gallery, or device storage to instant loan apps.",
            "Lodge immediate complaints on the RBI Sachet portal (sachet.rbi.org.in) and 1930."
        ]
    },
    {
        "id": "adv-trai-sms-headers-traceability",
        "title": "TRAI Mandate on Traceability of Commercial SMS and Action Against Fraudulent Headers",
        "source": "TRAI",
        "sourceUrl": "https://www.trai.gov.in/",
        "publishedDate": "2024-08-30",
        "category": "Telecom Governance",
        "severity": "ADVISORY",
        "summary": (
            "TRAI directed all Access Service Providers to implement full end-to-end traceability of commercial messages "
            "to curb fraudulent SMS traffic originating from unregistered telemarketers (UTMs). Over 1.8 million blacklisted mobile "
            "numbers were disconnected across India in concerted anti-smishing drives."
        ),
        "actionableAdvice": [
            "Always inspect SMS sender IDs: Banks and trusted brands use strictly regulated 6-character sender headers (e.g. AX-HDFCBK).",
            "Report spam and scam messages to your telecom operator by forwarding to 1909.",
            "Never click shortened links (bit.ly, tinyurl) sent via SMS without verifying the true destination domain."
        ]
    }
]

def get_all_advisories(category: Optional[str] = None, search: Optional[str] = None) -> List[Dict[str, Any]]:
    """Return filtered verified advisories."""
    results = VERIFIED_ADVISORIES

    if category and category != 'ALL':
        results = [a for a in results if a['category'].lower() == category.lower()]

    if search and search.strip():
        q = search.strip().lower()
        results = [
            a for a in results 
            if q in a['title'].lower() or q in a['summary'].lower() or q in a['source'].lower()
        ]

    return results
