"""
ZERO CHILL 3.0 – Indian Cyber Law & Legal Rights Knowledge Engine
Verified provisions under the Information Technology Act, 2000 and the Bharatiya Nyaya Sanhita, 2023.
Sources: India Code (indiacode.nic.in), Ministry of Law and Justice, Government of India.
"""

from typing import Dict, Any, List

LEGAL_DISCLAIMER = (
    "DISCLAIMER: The information provided herein is for educational and civic awareness purposes only. "
    "It reflects provisions of the Information Technology Act, 2000 and the Bharatiya Nyaya Sanhita, 2023. "
    "It does not constitute formal legal advice or a judicial determination of criminal liability. "
    "Victims should lodge an official complaint at cybercrime.gov.in or consult an advocate."
)

CYBER_LAWS_DIRECTORY: List[Dict[str, Any]] = [
    {
        "id": "it-act-sec-43",
        "act": "Information Technology Act, 2000",
        "section": "Section 43",
        "title": "Penalty and Compensation for Damage to Computer, Computer System, etc.",
        "simpleExplanation": (
            "Imposes civil financial liability on anyone who accesses, downloads, copies, or contaminates "
            "a computer system, phone, or data without the owner's permission."
        ),
        "conductCovered": [
            "Unauthorized access to mobile phones, computers, or bank accounts",
            "Downloading or extracting confidential data without consent",
            "Introducing viruses, Trojans, spyware, or malicious APKs",
            "Disrupting services or denying access to authorized users"
        ],
        "penalty": "Liable to pay damages by way of compensation to the person affected (up to ₹1 Crore adjudicable).",
        "educationalExample": (
            "A predatory loan app tricks an individual into installing an APK file that secretly accesses and downloads "
            "their private contact list and photo gallery without explicit, informed consent."
        ),
        "relevantCategories": ["Predatory Loan App Blackmail", "Malicious APK Distribution", "Data Harvesting"],
        "officialSource": "https://www.indiacode.nic.in/handle/123456789/1999",
        "reportingOption": "File civil claim with State IT Adjudicating Officer / Report on cybercrime.gov.in"
    },
    {
        "id": "it-act-sec-66",
        "act": "Information Technology Act, 2000",
        "section": "Section 66",
        "title": "Computer Related Offences",
        "simpleExplanation": (
            "Criminalizes dishonest or fraudulent acts specified in Section 43, turning unauthorized "
            "computer access into a punishable criminal offense."
        ),
        "conductCovered": [
            "Dishonest hacking into emails, banking applications, or social accounts",
            "Deleting, altering, or diminishing the value of electronic records",
            "Transmitting malicious code designed to compromise personal finances"
        ],
        "penalty": "Imprisonment up to 3 years, or with fine up to ₹5,00,000, or with both.",
        "educationalExample": (
            "A fraudster gains unauthorized access to a victim's netbanking portal and alters security settings "
            "or transfers funds to an illicit mule account."
        ),
        "relevantCategories": ["Bank Account Hacking", "Unauthorized Funds Transfer", "Ransomware"],
        "officialSource": "https://www.indiacode.nic.in/handle/123456789/1999",
        "reportingOption": "National Cyber Crime Reporting Portal (cybercrime.gov.in) & Local Cyber Police Station"
    },
    {
        "id": "it-act-sec-66c",
        "act": "Information Technology Act, 2000",
        "section": "Section 66C",
        "title": "Punishment for Identity Theft",
        "simpleExplanation": (
            "Punishes anyone who fraudulently or dishonestly uses another person's password, OTP, "
            "digital signature, or biometric identification."
        ),
        "conductCovered": [
            "Tricking victims into revealing their OTP or banking passwords",
            "Using stolen debit card details, CVV, or UPI MPIN to make unauthorized transactions",
            "Using another person's Aadhaar or PAN number to open fraudulent accounts (SIM swap fraud)"
        ],
        "penalty": "Imprisonment of either description for a term which may extend to 3 years and fine up to ₹1,00,000.",
        "educationalExample": (
            "An SMS scammer poses as bank support, asks for the 6-digit OTP under the pretext of 'canceling a wrong charge', "
            "and immediately uses that OTP to siphon money from the victim's account."
        ),
        "relevantCategories": ["OTP Fraud", "UPI PIN Theft", "SIM Swap Scam", "Credential Harvesting"],
        "officialSource": "https://www.indiacode.nic.in/handle/123456789/1999",
        "reportingOption": "Call 1930 immediately to freeze funds & lodge incident at cybercrime.gov.in"
    },
    {
        "id": "it-act-sec-66d",
        "act": "Information Technology Act, 2000",
        "section": "Section 66D",
        "title": "Punishment for Cheating by Personation by Using Computer Resource",
        "simpleExplanation": (
            "Specifically criminalizes impersonating an individual, bank, government agency, or company "
            "over phone, SMS, WhatsApp, email, or a fraudulent website to cheat someone."
        ),
        "conductCovered": [
            "Creating phishing websites that look identical to SBI, HDFC, or Income Tax portals",
            "Posing as a bank official, police inspector, or customs officer on WhatsApp or video call",
            "Posing as an HR manager offering guaranteed work-from-home jobs to demand registration fees"
        ],
        "penalty": "Imprisonment of either description for a term which may extend to 3 years and fine up to ₹1,00,000.",
        "educationalExample": (
            "A scammer sends an SMS claiming to be 'VM-SBIINB' stating: 'Your bank account will be blocked today! "
            "Update KYC at http://sbi-fake-kyc.com'. The website imitates State Bank of India's login page."
        ),
        "relevantCategories": ["Bank Phishing", "Digital Arrest Impersonation", "Fake Job Recruiter", "Government Impersonation"],
        "officialSource": "https://www.indiacode.nic.in/handle/123456789/1999",
        "reportingOption": "Report to Sanchar Saathi Chakshu (sancharsaathi.gov.in) & cybercrime.gov.in"
    },
    {
        "id": "it-act-sec-66e",
        "act": "Information Technology Act, 2000",
        "section": "Section 66E",
        "title": "Punishment for Violation of Privacy",
        "simpleExplanation": (
            "Punishes the intentional capture, publishing, or transmitting of images of a person's private area "
            "without their consent, in violation of their right to privacy."
        ),
        "conductCovered": [
            "Video call sextortion and blackmails using captured video feeds",
            "Morphing photographs of victims and threatening to circulate them",
            "Illegal transmission of private intimate images without consent"
        ],
        "penalty": "Imprisonment up to 3 years, or with fine up to ₹2,00,000, or with both.",
        "educationalExample": (
            "A WhatsApp contact video calls a victim, records the call, splices inappropriate imagery, and threatens "
            "to send the video to all family contacts unless ₹50,000 is transferred via UPI."
        ),
        "relevantCategories": ["Sextortion / Morphing Blackmail", "Privacy Violation", "Predatory Loan Extortion"],
        "officialSource": "https://www.indiacode.nic.in/handle/123456789/1999",
        "reportingOption": "Report on cybercrime.gov.in under 'Women / Child Related Crime' or 'Other Cybercrime'"
    },
    {
        "id": "it-act-sec-70b",
        "act": "Information Technology Act, 2000",
        "section": "Section 70B",
        "title": "Indian Computer Emergency Response Team (CERT-In) Powers & Responsibilities",
        "simpleExplanation": (
            "Designates CERT-In as the national nodal agency for collecting cybersecurity incident reports, "
            "analyzing threats, and issuing binding security advisories."
        ),
        "conductCovered": [
            "Mandatory reporting of cybersecurity breaches and ransomware",
            "Emergency containment of mass phishing campaigns and malicious domains",
            "Coordination with domestic and international incident response teams"
        ],
        "penalty": "Failure to furnish information to CERT-In is punishable under subsection (7) with up to 1 year imprisonment or fine up to ₹1,00,000.",
        "educationalExample": (
            "A widespread SMS campaign distributes a banking Trojan targeting major Indian banks; CERT-In issues a national alert "
            "and works with telecom providers to block the C2 servers."
        ),
        "relevantCategories": ["National Cybersecurity Alerts", "Malware Incident Response", "System Vulnerabilities"],
        "officialSource": "https://www.indiacode.nic.in/handle/123456789/1999",
        "reportingOption": "Report incident to CERT-In Incident Reporting Portal (cert-in.org.in / incident@cert-in.org.in)"
    },
    {
        "id": "bns-sec-316",
        "act": "Bharatiya Nyaya Sanhita, 2023",
        "section": "Section 316",
        "title": "Criminal Breach of Trust",
        "simpleExplanation": (
            "Covers situations where someone entrusted with money, property, or digital access dishonestly "
            "misappropriates it for their own benefit or violates the terms of trust."
        ),
        "conductCovered": [
            "Platform administrators or financial intermediaries diverting customer funds",
            "Employees or agents siphoning customer deposit money into unauthorized accounts",
            "Investment managers running fraudulent Ponzi schemes without executing promised investments"
        ],
        "penalty": "Imprisonment of either description for a term which may extend to 5 years, or with fine, or with both (enhanced under specific subsections).",
        "educationalExample": (
            "A fake Telegram investment manager receives ₹1,00,000 from an investor with a promise to trade in stocks, "
            "but transfers the funds into private crypto wallets and cuts off communication."
        ),
        "relevantCategories": ["Investment Fraud", "Crypto Ponzi Schemes", "Financial Misappropriation"],
        "officialSource": "https://www.indiacode.nic.in/handle/123456789/2023",
        "reportingOption": "File complaint on RBI Sachet (sachet.rbi.org.in) and cybercrime.gov.in"
    },
    {
        "id": "bns-sec-318",
        "act": "Bharatiya Nyaya Sanhita, 2023",
        "section": "Section 318",
        "title": "Cheating and Dishonestly Inducing Delivery of Property",
        "simpleExplanation": (
            "Replaced Section 420 of the Indian Penal Code. Punishes deceiving any person to induce them "
            "to deliver money, property, or consent to make a financial transfer."
        ),
        "conductCovered": [
            "Advance fee lottery fraud ('Pay ₹499 to claim ₹25 Lakhs')",
            "Fake work-from-home task scams ('Pay ₹3,000 VIP deposit to unlock higher salary')",
            "Non-delivery of goods ordered from fraudulent social media shopping advertisements"
        ],
        "penalty": "Imprisonment of either description for a term which may extend to 7 years, and shall also be liable to fine (Section 318(4)).",
        "educationalExample": (
            "A victim receives a WhatsApp message claiming they won ₹25 Lakhs in the KBC Lucky Draw, "
            "and is coerced into depositing ₹12,500 in 'customs clearance and processing charges'."
        ),
        "relevantCategories": ["Lottery Scams", "Work-from-Home Advance Fee", "E-Commerce Fraud", "Advance-Fee Fraud"],
        "officialSource": "https://www.indiacode.nic.in/handle/123456789/2023",
        "reportingOption": "National Cyber Crime Reporting Portal (cybercrime.gov.in) & 1930 Helpline"
    },
    {
        "id": "bns-sec-336-338",
        "act": "Bharatiya Nyaya Sanhita, 2023",
        "section": "Section 336 & 338",
        "title": "Forgery and Using as Genuine a Forged Document or Electronic Record",
        "simpleExplanation": (
            "Punishes making or using false electronic documents, fake appointment letters, fake police summons, "
            "or forged government certificates as genuine."
        ),
        "conductCovered": [
            "Forging Ministry of Finance, CBI, or Cyber Police seals on digital arrest notices",
            "Creating fake job offer letters with forged corporate letterheads (Tata, Google, Infosys)",
            "Fabricating bank balance receipts or fake loan sanction letters"
        ],
        "penalty": "Imprisonment of either description for a term which may extend to 2 to 7 years, with fine.",
        "educationalExample": (
            "Extortionists send a PDF titled 'Supreme Court of India Warrant of Arrest' bearing a forged national emblem "
            "and forged signature of a Chief Justice, demanding immediate settlement via RTGS."
        ),
        "relevantCategories": ["Digital Arrest Extortion", "Fake Job Appointment Letters", "Forged Document Scams"],
        "officialSource": "https://www.indiacode.nic.in/handle/123456789/2023",
        "reportingOption": "Report to local Cyber Crime Police Station with preserved PDF and cybercrime.gov.in"
    },
    {
        "id": "bns-sec-351",
        "act": "Bharatiya Nyaya Sanhita, 2023",
        "section": "Section 351",
        "title": "Criminal Intimidation and Extortion",
        "simpleExplanation": (
            "Punishes threatening a person with injury to their person, reputation, or property to force "
            "them to do any act they are not legally bound to do (e.g. transfer money)."
        ),
        "conductCovered": [
            "Coercing victims over Skype/WhatsApp that they will be arrested immediately unless they transfer savings",
            "Harassing and threatening family members by unauthorized loan app recovery agents",
            "Threatening immediate power disconnection or disconnection of mobile number"
        ],
        "penalty": "Imprisonment of either description for a term which may extend to 2 years, or fine, or both (extended to 7 years if threat is of death or grievous hurt).",
        "educationalExample": (
            "A caller poses as a Telecom / Police Inspector and threatens: 'Your phone number has been linked to drug trafficking. "
            "If you disconnect this call, an arrest party will reach your house in 15 minutes.'"
        ),
        "relevantCategories": ["Digital Arrest Scams", "Loan Recovery Harassment", "Extortion Threats"],
        "officialSource": "https://www.indiacode.nic.in/handle/123456789/2023",
        "reportingOption": "Call 1930 immediately. Never pay extortion money. Report to cybercrime.gov.in"
    }
]

