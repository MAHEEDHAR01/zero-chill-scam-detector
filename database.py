"""
ZERO CHILL 3.0 – Database Architecture
SQLite-backed persistence for scans, digital evidence, verified advisories, and system telemetry.
"""

import sqlite3
import json
import os
from datetime import datetime
from typing import Dict, Any, List, Optional

DB_PATH = os.path.join(os.path.dirname(__file__), 'zero_chill.db')

def get_db_connection():
    """Get a connection to the SQLite database with row factory enabled."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize database tables with schema migrations and seed baseline data."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Scans Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS scans (
        id TEXT PRIMARY KEY,
        scan_type TEXT NOT NULL, -- 'text', 'screenshot', 'url', 'email', 'qr', 'document'
        input_text TEXT NOT NULL,
        clean_snippet TEXT,
        risk_level TEXT NOT NULL, -- 'SAFE', 'SUSPICIOUS', 'HIGH-RISK SCAM'
        risk_score INTEGER NOT NULL,
        scam_category TEXT NOT NULL,
        detected_indicators TEXT, -- JSON
        highlighted_phrases TEXT, -- JSON
        explanation TEXT,
        recommendations TEXT, -- JSON
        legal_sections TEXT, -- JSON
        gov_services TEXT, -- JSON
        confidence_score REAL DEFAULT 0.90,
        uncertainty_rating TEXT DEFAULT 'Low', -- 'Low', 'Moderate', 'High'
        language TEXT DEFAULT 'en', -- 'en', 'hi', 'te', 'mixed'
        engine TEXT DEFAULT 'Rule-Based Threat Heuristics',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # 2. Evidence Vault Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS evidence (
        id TEXT PRIMARY KEY,
        incident_title TEXT NOT NULL,
        incident_type TEXT NOT NULL,
        incident_date TEXT,
        incident_time TEXT,
        description TEXT,
        suspect_details TEXT,
        financial_loss REAL DEFAULT 0.0,
        transaction_utr TEXT,
        file_path TEXT,
        file_name TEXT,
        file_type TEXT,
        file_size INTEGER,
        extracted_text TEXT,
        redacted_text TEXT,
        evidence_checklist TEXT, -- JSON
        status TEXT DEFAULT 'PRESERVED', -- 'PRESERVED', 'EXPORTED', 'REPORTED'
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # 3. Verified Advisories Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS advisories (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        source TEXT NOT NULL, -- 'CERT-In', 'RBI', 'TRAI', 'MHA / I4C', 'PIB'
        source_url TEXT NOT NULL,
        published_date TEXT NOT NULL,
        category TEXT NOT NULL,
        summary TEXT NOT NULL,
        actionable_advice TEXT NOT NULL,
        severity TEXT DEFAULT 'HIGH', -- 'CRITICAL', 'HIGH', 'ADVISORY'
        verified_date TEXT DEFAULT '2026-11-01',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    conn.commit()
    conn.close()
    print("[Database] ZERO CHILL 3.0 SQLite schema initialized successfully.")

# ----------------- SCAN OPERATIONS -----------------

def save_scan(data: Dict[str, Any]) -> str:
    """Save an analysis scan record into SQLite database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    scan_id = data.get('id') or f"scan-{int(datetime.now().timestamp()*1000)}"
    input_text = data.get('input_text', '')
    snippet = data.get('snippet') or (input_text[:110] + '...' if len(input_text) > 110 else input_text)

    cursor.execute('''
    INSERT INTO scans (
        id, scan_type, input_text, clean_snippet, risk_level, risk_score,
        scam_category, detected_indicators, highlighted_phrases, explanation,
        recommendations, legal_sections, gov_services, confidence_score,
        uncertainty_rating, language, engine
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        scan_id,
        data.get('scan_type', 'text'),
        input_text,
        snippet,
        data.get('riskLevel', 'SAFE'),
        data.get('riskScore', 0),
        data.get('scamType', 'Unknown'),
        json.dumps(data.get('indicators', [])),
        json.dumps(data.get('highlightedPhrases', [])),
        data.get('explanation', ''),
        json.dumps(data.get('recommendedSteps', [])),
        json.dumps(data.get('legalSections', [])),
        json.dumps(data.get('govServices', [])),
        data.get('confidenceScore', 0.92),
        data.get('uncertaintyRating', 'Low'),
        data.get('language', 'en'),
        data.get('engine', 'Heuristic')
    ))

    conn.commit()
    conn.close()
    return scan_id

def get_scans(limit: int = 50, filter_risk: Optional[str] = None) -> List[Dict[str, Any]]:
    """Retrieve scan history from database with optional risk filter."""
    conn = get_db_connection()
    cursor = conn.cursor()

    if filter_risk and filter_risk != 'ALL':
        cursor.execute(
            'SELECT * FROM scans WHERE risk_level = ? ORDER BY created_at DESC LIMIT ?',
            (filter_risk, limit)
        )
    else:
        cursor.execute(
            'SELECT * FROM scans ORDER BY created_at DESC LIMIT ?',
            (limit,)
        )

    rows = cursor.fetchall()
    scans = []
    for r in rows:
        scans.append({
            'id': r['id'],
            'scan_type': r['scan_type'],
            'input_text': r['input_text'],
            'clean_snippet': r['clean_snippet'],
            'risk_level': r['risk_level'],
            'risk_score': r['risk_score'],
            'scam_category': r['scam_category'],
            'detected_indicators': json.loads(r['detected_indicators'] or '[]'),
            'highlighted_phrases': json.loads(r['highlighted_phrases'] or '[]'),
            'explanation': r['explanation'],
            'recommendations': json.loads(r['recommendations'] or '[]'),
            'legal_sections': json.loads(r['legal_sections'] or '[]'),
            'gov_services': json.loads(r['gov_services'] or '[]'),
            'confidence_score': r['confidence_score'],
            'uncertainty_rating': r['uncertainty_rating'],
            'language': r['language'],
            'engine': r['engine'],
            'created_at': r['created_at']
        })
    conn.close()
    return scans

def delete_scan(scan_id: str) -> bool:
    """Delete a specific scan record."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM scans WHERE id = ?', (scan_id,))
    deleted = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return deleted

def clear_all_scans() -> int:
    """Clear all scans from database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM scans')
    count = cursor.rowcount
    conn.commit()
    conn.close()
    return count

def get_telemetry_stats() -> Dict[str, Any]:
    """Calculate real database-backed telemetry metrics and distribution."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) as total FROM scans')
    total = cursor.fetchone()['total']

    cursor.execute("SELECT COUNT(*) as count FROM scans WHERE risk_level = 'SAFE'")
    safe_count = cursor.fetchone()['count']

    cursor.execute("SELECT COUNT(*) as count FROM scans WHERE risk_level = 'SUSPICIOUS'")
    suspicious_count = cursor.fetchone()['count']

    cursor.execute("SELECT COUNT(*) as count FROM scans WHERE risk_level = 'HIGH-RISK SCAM'")
    high_risk_count = cursor.fetchone()['count']

    cursor.execute("SELECT AVG(risk_score) as avg_score FROM scans")
    avg_score = cursor.fetchone()['avg_score'] or 0

    # Category breakdown
    cursor.execute('''
    SELECT scam_category, COUNT(*) as count 
    FROM scans 
    GROUP BY scam_category 
    ORDER BY count DESC 
    LIMIT 6
    ''')
    category_counts = [{'category': r['scam_category'], 'count': r['count']} for r in cursor.fetchall()]

    # Scan types breakdown
    cursor.execute('''
    SELECT scan_type, COUNT(*) as count 
    FROM scans 
    GROUP BY scan_type
    ''')
    type_counts = [{'type': r['scan_type'], 'count': r['count']} for r in cursor.fetchall()]

    conn.close()
    return {
        'totalScans': total,
        'safeScans': safe_count,
        'suspiciousScans': suspicious_count,
        'highRiskScans': high_risk_count,
        'averageRiskScore': round(avg_score, 1),
        'topCategories': category_counts,
        'scanTypes': type_counts
    }

# ----------------- EVIDENCE OPERATIONS -----------------

def save_evidence(data: Dict[str, Any]) -> str:
    """Save an evidence record into the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    evidence_id = data.get('id') or f"ev-{int(datetime.now().timestamp()*1000)}"

    cursor.execute('''
    INSERT INTO evidence (
        id, incident_title, incident_type, incident_date, incident_time,
        description, suspect_details, financial_loss, transaction_utr,
        file_path, file_name, file_type, file_size, extracted_text,
        redacted_text, evidence_checklist, status
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        evidence_id,
        data.get('incident_title', 'Cyber Incident Evidence'),
        data.get('incident_type', 'General Cyber Fraud'),
        data.get('incident_date', datetime.now().strftime('%Y-%m-%d')),
        data.get('incident_time', datetime.now().strftime('%H:%M')),
        data.get('description', ''),
        data.get('suspect_details', ''),
        data.get('financial_loss', 0.0),
        data.get('transaction_utr', ''),
        data.get('file_path', ''),
        data.get('file_name', ''),
        data.get('file_type', ''),
        data.get('file_size', 0),
        data.get('extracted_text', ''),
        data.get('redacted_text', ''),
        json.dumps(data.get('evidence_checklist', [])),
        data.get('status', 'PRESERVED')
    ))

    conn.commit()
    conn.close()
    return evidence_id

