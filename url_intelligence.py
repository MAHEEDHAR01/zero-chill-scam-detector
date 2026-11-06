"""
ZERO CHILL 3.0 – Advanced URL & Threat Intelligence Engine
Multi-layered domain reputation, brand typosquatting, TLD danger profiling,
Google Safe Browsing & VirusTotal API integrations with transparent heuristic fallback.
"""

import os
import re
import base64
import requests
from urllib.parse import urlparse
from typing import Dict, Any, List, Optional

# Abused low-reputation top-level domains frequently weaponized in smishing/phishing
SUSPICIOUS_TLDS = {
    'xyz', 'top', 'club', 'work', 'click', 'live', 'loan', 'cam', 'vip', 
    'monster', 'support', 'rest', 'icu', 'gq', 'cf', 'tk', 'ml', 'ga', 
    'buzz', 'surf', 'fit', 'racing', 'download', 'stream', 'accountant',
    'bid', 'cricket', 'party', 'trade', 'webcam', 'zip', 'mov', 'bond'
}

# Known URL shortener services
URL_SHORTENERS = {
    'bit.ly', 'tinyurl.com', 't.co', 'is.gd', 'cutt.ly', 'rb.gy', 'ow.ly',
    'goo.gl', 's.id', 'shrtco.de', 'buff.ly', 'adf.ly', 'rebrand.ly', 'tiny.cc'
}

# Major targeted Indian and global financial/gov brands for typosquatting detection
TARGET_BRANDS = [
    ('State Bank of India (SBI)', ['sbi', 'onlinesbi', 'yono', 'sbiinb']),
    ('HDFC Bank', ['hdfc', 'hdfcbank', 'netbanking.hdfc']),
    ('ICICI Bank', ['icici', 'icicibank', 'imobile']),
    ('Axis Bank', ['axis', 'axisbank']),
    ('Punjab National Bank (PNB)', ['pnb', 'punjabnational']),
    ('Bank of Baroda', ['bob', 'bankofbaroda', 'bobworld']),
    ('Paytm', ['paytm', 'paytmbank']),
    ('PhonePe', ['phonepe']),
    ('Google Pay / GPay', ['gpay', 'googlepay']),
    ('Income Tax Department', ['incometax', 'incometaxindia', 'efiling']),
    ('UIDAI / Aadhaar', ['uidai', 'myaadhaar', 'aadhaar']),
    ('India Post', ['indiapost', 'indiapostgov']),
    ('Amazon India', ['amazon', 'amazonpay']),
    ('Flipkart', ['flipkart'])
]

# Legitimate official domain roots
LEGITIMATE_DOMAINS = {
    'onlinesbi.sbi', 'sbi.co.in', 'hdfcbank.com', 'icicibank.com', 
    'axisbank.com', 'pnbindia.in', 'bankofbaroda.in', 'paytm.com', 
    'phonepe.com', 'pay.google.com', 'incometax.gov.in', 'uidai.gov.in', 
    'indiapost.gov.in', 'amazon.in', 'flipkart.com', 'cybercrime.gov.in',
    'sancharsaathi.gov.in', 'rbi.org.in', 'trai.gov.in', 'cert-in.org.in'
}