def get_relevant_laws_for_category(scam_category: str) -> List[Dict[str, Any]]:
    """Map detected scam categories to the most relevant Indian legal provisions."""
    cat_lower = (scam_category or "").lower()
    matches = []

    for law in CYBER_LAWS_DIRECTORY:
        # Check if any relevant category matches
        is_relevant = any(
            c.lower() in cat_lower or cat_lower in c.lower()
            for c in law["relevantCategories"]
        )
        # Category specific heuristics
        if "bank" in cat_lower or "phishing" in cat_lower or "otp" in cat_lower or "credential" in cat_lower:
            if law["section"] in ["Section 66C", "Section 66D"]:
                is_relevant = True
        elif "job" in cat_lower or "lottery" in cat_lower or "advance" in cat_lower:
            if law["section"] in ["Section 66D", "Section 318"]:
                is_relevant = True
        elif "arrest" in cat_lower or "threat" in cat_lower or "extortion" in cat_lower or "police" in cat_lower:
            if law["section"] in ["Section 66D", "Section 336 & 338", "Section 351"]:
                is_relevant = True
        elif "loan" in cat_lower:
            if law["section"] in ["Section 43", "Section 66E", "Section 318", "Section 351"]:
                is_relevant = True

        if is_relevant:
            matches.append(law)

    return matches if matches else CYBER_LAWS_DIRECTORY[:3]