def get_evidence_list() -> List[Dict[str, Any]]:
    """Retrieve all preserved evidence items."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM evidence ORDER BY created_at DESC')
    rows = cursor.fetchall()
    evidence_list = []
    for r in rows:
        evidence_list.append({
            'id': r['id'],
            'incident_title': r['incident_title'],
            'incident_type': r['incident_type'],
            'incident_date': r['incident_date'],
            'incident_time': r['incident_time'],
            'description': r['description'],
            'suspect_details': r['suspect_details'],
            'financial_loss': r['financial_loss'],
            'transaction_utr': r['transaction_utr'],
            'file_name': r['file_name'],
            'file_type': r['file_type'],
            'file_size': r['file_size'],
            'extracted_text': r['extracted_text'],
            'redacted_text': r['redacted_text'],
            'evidence_checklist': json.loads(r['evidence_checklist'] or '[]'),
            'status': r['status'],
            'created_at': r['created_at']
        })
    conn.close()
    return evidence_list

def delete_evidence(evidence_id: str) -> bool:
    """Delete an evidence record and its file."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT file_path FROM evidence WHERE id = ?', (evidence_id,))
    row = cursor.fetchone()
    if row and row['file_path'] and os.path.exists(row['file_path']):
        try:
            os.remove(row['file_path'])
        except Exception as e:
            print(f"[Evidence] Error deleting file: {e}")

    cursor.execute('DELETE FROM evidence WHERE id = ?', (evidence_id,))
    deleted = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return deleted

# Initialize database on module import
if __name__ == '__main__':
    init_db()
    stats = get_telemetry_stats()
    print("[Database Test] Stats:", stats)
