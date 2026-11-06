"""
ScamShield AI - Gemini AI Scam Analysis Module
Connects to Google Gemini API when an API key is provided,
with transparent, 100% resilient fallback to local heuristics.
"""

import os
import json
import requests
from typing import Dict, Any, Optional
from scam_engine import analyze_scam_message

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

SYSTEM_INSTRUCTION = """You are ScamShield AI, an elite cybersecurity and fraud prevention analyst.
Your task is to analyze the user's message (SMS, WhatsApp, Email, Job Offer, Loan, Phishing text) and determine if it is a scam.

You must categorize into one of three EXACT levels:
1. SAFE - No significant scam indicators. Resembles legitimate transactional/informational message.
2. SUSPICIOUS - One or more warning signs (unsolicited offers, questionable claims, pressure, unverified links).
3. HIGH-RISK SCAM - Strong indicators of fraud, phishing, impersonation, OTP/PIN theft, or extortion.

Return ONLY a valid JSON object with these EXACT keys:
{
  "riskLevel": "SAFE" | "SUSPICIOUS" | "HIGH-RISK SCAM",
  "riskScore": integer between 0 and 100,
  "scamType": "short string identifying scam category e.g. Bank Impersonation / Fake Job Scam",
  "indicators": [
    {
      "name": "Short title of warning sign",
      "severity": "CRITICAL" | "HIGH" | "MEDIUM",
      "category": "Category name",
      "description": "Simple 1-sentence explanation"
    }
  ],
  "highlightedPhrases": ["exact word or phrase 1", "exact word or phrase 2"],
  "explanation": "Clear, easy-to-understand 2-3 sentence explanation in simple English for everyday people",
  "recommendedSteps": [
    "Actionable safety step 1",
    "Actionable safety step 2"
  ]
}

CRITICAL RULES:
- Never claim a message is definitely authentic simply because no red flags were found.
- If asking for OTP, PIN, password, or claiming account blocked with link, score MUST be >= 85 and HIGH-RISK SCAM.
- If money was lost in India, recommend dialing 1930 or visiting cybercrime.gov.in.
- Respond with pure JSON only, no markdown codeblocks, no commentary outside JSON.
"""

def analyze_with_gemini(text: str, api_key: Optional[str] = None) -> Dict[str, Any]:
    """
    Attempt analysis using Gemini API. If no key, network error, or invalid response,
    gracefully fall back to local rule-based heuristic engine.
    """
    key = api_key or os.environ.get("GEMINI_API_KEY", "").strip()

    # If no key provided, immediately use heuristic engine
    if not key:
        result = analyze_scam_message(text)
        result["engine"] = "Rule-Based Threat Heuristics (Offline Demo Mode)"
        return result

    try:
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": f"{SYSTEM_INSTRUCTION}\n\nAnalyze this message:\n\"\"\"{text}\"\"\""}
                    ]
                }
            ],
            "generationConfig": {
                "temperature": 0.2,
                "responseMimeType": "application/json"
            }
        }

        response = requests.post(
            f"{GEMINI_API_URL}?key={key}",
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=10
        )

        if response.status_code != 200:
            print(f"[Gemini API Warning] Status code {response.status_code}: {response.text}")
            result = analyze_scam_message(text)
            result["engine"] = f"Rule-Based Threat Heuristics (Gemini API returned {response.status_code})"
            return result

        resp_json = response.json()
        candidates = resp_json.get("candidates", [])
        if not candidates:
            result = analyze_scam_message(text)
            result["engine"] = "Rule-Based Threat Heuristics (No Gemini candidates)"
            return result

        raw_content = candidates[0].get("content", {}).get("parts", [{}])[0].get("text", "")
        # Clean potential markdown wrapping
        clean_json_str = raw_content.strip()
        if clean_json_str.startswith("```json"):
            clean_json_str = clean_json_str[7:]
        if clean_json_str.startswith("```"):
            clean_json_str = clean_json_str[3:]
        if clean_json_str.endswith("```"):
            clean_json_str = clean_json_str[:-3]
        clean_json_str = clean_json_str.strip()

        parsed = json.loads(clean_json_str)

        # Re-verify and ensure required fields
        risk_level = parsed.get("riskLevel", "SUSPICIOUS")
        if risk_level not in ["SAFE", "SUSPICIOUS", "HIGH-RISK SCAM"]:
            risk_level = "SUSPICIOUS"

        risk_score = parsed.get("riskScore", 50)
        try:
            risk_score = max(0, min(100, int(risk_score)))
        except (ValueError, TypeError):
            risk_score = 50

        color = "green" if risk_level == "SAFE" else "amber" if risk_level == "SUSPICIOUS" else "red"

        # Also extract URLs from rule engine to enrich
        local_eval = analyze_scam_message(text)

        # Merge highlights
        combined_highlights = list(set(
            parsed.get("highlightedPhrases", []) + local_eval.get("highlightedPhrases", [])
        ))

        return {
            "riskLevel": risk_level,
            "riskScore": risk_score,
            "color": color,
            "scamType": parsed.get("scamType", "AI Analyzed Scam Threat"),
            "indicators": parsed.get("indicators", local_eval.get("indicators", [])),
            "highlightedPhrases": combined_highlights,
            "explanation": parsed.get("explanation", local_eval.get("explanation")),
            "recommendedSteps": parsed.get("recommendedSteps", local_eval.get("recommendedSteps")),
            "detectedUrls": local_eval.get("detectedUrls", []),
            "engine": "Gemini 2.5 Flash + ScamShield Guardrails"
        }

    except Exception as e:
        print(f"[Gemini Exception, Fallback to Local Engine]: {e}")
        fallback = analyze_scam_message(text)
        fallback["engine"] = f"Rule-Based Threat Heuristics (Offline Fallback)"
        return fallback
