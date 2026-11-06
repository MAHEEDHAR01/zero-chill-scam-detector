// ZERO CHILL 3.0 – Hackathon Demonstration Benchmarks & Cyber Safety Data

window.BENCHMARK_SAMPLES = [
  {
    id: "sample-safe",
    category: "SAFE",
    label: "SAFE: Electricity Bill Payment",
    language: "en",
    text: "Your electricity bill payment of Rs. 850 was successfully received. Thank you.",
    description: "Standard payment receipt notification without malicious links or urgent demands.",
    source: "BESCOM Official SMS"
  },
  {
    id: "sample-suspicious",
    category: "SUSPICIOUS",
    label: "SUSPICIOUS: Work-From-Home Job",
    language: "en",
    text: "Congratulations! You have been selected for a work-from-home job. Contact us immediately for more details.",
    description: "Unsolicited job offer with artificial urgency and lack of verified employer details.",
    source: "Unverified SMS"
  },
  {
    id: "sample-high-risk",
    category: "HIGH-RISK SCAM",
    label: "HIGH-RISK: Bank Phishing + OTP Trap",
    language: "en",
    text: "Your bank account will be blocked today! Verify your account immediately by clicking http://fake-bank-example.com and entering your OTP.",
    description: "Severe phishing attempt: Panic-inducing threat, unverified HTTP link, and explicit OTP credential harvesting.",
    source: "Spoofed Bank Phishing SMS"
  },
  {
    id: "sample-hindi-threat",
    category: "HIGH-RISK SCAM",
    label: "HIGH-RISK: Hindi Bank KYC Expiry",
    language: "hi",
    text: "प्रिय ग्राहक, आपका एसबीआई बैंक खाता आज रात बंद हो जाएगा! तुरंत http://sbi-kyc-update.xyz पर जाकर पैन कार्ड और ओटीपी दर्ज करें।",
    description: "Hindi Devanagari smishing targeting SBI account holders with fake KYC urgency and .xyz phishing link.",
    source: "Hindi SMS Phishing"
  },
  {
    id: "sample-telugu-lottery",
    category: "HIGH-RISK SCAM",
    label: "HIGH-RISK: Telugu KBC Prize Scam",
    language: "te",
    text: "మీ మొబైల్ నంబర్ KBC లక్కీ డ్రాలో 25 లక్షల రూపాయలు గెలుచుకుంది! నగదును క్లెయిమ్ చేయడానికి వెంటనే 499 రూపాయల రిజిస్ట్రేషన్ ఫీజు చెల్లించండి.",
    description: "Telugu language advance-fee lottery scam demanding ₹499 upfront registration fee to claim fake ₹25 Lakhs.",
    source: "Telugu WhatsApp Scam"
  },
  {
    id: "sample-digital-arrest",
    category: "HIGH-RISK SCAM",
    label: "HIGH-RISK: FedEx / CBI Digital Arrest",
    language: "en",
    text: "FedEx Security Alert: Your parcel containing fake passports has been detained at Mumbai Customs. CBI FIR registered. To avoid police arrest, join immediate Skype call with Cyber Crime Cell.",
    description: "Digital arrest extortion scam exploiting fear of law enforcement to coerce victims into video calls.",
    source: "Digital Arrest Threat"
  },
  {
    id: "sample-qr-upi",
    category: "HIGH-RISK SCAM",
    label: "HIGH-RISK: UPI QR Code 'Receive Money' Trap",
    language: "en",
    text: "upi://pay?pa=scammer99@okhdfcbank&pn=State%20Bank%20of%20India&am=5000&cu=INR",
    description: "Fake merchant QR payload: Claims to credit money, but scanning and entering MPIN debits ₹5,000 from the victim.",
    source: "Malicious UPI QR Payload"
  }
];

window.SAFETY_RULES = [
  {
    icon: "ShieldAlert",
    title: "Never Share OTPs, PINs or Passwords",
    desc: "No bank, electricity board, police officer, or government agency will ever ask for your OTP, UPI MPIN, or password over call or text."
  },
  {
    icon: "Clock",
    title: "Report Within the 2-Hour Golden Window",
    desc: "If defrauded in India, call National Cybercrime Helpline 1930 immediately. Acting within 2 hours enables nodal officers to freeze fraudulent transfers."
  },
  {
    icon: "Link2Off",
    title: "Inspect URLs & Never Trust Shorteners",
    desc: "Beware of shortened links (bit.ly, tinyurl) and unusual domains (.xyz, .top, .live). Official portals end in .gov.in, .nic.in, or verified banking domains."
  },
  {
    icon: "Ban",
    title: "Never Pay Upfront Fees for Jobs or Prizes",
    desc: "If you have to pay a 'processing fee', 'courier charge', or 'VIP task deposit' to receive money or employment, it is 100% a scam."
  },
  {
    icon: "DownloadCloud",
    title: "Never Install Unverified APKs or Remote Apps",
    desc: "Never install APK files sent via WhatsApp or install remote screen sharing software like AnyDesk or RustDesk on stranger requests."
  },
  {
    icon: "AlertOctagon",
    title: "'Digital Arrest' Does Not Exist in Law",
    desc: "Indian Police, CBI, ED, and Customs never conduct video call court trials or demand funds to be transferred to 'safe verification accounts'."
  }
];
