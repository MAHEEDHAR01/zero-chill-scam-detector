// ZERO CHILL 3.0 – Client-Side Offline Threat Detection Engine
// Provides instant client-side heuristic evaluation with multilingual Hindi/Telugu and UPI QR support.

(function() {
  const SUSPICIOUS_TLDS = new Set([
    'xyz', 'top', 'club', 'work', 'click', 'live', 'loan', 'cam', 'vip', 
    'monster', 'support', 'rest', 'icu', 'gq', 'cf', 'tk', 'ml', 'ga', 
    'buzz', 'surf', 'fit', 'racing', 'download', 'stream', 'accountant',
    'bid', 'cricket', 'party', 'trade', 'webcam', 'zip', 'mov'
  ]);

  const URL_SHORTENERS = new Set([
    'bit.ly', 'tinyurl.com', 't.co', 'is.gd', 'cutt.ly', 'rb.gy', 'ow.ly',
    'goo.gl', 's.id', 'shrtco.de', 'buff.ly', 'adf.ly', 'rebrand.ly', 'tiny.cc'
  ]);

  function detectLanguage(text) {
    const devanagari = (text.match(/[\u0900-\u097F]/g) || []).length;
    const telugu = (text.match(/[\u0C00-\u0C7F]/g) || []).length;
    const total = text.length || 1;

    if (devanagari / total > 0.15) return 'hi';
    if (telugu / total > 0.15) return 'te';
    if (devanagari > 0 || telugu > 0) return 'mixed';

    const lower = text.toLowerCase();
    const hinglish = ['aapka', 'turant', 'karein', 'jeeta', 'badhai', 'bijli', 'hoga'];
    const teluglish = ['mee', 'ventane', 'cheyandi', 'avthundi', 'kurchuni'];

    if (hinglish.some(w => lower.includes(w))) return 'mixed';
    if (teluglish.some(w => lower.includes(w))) return 'mixed';

    return 'en';
  }

  function parseUpi(text) {
    if (!text.toLowerCase().includes('upi://pay')) return null;
    try {
      const url = new URL(text.trim());
      const vpa = url.searchParams.get('pa') || '';
      const name = url.searchParams.get('pn') || '';
      const amount = url.searchParams.get('am') || 'Variable';
      return { vpa, name, amount, isUpi: true };
    } catch(e) {
      return null;
    }
  }

  function analyze(text) {
    if (!text || !text.trim()) {
      return {
        riskLevel: 'SAFE',
        riskScore: 0,
        color: 'green',
        scamType: 'Empty Input',
        confidenceScore: 0.99,
        uncertaintyRating: 'Low',
        language: 'en',
        indicators: [],
        highlightedPhrases: [],
        explanation: 'No message text provided for analysis.',
        recommendedSteps: ['Enter or paste text to evaluate.'],
        legalSections: [],
        govServices: [],
        detectedUrls: [],
        engine: 'ZERO CHILL 3.0 Client Engine'
      };
    }

    const raw = text.trim();
    const lower = raw.toLowerCase();
    const lang = detectLanguage(raw);
    let score = 0;
    const indicators = [];
    const highlights = [];
    const detectedTypes = [];

    // QR Check
    const upi = parseUpi(raw);
    if (upi) {
      score += 40;
      highlights.push(raw);
      indicators.push({
        name: 'UPI Pay Payload Detected',
        severity: 'CRITICAL',
        category: 'UPI Payment Trap',
        description: `QR Code payload executes UPI debit to ${upi.vpa}. Scanning this and entering your MPIN sends money to the scammer.`
      });
      detectedTypes.push('UPI Payment Trap');
    }

    // URLs
    const urlPattern = /(https?:\/\/[^\s<>"',;]+|www\.[^\s<>"',;]+|[a-zA-Z0-9-]+\.(?:com|org|net|in|xyz|top|live|click|club|loan|info|biz|me|online|site|app)[^\s<>"',;]*)/gi;
    const urls = raw.match(urlPattern) || [];

    urls.forEach(u => {
      highlights.push(u);
      let full = u.startsWith('http') ? u : 'http://' + u;
      try {
        let parsed = new URL(full);
        let domain = parsed.hostname.toLowerCase();
        let parts = domain.split('.');
        let tld = parts.length > 1 ? parts[parts.length - 1] : '';

        if (URL_SHORTENERS.has(domain)) {
          score += 35;
          indicators.push({
            name: `Shortened URL (${domain})`,
            severity: 'HIGH',
            category: 'Deceptive Link',
            description: 'URL shortener hides actual malicious landing address.'
          });
          detectedTypes.push('Phishing Shortened Link');
        }
        if (SUSPICIOUS_TLDS.has(tld)) {
          score += 40;
          indicators.push({
            name: `Untrusted TLD (.${tld})`,
            severity: 'HIGH',
            category: 'Untrusted Domain',
            description: `Uses high-risk .${tld} top level domain common in smishing.`
          });
          detectedTypes.push('Suspicious Domain Phishing');
        }
        if (/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/.test(domain)) {
          score += 50;
          indicators.push({
            name: 'Direct Server IP Host',
            severity: 'CRITICAL',
            category: 'Phishing Infrastructure',
            description: `Points directly to raw server IP ${domain}.`
          });
          detectedTypes.push('Direct IP Phishing');
        }
      } catch(e) {}
    });

    // Threat Patterns
    const rules = [
      { regex: /\b(otp|one time password|atm pin|upi pin|cvv|netbanking password)\b/i, name: 'Credential / OTP Request', weight: 45, sev: 'CRITICAL', type: 'Credential Theft' },
      { regex: /(ओटीपी|पासवर्ड|पिन|ఓటీపీ|పిన్)/i, name: 'Multilingual OTP / PIN Request', weight: 45, sev: 'CRITICAL', type: 'Credential Theft' },
      { regex: /\b(account.*(block|suspend|deactivat|clos)|blocked today|power.*disconnect|arrest warrant|digital arrest)\b/i, name: 'Panic & Urgent Coercion', weight: 35, sev: 'HIGH', type: 'Panic Coercion' },
      { regex: /(खाता ब्लॉक|बिजली कट|गिरफ्तारी वारंट|ఖాతా బ్లాక్|కరెంట్ కట్)/i, name: 'Multilingual Panic Coercion', weight: 40, sev: 'HIGH', type: 'Panic Coercion' },
      { regex: /\b(work from home|part[- ]time job|earn.*daily|like youtube videos|telegram task)\b/i, name: 'Task Scam / Job Bait', weight: 35, sev: 'HIGH', type: 'Job Scam' },
      { regex: /(घर बैठे कमाए|यूट्यूब लाइक|ఇంటి నుండి పని|రోజువారీ సంపాదన)/i, name: 'Multilingual Job Scam Bait', weight: 35, sev: 'HIGH', type: 'Job Scam' },
      { regex: /\b(won|winner|winning|kbc lucky draw|lottery)\b/i, name: 'Lottery / Prize Claim', weight: 35, sev: 'HIGH', type: 'Lottery Fraud' },
      { regex: /(बधाई हो|इनाम जीता|లక్కీ డ్రా|బహుమతి)/i, name: 'Multilingual Prize Hook', weight: 35, sev: 'HIGH', type: 'Lottery Fraud' },
      { regex: /\b(pay\s*(rs\.?|inr|₹)\s*\d+.*(registration|processing|customs|vip))\b/i, name: 'Advance Fee Demand', weight: 45, sev: 'CRITICAL', type: 'Advance-Fee Fraud' },
      { regex: /(रजिस्ट्रेशन फीस|कस्टम ड्यूटी|రిజిస్ట్రేషన్ ఫీజు)/i, name: 'Multilingual Upfront Fee Request', weight: 45, sev: 'CRITICAL', type: 'Advance-Fee Fraud' },
      { regex: /\b(instant loan.*approved|loan without cibil|zero interest loan)\b/i, name: 'Predatory Instant Loan', weight: 35, sev: 'HIGH', type: 'Loan Fraud' }
    ];

    rules.forEach(r => {
      const m = raw.match(r.regex);
      if (m) {
        highlights.push(m[0]);
        score += r.weight;
        indicators.push({
          name: r.name,
          severity: r.sev,
          category: r.type,
          description: `Detected warning indicator: '${m[0]}'.`
        });
        if (!detectedTypes.includes(r.type)) detectedTypes.push(r.type);
      }
    });

    // Mitigating safe signals
    if (urls.length === 0 && !indicators.some(i => i.severity === 'CRITICAL')) {
      if (/\b(successfully received|payment received|credited to your a\/c|debited from a\/c)\b/i.test(raw)) {
        score -= 20;
      }
    }

    const finalScore = Math.max(0, Math.min(100, Math.round(score)));
    let riskLevel = 'SAFE';
    let color = 'green';
    let scamType = detectedTypes[0] || 'Legitimate Notification Pattern';
    let explanation = '';
    let recommendations = [];

    if (finalScore >= 60) {
      riskLevel = 'HIGH-RISK SCAM';
      color = 'red';
      explanation = `This message shows high-probability indicators of ${scamType}. It uses psychological panic, credential harvesting, or unverified links to commit fraud.`;
      recommendations = [
        "DO NOT click any link or dial any number provided.",
        "NEVER share OTP, UPI PIN, or passwords.",
        "If money was debited, call National Cybercrime Helpline 1930 immediately (Golden Window).",
        "Report to cybercrime.gov.in and Sanchar Saathi Chakshu."
      ];
    } else if (finalScore >= 25) {
      riskLevel = 'SUSPICIOUS';
      color = 'amber';
      explanation = "One or more warning signs detected. Unsolicited job offers, predatory loans, or unverified links require caution.";
      recommendations = [
        "Do not click links or call unsolicited numbers.",
        "Verify offers independently on official websites.",
        "Never pay advance fees to claim jobs or prizes."
      ];
    } else {
      riskLevel = 'SAFE';
      color = 'green';
      explanation = "No significant scam indicators, malicious URLs, or credential-harvesting patterns found. Resembles standard informational notice.";
      recommendations = [
        "Important: Automated scanning cannot guarantee 100% authenticity.",
        "Never share OTPs or passwords under any circumstances.",
        "Always verify unexpected payment requests with your bank."
      ];
    }

    return {
      riskLevel,
      riskScore: finalScore,
      color,
      scamType,
      confidenceScore: finalScore >= 60 ? 0.95 : 0.88,
      uncertaintyRating: finalScore >= 25 && finalScore < 60 ? 'Moderate' : 'Low',
      language: lang,
      indicators,
      highlightedPhrases: [...new Set(highlights)],
      explanation,
      recommendedSteps: recommendations,
      legalSections: [],
      govServices: [],
      detectedUrls: urls.map(u => ({ original: u, domain: u, riskScore: finalScore })),
      engine: 'ZERO CHILL 3.0 Client Threat Engine'
    };
  }

  window.ScamShieldLocalAnalyzer = { analyze };
  window.ZeroChillLocalAnalyzer = { analyze };
})();
