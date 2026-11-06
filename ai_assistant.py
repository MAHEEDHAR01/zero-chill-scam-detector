"""
ZERO CHILL 3.0 – Conversational AI Cyber Safety & Legal Rights Assistant
Powered by Google Gemini 2.5 Flash with intelligent offline knowledge engine fallback.
Multilingual assistance in English, Hindi (हिन्दी), and Telugu (తెలుగు).
"""

import os
import json
import requests
from typing import Dict, Any, List, Optional
from cyber_laws import CYBER_LAWS_DIRECTORY
from gov_services import GOV_SERVICES_DIRECTORY

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

ASSISTANT_SYSTEM_PROMPT = """You are ZERO CHILL AI, an expert, empathetic Indian Cyber Safety, Citizen Defense, and Cyber Law Assistant.
Your mission is to help ordinary citizens identify scams, understand their statutory rights under the Information Technology Act, 2000 and the Bharatiya Nyaya Sanhita, 2023, and take immediate official steps if defrauded.

KEY KNOWLEDGE:
1. Financial Emergency: National Cyber Crime Helpline 1930 operates 24x7. Emphasize the 'Golden Window' (reporting within 2 hours of money transfer to freeze funds).
2. Official Reporting: National Cyber Crime Reporting Portal (cybercrime.gov.in).
3. Telecom/SMS Scams: Sanchar Saathi Chakshu (sancharsaathi.gov.in/sfc/) for reporting fraudulent numbers/SMS even if no money lost.
4. Loan Scams: RBI Sachet (sachet.rbi.org.in).
5. Indian Cyber Laws:
   - IT Act Sec 43: Damage to computer/phone & unauthorized access (civil compensation).
   - IT Act Sec 66: Criminal computer related offences (up to 3 years imprisonment).
   - IT Act Sec 66C: Identity theft & OTP/password/PIN theft (up to 3 years imprisonment).
   - IT Act Sec 66D: Cheating by personation (phishing, posing as bank/police/recruiter).
   - IT Act Sec 66E: Privacy violation & sextortion.
   - BNS Sec 318: Cheating and dishonestly inducing delivery of property (lottery/job fees).
   - BNS Sec 351: Criminal intimidation & extortion (Digital arrest threats).

COMMUNICATION STYLE:
- Empathetic, clear, and reassuring.
- Use simple everyday language without excessive technical or legal jargon.
- If the user asks in Hindi, reply in clear, natural Hindi.
- If the user asks in Telugu, reply in Telugu.
- If the user asks in English, reply in English.
- Always include actionable next steps.
- Always clarify that you provide general educational cyber safety and legal information, not formal legal representation.
"""