def audit_url_deep(raw_url: str, custom_api_keys: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """
    Perform multi-vector inspection of a web address.
    Checks live external APIs (Safe Browsing / VirusTotal) if configured,
    and runs comprehensive offline domain heuristics.
    """
    keys = custom_api_keys or {}
    safe_browsing_key = keys.get('safe_browsing') or os.environ.get('GOOGLE_SAFE_BROWSING_KEY', '').strip()
    virustotal_key = keys.get('virustotal') or os.environ.get('VIRUSTOTAL_KEY', '').strip()

    clean_url = raw_url.strip()
    if not clean_url.startswith(('http://', 'https://')):
        clean_url = 'http://' + clean_url

    parsed = urlparse(clean_url)
    domain = (parsed.netloc or parsed.path.split('/')[0]).lower().split(':')[0]
    protocol = parsed.scheme.lower()
    path = parsed.path

    warnings = []
    risk_score = 0
    threat_sources = []

    # 1. Protocol Inspection (HTTPS is NOT proof of safety!)
    is_https = (protocol == 'https')
    if not is_https:
        risk_score += 25
        warnings.append({
            'severity': 'HIGH',
            'type': 'Insecure Protocol (HTTP)',
            'message': 'Uses unencrypted HTTP connection. Legitimate banking and authentication portals mandate HTTPS.'
        })
    else:
        warnings.append({
            'severity': 'INFO',
            'type': 'HTTPS Protocol Present',
            'message': 'SSL/TLS encryption detected. Note: 80%+ of modern phishing sites also obtain free HTTPS certificates; HTTPS alone does not guarantee legitimacy.'
        })

    # 2. Check for IP address host
    is_ip = bool(re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', domain))
    if is_ip:
        risk_score += 50
        warnings.append({
            'severity': 'CRITICAL',
            'type': 'Direct IP Address Host',
            'message': f'Points directly to server IP {domain} rather than a registered enterprise domain name.'
        })

    # 3. Check URL Shorteners
    is_shortener = domain in URL_SHORTENERS
    if is_shortener:
        risk_score += 35
        warnings.append({
            'severity': 'HIGH',
            'type': 'URL Shortener Cloaking',
            'message': f"Domain '{domain}' is a shortener used to conceal the actual landing URL from users and security filters."
        })

    # 4. TLD Threat Assessment
    parts = domain.split('.')
    tld = parts[-1] if len(parts) > 1 else ''
    is_suspicious_tld = tld in SUSPICIOUS_TLDS
    if is_suspicious_tld:
        risk_score += 40
        warnings.append({
            'severity': 'HIGH',
            'type': f'High-Risk TLD (.{tld})',
            'message': f"Top-level domain .{tld} has a statistically high correlation with cybercrime campaigns due to cheap or anonymous registration."
        })

    # 5. Lookalike / Typosquatting / Brand Spoofing Check
    is_legitimate_exact = any(domain == legit or domain.endswith('.' + legit) for legit in LEGITIMATE_DOMAINS)
    detected_spoofed_brand = None

    if not is_legitimate_exact:
        for brand_name, brand_keywords in TARGET_BRANDS:
            for kw in brand_keywords:
                if kw in domain:
                    detected_spoofed_brand = brand_name
                    risk_score += 45
                    warnings.append({
                        'severity': 'CRITICAL',
                        'type': f'Brand Typosquatting ({brand_name})',
                        'message': f"Domain '{domain}' includes brand keyword '{kw}' but is NOT hosted on the official {brand_name} verified domain."
                    })
                    break
            if detected_spoofed_brand:
                break

    # 6. Check for excessive subdomains or hyphens
    subdomains_count = len(parts) - 2 if len(parts) > 2 else 0
    if subdomains_count >= 2:
        risk_score += 20
        warnings.append({
            'severity': 'MEDIUM',
            'type': 'Excessive Subdomain Stacking',
            'message': f"Domain uses {subdomains_count} subdomains, a pattern common in phishing redirects (e.g. login.sbi.com.threat.xyz)."
        })

    if domain.count('-') >= 2:
        risk_score += 20
        warnings.append({
            'severity': 'MEDIUM',
            'type': 'Multi-Hyphen Domain Spoofing',
            'message': f"Domain contains {domain.count('-')} hyphens mimicking complex official service names."
        })

    # 7. Check for @ symbol obfuscation
    if '@' in clean_url:
        risk_score += 50
        warnings.append({
            'severity': 'CRITICAL',
            'type': '@ Symbol URL Obfuscation',
            'message': "Contains '@' symbol, tricking browsers into ignoring the preceding domain and navigating to the host after '@'."
        })

    # 8. Check Google Safe Browsing API (if key available)
    safe_browsing_checked = False
    if safe_browsing_key:
        try:
            sb_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={safe_browsing_key}"
            payload = {
                "client": {"clientId": "zero-chill-ai", "clientVersion": "3.0.0"},
                "threatInfo": {
                    "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
                    "platformTypes": ["ANY_PLATFORM"],
                    "threatEntryTypes": ["URL"],
                    "threatEntries": [{"url": clean_url}]
                }
            }
            res = requests.post(sb_url, json=payload, timeout=4)
            if res.status_code == 200:
                data = res.json()
                matches = data.get('matches', [])
                safe_browsing_checked = True
                if matches:
                    risk_score = 100
                    threat_sources.append('Google Safe Browsing (MALICIOUS)')
                    warnings.append({
                        'severity': 'CRITICAL',
                        'type': 'Google Safe Browsing Flag',
                        'message': f"Flagged by Google Safe Browsing as {matches[0].get('threatType', 'SOCIAL_ENGINEERING')}."
                    })
                else:
                    threat_sources.append('Google Safe Browsing (Clean in global database)')
        except Exception as e:
            print(f"[Safe Browsing Warning]: {e}")

    # 9. Check VirusTotal API (if key available)
    virustotal_checked = False
    if virustotal_key:
        try:
            url_id = base64.urlsafe_b64encode(clean_url.encode()).decode().strip("=")
            vt_url = f"https://www.virustotal.com/api/v3/urls/{url_id}"
            headers = {"x-apikey": virustotal_key}
            res = requests.get(vt_url, headers=headers, timeout=4)
            if res.status_code == 200:
                vt_data = res.json()
                stats = vt_data.get('data', {}).get('attributes', {}).get('last_analysis_stats', {})
                malicious_count = stats.get('malicious', 0)
                virustotal_checked = True
                if malicious_count > 0:
                    risk_score = max(risk_score, min(100, 50 + malicious_count * 10))
                    threat_sources.append(f'VirusTotal ({malicious_count} security vendors flagged as malicious)')
                    warnings.append({
                        'severity': 'CRITICAL',
                        'type': 'VirusTotal Multi-Vendor Flag',
                        'message': f"{malicious_count} antivirus engines detected this URL as malicious or phishing."
                    })
                else:
                    threat_sources.append('VirusTotal (0 vendors flagged)')
        except Exception as e:
            print(f"[VirusTotal Warning]: {e}")

    # Clamp Score
    final_score = max(0, min(100, risk_score))

    if is_legitimate_exact and not (safe_browsing_checked and risk_score >= 80):
        final_score = 0
        risk_level = 'SAFE'
        color = 'green'
        summary = f"Domain '{domain}' matches verified legitimate enterprise infrastructure. No phishing flags detected."
    elif final_score >= 60:
        risk_level = 'HIGH-RISK SCAM'
        color = 'red'
        summary = f"Domain '{domain}' displays critical indicators of deceptive phishing, malicious hosting, or brand spoofing."
    elif final_score >= 25:
        risk_level = 'SUSPICIOUS'
        color = 'amber'
        summary = f"Domain '{domain}' carries warning signs (e.g. low-trust TLD, shortener, or unverified redirects). Proceed with extreme caution."
    else:
        risk_level = 'SAFE'
        color = 'green'
        summary = f"No active red flags found for '{domain}'. (Always verify destination independently before inputting payment credentials)."

    engine_label = "Live Threat Intelligence (Safe Browsing / VirusTotal)" if (safe_browsing_checked or virustotal_checked) else "Deep Domain Threat Heuristics (Offline)"

    return {
        'fullUrl': clean_url,
        'domain': domain,
        'protocol': protocol,
        'isHttps': is_https,
        'isIpAddress': is_ip,
        'isShortened': is_shortener,
        'isSuspiciousTld': is_suspicious_tld,
        'detectedSpoofedBrand': detected_spoofed_brand,
        'subdomainsCount': subdomains_count,
        'riskScore': final_score,
        'riskLevel': risk_level,
        'color': color,
        'summary': summary,
        'warnings': warnings,
        'engineType': engine_label,
        'threatSources': threat_sources if threat_sources else ['Offline Threat Heuristics Engine (Verified)']
    }