def get_offline_assistant_response(message: str) -> str:
    """Intelligent offline knowledge agent for when Gemini API key is absent."""
    msg = message.lower()

    # Hindi queries
    if any(k in msg for k in ['1930', 'हेल्पलाइन', 'पैसे कट गए', 'धोखा', 'शिकायत', 'पुलिस', 'खाता']):
        return (
            "🛡️ **ZERO CHILL सुरक्षा सहायता (हिन्दी):**\n\n"
            "1. **तुरंत 1930 पर कॉल करें:** यदि आपके बैंक खाते से पैसे कट गए हैं, तो तुरंत **1930 (राष्ट्रीय साइबर वित्तीय धोखाधड़ी हेल्पलाइन)** पर कॉल करें। पहले 2 घंटे 'गोल्डन विंडो' होते हैं, जिसमें बैंक पैसे को ब्लॉक कर सकते हैं।\n"
            "2. **अपना कार्ड और UPI ब्लॉक करें:** अपने बैंक के ऐप या कस्टमर केयर से तुरंत डेबिट कार्ड और नेटबैंकिंग को फ्रीज करें।\n"
            "3. **आधिकारिक शिकायत दर्ज करें:** **cybercrime.gov.in** पर जाकर 'Report Financial Fraud' में शिकायत दर्ज करें और एक्नॉलेजमेंट नंबर सुरक्षित रखें।\n"
            "4. **कानूनी धाराएं:** यह अपराध **IT Act की धारा 66D (प्रतिरूपण द्वारा धोखाधड़ी)** और **BNS की धारा 318 (धोखाधड़ी)** के तहत दंडनीय है जिसमें 3 से 7 साल तक की जेल हो सकती है।"
        )

    # Telugu queries
    if any(k in msg for k in ['డబ్బులు', 'మోసం', 'హెల్ప్‌లైన్', 'పోలీస్', 'ఫిర్యాదు']):
        return (
            "🛡️ **ZERO CHILL భద్రతా సహాయం (తెలుగు):**\n\n"
            "1. **వెంటనే 1930 కి కాల్ చేయండి:** మీ బ్యాంక్ ఖాతా నుండి అనధికారికంగా డబ్బు కట్ అయితే, వెంటనే **1930 (నేషనల్ సైబర్ క్రైమ్ హెల్ప్‌లైన్)** కి కాల్ చేయండి. మొదటి 2 గంటల వ్యవధిలో బ్యాంకులు ఆ లావాదేవీని నిలిపివేయగలవు.\n"
            "2. **కార్డు మరియు UPI బ్లాక్ చేయండి:** మీ బ్యాంక్ మొబైల్ యాప్ ద్వారా డెబిట్ కార్డు మరియు యూపీఐని వెంటనే బ్లాక్ చేయండి.\n"
            "3. **పోర్టల్‌లో ఫిర్యాదు చేయండి:** **cybercrime.gov.in** లో అధికారిక ఫిర్యాదు నమోదు చేయండి.\n"
            "4. **చట్టపరమైన సమాచారం:** ఐటీ చట్టం సెక్షన్ 66D మరియు BNS సెక్షన్ 318 ప్రకారం సైబర్ మోసగాళ్లకు 3 నుండి 7 సంవత్సరాల జైలు శిక్ష విధించబడుతుంది."
        )

    # 1930 or Emergency
    if any(k in msg for k in ['1930', 'lost money', 'debit', 'unauthorized', 'stolen money', 'emergency', 'golden window', 'golden hour']):
        return (
            "🚨 **CRITICAL FINANCIAL FRAUD RESPONSE (Within 2 Hours):**\n\n"
            "1. **Dial 1930 Immediately:** The National Cyber Crime Financial Fraud Helpline operates 24x7. Police operators trigger real-time holds across 250+ connected banks to freeze the fraudster's mule account before cash withdrawal.\n"
            "2. **Gather Required Details:** Keep your Bank Name, Account Number, Transaction Amount, and **Transaction UTR Number** (from your bank's debit SMS) ready before calling.\n"
            "3. **Freeze Cards & UPI:** Open your official banking app or call your bank's 24/7 helpline to block your debit card and suspend internet banking access.\n"
            "4. **Lodge Formal Complaint:** Complete the formal online incident filing at **[cybercrime.gov.in](https://cybercrime.gov.in)** within 24 hours using the ticket reference received via SMS.\n\n"
            "*Legal Note: Unauthorized electronic fund siphoning violates IT Act Section 66C/66D and BNS Section 318 (up to 7 years imprisonment).* "
        )

    # Digital Arrest
    if any(k in msg for k in ['digital arrest', 'arrest warrant', 'cbi', 'customs', 'police call', 'skype', 'video call']):
        return (
            "⚠️ **WARNING: 'DIGITAL ARREST' IS A 100% FRAUDULENT EXTORTION SCAM:**\n\n"
            "• **The Reality:** Indian Police, CBI, ED, Narcotics Control Bureau (NCB), and Telecom Department NEVER conduct 'Digital Arrests', judicial hearings, or investigations over Skype or WhatsApp video calls.\n"
            "• **No Government Escrow Accounts:** Scammers demand money to be transferred to 'safe verification RBI accounts' or 'Supreme Court escrow'. There are NO such accounts in existence.\n"
            "• **Action Steps:**\n"
            "  1. Hang up the call immediately. Do not be intimidated by forged police uniforms or fake background seals.\n"
            "  2. Do not transfer a single rupee.\n"
            "  3. Report the phone number to **Sanchar Saathi Chakshu** ([sancharsaathi.gov.in/sfc/](https://sancharsaathi.gov.in/sfc/)) and **cybercrime.gov.in**.\n"
            "  4. This conduct constitutes Criminal Intimidation under **BNS Section 351** and Cheating by Personation under **IT Act Section 66D**."
        )

    # IT Act & Cyber Laws
    if any(k in msg for k in ['it act', 'law', 'section', '66d', '66c', 'bns', 'legal rights', 'punishment', 'police case']):
        return (
            "⚖️ **INDIAN CYBER LAW PROVISIONS & YOUR RIGHTS:**\n\n"
            "• **IT Act Section 66D (Cheating by Personation):** Punishes anyone who cheats by impersonating a bank, government officer, police, or company using any phone or computer. **Penalty: Up to 3 years imprisonment + ₹1 Lakh fine.**\n"
            "• **IT Act Section 66C (Identity Theft):** Punishes fraudulent use of another person's password, OTP, ATM PIN, or electronic identity. **Penalty: Up to 3 years imprisonment + fine.**\n"
            "• **BNS Section 318 (Cheating):** Punishes deceiving victims into delivering money or paying advance fees. **Penalty: Up to 7 years imprisonment + fine.**\n"
            "• **BNS Section 351 (Criminal Intimidation):** Punishes threatening arrest or property damage. **Penalty: Up to 2 to 7 years imprisonment.**\n\n"
            "Citizens have the statutory right to zero-liability reimbursement if unauthorized transactions are reported to their bank within 3 working days (RBI Circular 2017)."
        )

    # Job / Task Scams
    if any(k in msg for k in ['job', 'work from home', 'youtube', 'telegram task', 'part time']):
        return (
            "💼 **PART-TIME JOB & YOUTUBE LIKE SCAM WARNING:**\n\n"
            "• **How the Trap Works:** Fraudsters recruit via WhatsApp/Telegram offering ₹3,500/day for liking YouTube videos or rating hotels. They pay ₹150–₹500 initially to gain trust, then require you to deposit thousands into 'Prepaid VIP Tasks' which cannot be withdrawn.\n"
            "• **Golden Rule:** Legitimate companies NEVER ask job seekers to pay registration fees, security deposits, or task investments.\n"
            "• **What To Do:** Never pay advance fees. Export your chat history and report the recruiter handles at **cybercrime.gov.in** and **sancharsaathi.gov.in/sfc/**."
        )

    # General Fallback
    return (
        "🛡️ **ZERO CHILL AI Assistant:**\n\n"
        "I am ready to help you identify scam patterns, preserve digital evidence, understand Indian Cyber Laws (IT Act 2000, BNS 2023), and access verified official government services.\n\n"
        "**Quick Assistance Options:**\n"
        "• If money was lost, call **1930** immediately to freeze bank transfers (Golden Window).\n"
        "• Report suspicious phone numbers and SMS to **Sanchar Saathi Chakshu** (sancharsaathi.gov.in/sfc/).\n"
        "• File formal cybercrime complaints at **cybercrime.gov.in**.\n"
        "• Ask me anything about specific scams (Bank Phishing, Digital Arrest, Job Tasks, Loan Apps) or Indian Cyber Laws!"
    )

def chat_with_assistant(message: str, api_key: Optional[str] = None, history: Optional[List[Dict[str, str]]] = None) -> Dict[str, Any]:
    """
    Handle conversational chat using Gemini API if key available,
    falling back to structured local cybersecurity knowledge engine.
    """
    key = api_key or os.environ.get("GEMINI_API_KEY", "").strip()

    if not key:
        reply = get_offline_assistant_response(message)
        return {
            "reply": reply,
            "engine": "ZERO CHILL Offline Knowledge Engine (Verified)",
            "sources": ["MHA I4C", "IT Act 2000", "BNS 2023", "RBI Kehta Hai"]
        }

    try:
        # Build contents from history
        contents = []
        contents.append({
            "parts": [{"text": ASSISTANT_SYSTEM_PROMPT}]
        })

        if history:
            for item in history[-6:]: # last 6 messages
                role = "user" if item.get("role") == "user" else "model"
                contents.append({
                    "role": role,
                    "parts": [{"text": item.get("content", "")}]
                })

        contents.append({
            "role": "user",
            "parts": [{"text": message}]
        })

        payload = {
            "contents": contents,
            "generationConfig": {
                "temperature": 0.4,
                "maxOutputTokens": 800
            }
        }

        response = requests.post(
            f"{GEMINI_API_URL}?key={key}",
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=8
        )

        if response.status_code == 200:
            data = response.json()
            candidates = data.get("candidates", [])
            if candidates:
                reply_text = candidates[0].get("content", {}).get("parts", [{}])[0].get("text", "")
                return {
                    "reply": reply_text.strip(),
                    "engine": "Google Gemini 2.5 Flash (AI Cyber Safety Assistant)",
                    "sources": ["Gemini 2.5 Flash", "Indian Cyber Crime Framework", "IT Act 2000"]
                }

        # If non-200 or no candidates, fallback
        reply = get_offline_assistant_response(message)
        return {
            "reply": reply,
            "engine": f"ZERO CHILL Offline Knowledge Engine (Gemini status {response.status_code})",
            "sources": ["MHA I4C", "IT Act 2000", "BNS 2023"]
        }

    except Exception as e:
        print(f"[AI Assistant Warning]: {e}")
        reply = get_offline_assistant_response(message)
        return {
            "reply": reply,
            "engine": "ZERO CHILL Offline Knowledge Engine (Fallback)",
            "sources": ["MHA I4C", "IT Act 2000", "BNS 2023"]
        }
