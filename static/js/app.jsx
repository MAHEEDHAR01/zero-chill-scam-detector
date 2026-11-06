/**
 * ZERO CHILL 3.0 – Ultimate AI Cybersecurity, Cybercrime Prevention & Legal Action Platform
 * Complete Modern React 18 Dashboard Application
 */

const { useState, useEffect, useRef, useMemo } = React;

// Inline SVG Icon components matching Lucide React styling
const Icon = ({ name, className = "w-5 h-5", ...props }) => {
  const icons = {
    Shield: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
      </svg>
    ),
    ShieldAlert: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
        <line x1="12" y1="8" x2="12" y2="12"/>
        <line x1="12" y1="16" x2="12.01" y2="16"/>
      </svg>
    ),
    ShieldCheck: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
        <polyline points="9 12 11 14 15 10"/>
      </svg>
    ),
    AlertTriangle: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/>
        <line x1="12" y1="9" x2="12" y2="13"/>
        <line x1="12" y1="17" x2="12.01" y2="17"/>
      </svg>
    ),
    AlertOctagon: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <polygon points="7.86 2 16.14 2 22 7.86 22 16.14 16.14 22 7.86 22 2 16.14 2 7.86 7.86 2"/>
        <line x1="12" y1="8" x2="12" y2="12"/>
        <line x1="12" y1="16" x2="12.01" y2="16"/>
      </svg>
    ),
    FileText: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
        <polyline points="14 2 14 8 20 8"/>
        <line x1="16" y1="13" x2="8" y2="13"/>
        <line x1="16" y1="17" x2="8" y2="17"/>
      </svg>
    ),
    Image: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
        <circle cx="8.5" cy="8.5" r="1.5"/>
        <polyline points="21 15 16 10 5 21"/>
      </svg>
    ),
    UploadCloud: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <polyline points="16 16 12 12 8 16"/>
        <line x1="12" y1="12" x2="12" y2="21"/>
        <path d="M20.39 18.39A5 5 0 0 0 18 9h-1.26A8 8 0 1 0 3 16.3"/>
        <polyline points="16 16 12 12 8 16"/>
      </svg>
    ),
    CheckCircle: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
        <polyline points="22 4 12 14.01 9 11.01"/>
      </svg>
    ),
    History: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/>
        <path d="M3 3v5h5"/>
        <polyline points="12 7 12 12 15 15"/>
      </svg>
    ),
    Trash2: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <polyline points="3 6 5 6 21 6"/>
        <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>
        <line x1="10" y1="11" x2="10" y2="17"/>
        <line x1="14" y1="11" x2="14" y2="17"/>
      </svg>
    ),
    ExternalLink: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>
        <polyline points="15 3 21 3 21 9"/>
        <line x1="10" y1="14" x2="21" y2="3"/>
      </svg>
    ),
    PhoneCall: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <path d="M15.05 5A5 5 0 0 1 19 8.95M15.05 1A9 9 0 0 1 23 8.94m-1 7.98v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
      </svg>
    ),
    Copy: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"/>
        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/>
      </svg>
    ),
    RefreshCw: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <polyline points="23 4 23 10 17 10"/>
        <polyline points="1 20 1 14 7 14"/>
        <path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/>
      </svg>
    ),
    Link2: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <path d="M9 17H7A5 5 0 0 1 7 7h2"/>
        <path d="M15 7h2a5 5 0 1 1 0 10h-2"/>
        <line x1="8" y1="12" x2="16" y2="12"/>
      </svg>
    ),
    BookOpen: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>
        <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>
      </svg>
    ),
    Scale: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/>
        <path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/>
        <path d="M7 21h10"/>
        <path d="M12 3v18"/>
        <path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/>
      </svg>
    ),
    Building: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <rect x="4" y="2" width="16" height="20" rx="2" ry="2"/>
        <path d="M9 22v-4h6v4"/>
        <path d="M8 6h.01"/>
        <path d="M16 6h.01"/>
        <path d="M8 10h.01"/>
        <path d="M16 10h.01"/>
        <path d="M8 14h.01"/>
        <path d="M16 14h.01"/>
      </svg>
    ),
    Zap: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
      </svg>
    ),
    Lock: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
        <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
      </svg>
    ),
    Newspaper: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <path d="M4 22h16a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v16a2 2 0 0 1-2 2Zm0 0a2 2 0 0 1-2-2v-9c0-1.1.9-2 2-2h2"/>
        <path d="M18 14h-8"/>
        <path d="M15 18h-5"/>
        <path d="M10 6h8v4h-8V6Z"/>
      </svg>
    ),
    Bot: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <path d="M12 8V4H8"/>
        <rect width="16" height="12" x="4" y="8" rx="2"/>
        <path d="M2 14h2"/>
        <path d="M20 14h2"/>
        <path d="M15 13v2"/>
        <path d="M9 13v2"/>
      </svg>
    ),
    BarChart3: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <path d="M3 3v18h18"/>
        <path d="M18 17V9"/>
        <path d="M13 17V5"/>
        <path d="M8 17v-3"/>
      </svg>
    ),
    Send: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <line x1="22" y1="2" x2="11" y2="13"/>
        <polygon points="22 2 15 22 11 13 2 9 22 2"/>
      </svg>
    ),
    QrCode: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <rect width="5" height="5" x="3" y="3" rx="1"/>
        <rect width="5" height="5" x="16" y="3" rx="1"/>
        <rect width="5" height="5" x="3" y="16" rx="1"/>
        <path d="M21 16h-3a2 2 0 0 0-2 2v3"/>
        <path d="M21 21v.01"/>
        <path d="M12 7v3a2 2 0 0 1-2 2H7"/>
        <path d="M3 12h.01"/>
        <path d="M12 3h.01"/>
        <path d="M12 16v.01"/>
        <path d="M16 12h1"/>
        <path d="M21 12v.01"/>
        <path d="M12 21v-1"/>
      </svg>
    ),
    Mail: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <rect width="20" height="16" x="2" y="4" rx="2"/>
        <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
      </svg>
    ),
    Key: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <path d="m21 2-2 2m-1.5 1.5L16 7l-1.5-1.5-3 3-1.5-1.5L8.5 8.5 7 7l-1.5 1.5 1.5 1.5-4 4a5 5 0 1 0 7.07 7.07l4-4 1.5 1.5 1.5-1.5-1.5-1.5 3-3 1.5 1.5 1.5-1.5-1.5-1.5 1.5-1.5Z"/>
      </svg>
    ),
    Printer: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <polyline points="6 9 6 2 18 2 18 9"/>
        <path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/>
        <rect width="12" height="8" x="6" y="14"/>
      </svg>
    ),
    X: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <line x1="18" y1="6" x2="6" y2="18"/>
        <line x1="6" y1="6" x2="18" y2="18"/>
      </svg>
    ),
    ArrowRight: (
      <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
        <line x1="5" y1="12" x2="19" y2="12"/>
        <polyline points="12 5 19 12 12 19"/>
      </svg>
    )
  };

  return icons[name] || icons.Shield;
};

function ZeroChillApp() {
  // Navigation tabs: 'scanner', 'actions', 'gov', 'laws', 'evidence', 'advisories', 'assistant', 'dashboard'
  const [activeTab, setActiveTab] = useState("scanner");
  const [scannerSubTab, setScannerSubTab] = useState("message"); // 'message', 'screenshot', 'url', 'email', 'qr'
  const [appState, setAppState] = useState("idle"); // 'idle', 'scanning', 'report'

  // Input states
  const [inputText, setInputText] = useState("");
  const [inputUrl, setInputUrl] = useState("");
  const [inputEmail, setInputEmail] = useState("");
  const [inputQr, setInputQr] = useState("");
  const [analysisResult, setAnalysisResult] = useState(null);

  // Language state: 'en', 'hi', 'te'
  const [currentLang, setCurrentLang] = useState("en");

  // Screenshot OCR states
  const [screenshotPreview, setScreenshotPreview] = useState(null);
  const [isOcrRunning, setIsOcrRunning] = useState(false);
  const [ocrProgress, setOcrProgress] = useState({ progress: 0, status: "Ready" });
  const [extractedOcrText, setExtractedOcrText] = useState("");
  const fileInputRef = useRef(null);

  // Evidence Vault state
  const [evidenceList, setEvidenceList] = useState([]);
  const [evidenceTitle, setEvidenceTitle] = useState("");
  const [evidenceType, setEvidenceType] = useState("Bank Phishing");
  const [evidenceLoss, setEvidenceLoss] = useState("");
  const [evidenceUtr, setEvidenceUtr] = useState("");
  const [evidenceSuspect, setEvidenceSuspect] = useState("");
  const [evidenceDesc, setEvidenceDesc] = useState("");
  const [evidenceFile, setEvidenceFile] = useState(null);
  const [isUploadingEvidence, setIsUploadingEvidence] = useState(false);

  // Advisories state
  const [advisories, setAdvisories] = useState([]);
  const [advisorySearch, setAdvisorySearch] = useState("");
  const [advisoryCat, setAdvisoryCat] = useState("ALL");

  // Cyber Laws state
  const [cyberLaws, setCyberLaws] = useState([]);
  const [lawSearch, setLawSearch] = useState("");

  // Gov Services state
  const [govServices, setGovServices] = useState([]);

  // Telemetry & History state
  const [telemetry, setTelemetry] = useState({ totalScans: 0, safeScans: 0, suspiciousScans: 0, highRiskScans: 0, averageRiskScore: 0 });
  const [scanHistory, setScanHistory] = useState([]);
  const [historyFilter, setHistoryFilter] = useState("ALL");

  // AI Assistant Chat state
  const [chatMessages, setChatMessages] = useState([
    {
      role: "model",
      content: "Hello! I am ZERO CHILL AI, your Indian Cyber Safety & Legal Rights Assistant. You can ask me questions about scams, reporting to 1930, the IT Act 2000, or evidence preservation in English, हिन्दी (Hindi), or తెలుగు (Telugu)!"
    }
  ]);
  const [chatInput, setChatInput] = useState("");
  const [isChatThinking, setIsChatThinking] = useState(false);

  // Modals & settings
  const [geminiApiKey, setGeminiApiKey] = useState(() => localStorage.getItem("zerochill_gemini_key") || "");
  const [isApiKeyModalOpen, setIsApiKeyModalOpen] = useState(false);
  const [isEmergencyModalOpen, setIsEmergencyModalOpen] = useState(false);
  const [toastMessage, setToastMessage] = useState(null);

  const showToast = (message, type = "info") => {
    setToastMessage({ message, type });
    setTimeout(() => {
      setToastMessage(curr => (curr?.message === message ? null : curr));
    }, 4000);
  };

  // Fetch initial data from backend
  useEffect(() => {
    fetchStats();
    fetchLaws();
    fetchGovServices();
    fetchAdvisories();
    fetchEvidence();
    fetchHistory();
  }, []);

  const fetchStats = async () => {
    try {
      const res = await fetch("/api/stats");
      if (res.ok) {
        const data = await res.json();
        setTelemetry(data);
      }
    } catch(e) {}
  };

  const fetchLaws = async () => {
    try {
      const res = await fetch("/api/laws");
      if (res.ok) {
        const data = await res.json();
        setCyberLaws(data.laws || []);
      }
    } catch(e) {}
  };

  const fetchGovServices = async () => {
    try {
      const res = await fetch("/api/gov-services");
      if (res.ok) {
        const data = await res.json();
        setGovServices(data.services || []);
      }
    } catch(e) {}
  };

  const fetchAdvisories = async () => {
    try {
      const res = await fetch("/api/advisories");
      if (res.ok) {
        const data = await res.json();
        setAdvisories(data.advisories || []);
      }
    } catch(e) {}
  };

  const fetchEvidence = async () => {
    try {
      const res = await fetch("/api/evidence");
      if (res.ok) {
        const data = await res.json();
        setEvidenceList(data.evidence || []);
      }
    } catch(e) {}
  };

  const fetchHistory = async () => {
    try {
      const res = await fetch("/api/history");
      if (res.ok) {
        const data = await res.json();
        setScanHistory(data.scans || []);
      }
    } catch(e) {}
  };

  // Main Analyze Function
  const handleAnalyze = async (textToAnalyze, scanType = "text") => {
    if (!textToAnalyze || !textToAnalyze.trim()) {
      showToast("Please provide content to analyze.", "error");
      return;
    }

    setAppState("scanning");
    window.scrollTo({ top: 120, behavior: "smooth" });
    const startTime = Date.now();

    try {
      let finalResult = null;

      // Call Backend API
      try {
        const res = await fetch("/api/analyze", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            text: textToAnalyze,
            scanType: scanType,
            apiKey: geminiApiKey || undefined
          })
        });

        if (res.ok) {
          finalResult = await res.json();
        } else {
          throw new Error("Backend response error");
        }
      } catch (backendErr) {
        console.warn("Backend unavailable, using client heuristic engine:", backendErr);
        if (window.ZeroChillLocalAnalyzer) {
          finalResult = window.ZeroChillLocalAnalyzer.analyze(textToAnalyze);
        }
      }

      if (!finalResult && window.ZeroChillLocalAnalyzer) {
        finalResult = window.ZeroChillLocalAnalyzer.analyze(textToAnalyze);
      }

      const elapsed = Date.now() - startTime;
      const waitTime = Math.max(0, 1600 - elapsed);

      setTimeout(() => {
        setAnalysisResult({
          ...finalResult,
          analyzedText: textToAnalyze
        });
        setAppState("report");
        fetchStats();
        fetchHistory();
        window.scrollTo({ top: 80, behavior: "smooth" });
      }, waitTime);

    } catch (err) {
      console.error("Scan error:", err);
      showToast("Analysis failed. Please try again.", "error");
      setAppState("idle");
    }
  };

  // OCR Screenshot Handler
  const handleScreenshotUpload = async (e) => {
    const file = e.target.files?.[0];
    if (!file) return;

    if (!file.type.startsWith("image/")) {
      showToast("Please upload an image (JPG, PNG, JPEG).", "error");
      return;
    }

    const previewUrl = URL.createObjectURL(file);
    setScreenshotPreview(previewUrl);
    setExtractedOcrText("");
    setIsOcrRunning(true);
    setOcrProgress({ progress: 10, status: "Initializing Tesseract OCR Core..." });

    try {
      if (typeof Tesseract === "undefined") {
        throw new Error("Tesseract.js OCR library is still loading.");
      }

      const res = await Tesseract.recognize(file, "eng", {
        logger: m => {
          if (m.status === "recognizing text") {
            const pct = Math.round((m.progress || 0) * 100);
            setOcrProgress({ progress: pct, status: `Reading text from screenshot (${pct}%)...` });
          } else if (m.status === "loading tesseract core") {
            setOcrProgress({ progress: 25, status: "Loading AI OCR Core..." });
          }
        }
      });

      const extracted = (res?.data?.text || "").trim();
      setIsOcrRunning(false);

      if (extracted) {
        setExtractedOcrText(extracted);
        showToast("Text successfully extracted from screenshot!", "success");
      } else {
        setExtractedOcrText("No clear text detected. Please upload a higher resolution screenshot.");
        showToast("No clear text detected.", "warning");
      }
    } catch(err) {
      console.error(err);
      setIsOcrRunning(false);
      showToast("OCR failed. You can paste the text manually.", "error");
    }
  };

  // Evidence Upload Handler
  const handleEvidenceSubmit = async (e) => {
    e.preventDefault();
    if (!evidenceTitle.trim()) {
      showToast("Please enter an incident title.", "error");
      return;
    }

    setIsUploadingEvidence(true);
    const formData = new FormData();
    formData.append("incident_title", evidenceTitle);
    formData.append("incident_type", evidenceType);
    formData.append("financial_loss", evidenceLoss || "0");
    formData.append("transaction_utr", evidenceUtr);
    formData.append("suspect_details", evidenceSuspect);
    formData.append("description", evidenceDesc);
    formData.append("checklist", JSON.stringify([
      "Screenshot of suspicious communication preserved",
      "Transaction UTR / Bank SMS preserved",
      "Suspect phone number and VPA recorded"
    ]));

    if (evidenceFile) {
      formData.append("file", evidenceFile);
    } else if (analysisResult?.analyzedText) {
      formData.append("extracted_text", analysisResult.analyzedText);
    }

    try {
      const res = await fetch("/api/evidence/upload", {
        method: "POST",
        body: formData
      });
      if (res.ok) {
        showToast("Incident evidence preserved with sensitive PII redaction!", "success");
        setEvidenceTitle("");
        setEvidenceLoss("");
        setEvidenceUtr("");
        setEvidenceSuspect("");
        setEvidenceDesc("");
        setEvidenceFile(null);
        fetchEvidence();
      } else {
        throw new Error("Upload failed");
      }
    } catch(err) {
      showToast("Failed to preserve evidence.", "error");
    } finally {
      setIsUploadingEvidence(false);
    }
  };

  // Chat Message Handler
  const handleSendChatMessage = async (e) => {
    e?.preventDefault();
    const query = chatInput.trim();
    if (!query) return;

    const newMessages = [...chatMessages, { role: "user", content: query }];
    setChatMessages(newMessages);
    setChatInput("");
    setIsChatThinking(true);

    try {
      const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          message: query,
          apiKey: geminiApiKey || undefined,
          history: newMessages.slice(-6)
        })
      });

      if (res.ok) {
        const data = await res.json();
        setChatMessages([...newMessages, { role: "model", content: data.reply, engine: data.engine }]);
      } else {
        throw new Error("Chat error");
      }
    } catch(e) {
      setChatMessages([...newMessages, {
        role: "model",
        content: "I am ready to help. If money was lost, call 1930 immediately. File formal complaints at cybercrime.gov.in."
      }]);
    } finally {
      setIsChatThinking(false);
    }
  };

  // Copy Safety Advice
  const handleCopyAdvice = () => {
    if (!analysisResult) return;
    const text = `🛡️ ZERO CHILL 3.0 Safety Assessment:
Risk Classification: ${analysisResult.riskLevel} (${analysisResult.riskScore}/100)
Category: ${analysisResult.scamType}

⚠️ Analysis:
${analysisResult.explanation}

🛡️ Recommended Steps:
${(analysisResult.recommendedSteps || []).map(s => "• " + s).join("\n")}

🚨 Indian Cyber Financial Emergency: Call 1930 within the 2-Hour Golden Window or file at cybercrime.gov.in.`;

    navigator.clipboard.writeText(text).then(() => {
      showToast("Safety assessment copied to clipboard!", "success");
    });
  };

  // Filtered Laws
  const filteredLaws = useMemo(() => {
    if (!lawSearch.trim()) return cyberLaws;
    const q = lawSearch.toLowerCase();
    return cyberLaws.filter(l => 
      l.section.toLowerCase().includes(q) || 
      l.title.toLowerCase().includes(q) || 
      l.simpleExplanation.toLowerCase().includes(q)
    );
  }, [cyberLaws, lawSearch]);

  // Filtered Advisories
  const filteredAdvisories = useMemo(() => {
    let list = advisories;
    if (advisoryCat !== "ALL") {
      list = list.filter(a => a.category.toLowerCase().includes(advisoryCat.toLowerCase()));
    }
    if (advisorySearch.trim()) {
      const q = advisorySearch.toLowerCase();
      list = list.filter(a => a.title.toLowerCase().includes(q) || a.summary.toLowerCase().includes(q));
    }
    return list;
  }, [advisories, advisoryCat, advisorySearch]);

  return (
    <div className="min-h-screen bg-[#070d1b] text-slate-100 flex flex-col selection:bg-cyan-500/30 selection:text-cyan-200">
      {/* Background Cyber Defense Grid & Ambient Glows */}
      <div className="fixed inset-0 pointer-events-none cyber-grid opacity-30 z-0"></div>
      <div className="fixed -top-40 -left-40 w-96 h-96 bg-cyan-600/10 rounded-full blur-[140px] pointer-events-none z-0"></div>
      <div className="fixed top-1/3 -right-40 w-96 h-96 bg-blue-600/10 rounded-full blur-[140px] pointer-events-none z-0"></div>
      <div className="fixed -bottom-40 left-1/3 w-96 h-96 bg-emerald-600/5 rounded-full blur-[140px] pointer-events-none z-0"></div>

      {/* 1. TOP PERSISTENT EMERGENCY 1930 HELPLINE BANNER */}
      <div className="bg-gradient-to-r from-red-950/90 via-slate-900/90 to-red-950/90 border-b border-red-500/30 px-4 py-2 z-50 sticky top-0 backdrop-blur-md">
        <div className="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-2 text-xs">
          <div className="flex items-center gap-2 text-red-200 font-medium">
            <span className="w-2.5 h-2.5 rounded-full bg-red-500 animate-ping shrink-0"></span>
            <span className="font-bold text-white">NATIONAL CYBERCRIME ALERT:</span>
            <span>Lost money to online fraud? Act within the 2-Hour Golden Window to freeze transfers.</span>
          </div>
          <div className="flex items-center gap-3">
            <a 
              href="tel:1930" 
              className="px-3 py-1 rounded-lg bg-red-600 hover:bg-red-500 text-white font-bold font-mono text-xs flex items-center gap-1.5 shadow-lg shadow-red-600/30 transition"
            >
              <Icon name="PhoneCall" className="w-3.5 h-3.5" />
              <span>DIAL 1930</span>
            </a>
            <button
              onClick={() => setIsEmergencyModalOpen(true)}
              className="text-red-300 underline font-semibold hover:text-white transition"
            >
              Emergency Protocol Guide
            </button>
          </div>
        </div>
      </div>

      {/* 2. HEADER & NAVIGATION BAR */}
      <header className="z-40 glass-panel border-b border-slate-800/80">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 flex flex-col md:flex-row md:items-center justify-between gap-4">
          {/* Logo & Identity */}
          <div 
            onClick={() => { setActiveTab("scanner"); setAppState("idle"); }} 
            className="flex items-center gap-3 cursor-pointer group"
          >
            <div className="w-11 h-11 rounded-2xl bg-gradient-to-tr from-cyan-600 to-blue-500 p-0.5 shadow-lg shadow-cyan-500/20 group-hover:shadow-cyan-500/40 transition duration-300">
              <div className="w-full h-full bg-[#070d1b] rounded-[14px] flex items-center justify-center">
                <Icon name="ShieldAlert" className="w-6 h-6 text-cyan-400 group-hover:scale-110 transition duration-300" />
              </div>
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-xl font-extrabold tracking-tight text-white font-mono-numbers">
                  ZERO CHILL<span className="text-cyan-400"> 3.0</span>
                </span>
                <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full bg-cyan-500/10 text-cyan-300 border border-cyan-500/30">
                  National Hackathon Edition
                </span>
              </div>
              <p className="text-xs text-slate-400">
                AI Cyber Safety, Cybercrime Prevention & Legal Action Platform
              </p>
            </div>
          </div>

          {/* Quick Controls: Engine Key & Language */}
          <div className="flex items-center gap-2 sm:gap-3 self-end md:self-center">
            {/* Language Selector */}
            <div className="flex items-center bg-slate-900 border border-slate-700/80 rounded-xl p-0.5 text-xs font-semibold">
              <button
                onClick={() => { setCurrentLang("en"); showToast("Language: English", "info"); }}
                className={`px-2.5 py-1 rounded-lg transition ${currentLang === "en" ? "bg-cyan-500/20 text-cyan-300 font-bold" : "text-slate-400 hover:text-white"}`}
              >
                English
              </button>
              <button
                onClick={() => { setCurrentLang("hi"); showToast("भाषा: हिन्दी (Hindi)", "info"); }}
                className={`px-2.5 py-1 rounded-lg transition ${currentLang === "hi" ? "bg-cyan-500/20 text-cyan-300 font-bold" : "text-slate-400 hover:text-white"}`}
              >
                हिन्दी
              </button>
              <button
                onClick={() => { setCurrentLang("te"); showToast("భాష: తెలుగు (Telugu)", "info"); }}
                className={`px-2.5 py-1 rounded-lg transition ${currentLang === "te" ? "bg-cyan-500/20 text-cyan-300 font-bold" : "text-slate-400 hover:text-white"}`}
              >
                తెలుగు
              </button>
            </div>

            {/* AI Engine Status Button */}
            <button 
              onClick={() => setIsApiKeyModalOpen(true)}
              className="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-700 text-xs font-medium text-slate-300 hover:border-cyan-500/50 hover:text-cyan-300 transition"
              title="Configure Gemini or Safe Browsing Keys"
            >
              <div className={`w-2 h-2 rounded-full ${geminiApiKey ? "bg-cyan-400 animate-pulse" : "bg-emerald-400"}`}></div>
              <span className="hidden sm:inline">
                {geminiApiKey ? "Gemini AI" : "Heuristic AI"}
              </span>
              <Icon name="Key" className="w-3.5 h-3.5 text-slate-400" />
            </button>
          </div>
        </div>

        {/* 8-PILLAR NAVIGATION TAB BAR */}
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 border-t border-slate-800/80 overflow-x-auto">
          <div className="flex items-center gap-1 py-2 min-w-max">
            {[
              { id: "scanner", label: "Threat Scanner", icon: "Shield" },
              { id: "actions", label: "Action Center", icon: "Zap" },
              { id: "gov", label: "Gov Services", icon: "Building" },
              { id: "laws", label: "Cyber Laws & Rights", icon: "Scale" },
              { id: "evidence", label: "Evidence Vault", icon: "Lock" },
              { id: "advisories", label: "Advisories & News", icon: "Newspaper" },
              { id: "assistant", label: "AI Safety Assistant", icon: "Bot" },
              { id: "dashboard", label: "Telemetry & Stats", icon: "BarChart3" }
            ].map(tab => (
              <button
                key={tab.id}
                onClick={() => {
                  setActiveTab(tab.id);
                  if (tab.id === "scanner") setAppState("idle");
                  window.scrollTo({ top: 100, behavior: "smooth" });
                }}
                className={`flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs font-semibold transition ${
                  activeTab === tab.id
                    ? "bg-gradient-to-r from-cyan-500 to-blue-600 text-white shadow-md shadow-cyan-500/20"
                    : "text-slate-400 hover:text-slate-200 hover:bg-slate-900/60"
                }`}
              >
                <Icon name={tab.icon} className="w-4 h-4" />
                <span>{tab.label}</span>
              </button>
            ))}
          </div>
        </div>
      </header>

      {/* MAIN CONTENT AREA */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 relative z-10 space-y-10">

        {/* ========================================================
            TAB 1: THREAT SCANNER
        ======================================================== */}
        {activeTab === "scanner" && (
          <div className="space-y-8 animate-fadeIn">
            {/* Hero Banner */}
            <section className="text-center space-y-3 pt-2 sm:pt-4">
              <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-xs font-semibold tracking-wide">
                <Icon name="Shield" className="w-3.5 h-3.5" />
                <span>AI CYBER FRAUD DEFENSE & EVIDENCE ECOSYSTEM</span>
              </div>
              <h1 className="text-3xl sm:text-5xl font-extrabold text-white tracking-tight leading-tight">
                Think <span className="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-blue-400 to-indigo-400">Before You Click</span>
              </h1>
              <p className="text-xs sm:text-sm text-slate-300 max-w-2xl mx-auto">
                Scan suspicious SMS, WhatsApp chats, phishing links, fake job offers, predatory loan ads, and QR codes across English, Hindi, and Telugu.
              </p>

              {/* Hackathon Benchmark Buttons */}
              <div className="pt-2">
                <p className="text-[11px] uppercase font-bold tracking-wider text-slate-400 mb-2">
                  ⚡ Load Hackathon Benchmark Scenarios:
                </p>
                <div className="flex flex-wrap items-center justify-center gap-2">
                  {(window.BENCHMARK_SAMPLES || []).map(sample => (
                    <button
                      key={sample.id}
                      onClick={() => {
                        setInputText(sample.text);
                        setScannerSubTab("message");
                        setAppState("idle");
                        showToast(`Loaded ${sample.label}!`, "info");
                      }}
                      className={`px-3 py-1.5 rounded-xl border text-xs font-semibold transition flex items-center gap-1.5 shadow-sm ${
                        sample.category === "HIGH-RISK SCAM"
                          ? "bg-red-500/10 border-red-500/30 text-red-300 hover:bg-red-500/20"
                          : sample.category === "SUSPICIOUS"
                          ? "bg-amber-500/10 border-amber-500/30 text-amber-300 hover:bg-amber-500/20"
                          : "bg-emerald-500/10 border-emerald-500/30 text-emerald-300 hover:bg-emerald-500/20"
                      }`}
                    >
                      <span className={`w-2 h-2 rounded-full ${
                        sample.category === "HIGH-RISK SCAM" ? "bg-red-400 animate-pulse" : sample.category === "SUSPICIOUS" ? "bg-amber-400" : "bg-emerald-400"
                      }`}></span>
                      <span>{sample.label}</span>
                    </button>
                  ))}
                </div>
              </div>
            </section>

            {/* SCANNER SUB-TABS */}
            {appState === "idle" && (
              <div className="space-y-6">
                <div className="flex justify-center">
                  <div className="inline-flex p-1.5 rounded-2xl bg-slate-900/90 border border-slate-800 backdrop-blur-md">
                    {[
                      { id: "message", label: "Text / SMS / WhatsApp", icon: "FileText" },
                      { id: "screenshot", label: "Screenshot OCR", icon: "Image" },
                      { id: "url", label: "Web Link / URL", icon: "Link2" },
                      { id: "email", label: "Email Phishing", icon: "Mail" },
                      { id: "qr", label: "UPI & QR Code", icon: "QrCode" }
                    ].map(st => (
                      <button
                        key={st.id}
                        onClick={() => setScannerSubTab(st.id)}
                        className={`flex items-center gap-1.5 px-4 py-2 rounded-xl text-xs font-semibold transition ${
                          scannerSubTab === st.id
                            ? "bg-cyan-500/20 text-cyan-300 border border-cyan-500/40"
                            : "text-slate-400 hover:text-white"
                        }`}
                      >
                        <Icon name={st.icon} className="w-3.5 h-3.5" />
                        <span>{st.label}</span>
                      </button>
                    ))}
                  </div>
                </div>

                {/* SUB-TAB 1: MESSAGE TEXT SCANNER */}
                {scannerSubTab === "message" && (
                  <div className="max-w-3xl mx-auto glass-panel-elevated rounded-3xl p-6 sm:p-8 space-y-6">
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-2 text-sm font-bold text-white">
                        <Icon name="FileText" className="w-4 h-4 text-cyan-400" />
                        <span>Paste Suspicious Message (SMS, WhatsApp, Social Chat)</span>
                      </div>
                      <span className="text-xs text-slate-400 font-mono-numbers">
                        {inputText.length} chars
                      </span>
                    </div>

                    <div className="relative">
                      <textarea
                        rows={6}
                        value={inputText}
                        onChange={(e) => setInputText(e.target.value)}
                        placeholder="Paste suspicious SMS, WhatsApp message, job offer, or loan pitch here... (English, हिन्दी or తెలుగు supported)"
                        className="w-full bg-[#0a1226]/90 border border-slate-700/80 rounded-2xl p-4 text-sm sm:text-base text-slate-100 placeholder-slate-500 focus:outline-none focus:border-cyan-500/70 focus:ring-2 focus:ring-cyan-500/20 transition resize-y font-sans leading-relaxed"
                      />
                      {inputText && (
                        <button
                          onClick={() => setInputText("")}
                          className="absolute top-3 right-3 p-1.5 rounded-lg bg-slate-800 text-slate-400 hover:text-white"
                          title="Clear message"
                        >
                          <Icon name="X" className="w-4 h-4" />
                        </button>
                      )}
                    </div>

                    <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
                      <button
                        type="button"
                        onClick={async () => {
                          try {
                            const clip = await navigator.clipboard.readText();
                            if (clip) { setInputText(clip); showToast("Pasted from clipboard!", "success"); }
                          } catch(e) { showToast("Clipboard permission required.", "info"); }
                        }}
                        className="px-4 py-2.5 rounded-xl bg-slate-900 border border-slate-700 text-xs font-semibold text-slate-300 hover:text-white transition flex items-center gap-1.5 w-full sm:w-auto"
                      >
                        <Icon name="Copy" className="w-3.5 h-3.5" />
                        <span>Paste from Clipboard</span>
                      </button>

                      <button
                        type="button"
                        onClick={() => handleAnalyze(inputText, "text")}
                        disabled={!inputText.trim()}
                        className={`w-full sm:w-auto px-8 py-3 rounded-2xl font-bold text-sm tracking-wide flex items-center justify-center gap-2 transition duration-300 shadow-xl ${
                          inputText.trim()
                            ? "bg-gradient-to-r from-cyan-500 via-blue-600 to-indigo-600 text-white shadow-cyan-500/25 hover:shadow-cyan-500/40 hover:scale-[1.02] cursor-pointer"
                            : "bg-slate-800 text-slate-500 cursor-not-allowed border border-slate-700/50"
                        }`}
                      >
                        <Icon name="ShieldAlert" className="w-4 h-4" />
                        <span>Analyze Message Now</span>
                      </button>
                    </div>
                  </div>
                )}

                {/* SUB-TAB 2: SCREENSHOT OCR SCANNER */}
                {scannerSubTab === "screenshot" && (
                  <div className="max-w-3xl mx-auto glass-panel-elevated rounded-3xl p-6 sm:p-8 space-y-6">
                    <div>
                      <h3 className="text-base font-bold text-white flex items-center gap-2">
                        <Icon name="Image" className="w-5 h-5 text-cyan-400" />
                        <span>Screenshot OCR Optical Reader</span>
                      </h3>
                      <p className="text-xs text-slate-400 mt-1">
                        Upload JPG, PNG, or JPEG screenshots of SMS, WhatsApp, or email. Tesseract.js will extract the text automatically.
                      </p>
                    </div>

                    {!screenshotPreview ? (
                      <div
                        onClick={() => fileInputRef.current?.click()}
                        className="border-2 border-dashed border-slate-700/80 hover:border-cyan-500/60 rounded-2xl p-8 sm:p-12 text-center cursor-pointer transition duration-300 bg-slate-900/40 hover:bg-cyan-500/5 group"
                      >
                        <input
                          ref={fileInputRef}
                          type="file"
                          accept="image/png, image/jpeg, image/jpg"
                          onChange={handleScreenshotUpload}
                          className="hidden"
                        />
                        <div className="w-16 h-16 rounded-2xl bg-slate-800/80 group-hover:bg-cyan-500/10 border border-slate-700 group-hover:border-cyan-500/40 flex items-center justify-center mx-auto mb-4 transition duration-300">
                          <Icon name="UploadCloud" className="w-8 h-8 text-cyan-400 group-hover:scale-110 transition duration-300" />
                        </div>
                        <p className="text-sm font-semibold text-white">Click to browse or drag & drop screenshot</p>
                        <p className="text-xs text-slate-400 mt-1">Supports JPG, PNG, JPEG screenshots</p>
                      </div>
                    ) : (
                      <div className="space-y-4">
                        <div className="relative rounded-2xl overflow-hidden border border-slate-700 max-h-72 bg-black/50 flex items-center justify-center">
                          <img src={screenshotPreview} alt="Screenshot" className="max-h-72 object-contain" />
                          <button
                            onClick={() => { setScreenshotPreview(null); setExtractedOcrText(""); }}
                            className="absolute top-3 right-3 px-3 py-1.5 rounded-xl bg-slate-950/80 border border-slate-700 text-xs font-semibold text-slate-300 hover:text-white hover:bg-red-500/20 transition flex items-center gap-1"
                          >
                            <Icon name="Trash2" className="w-3.5 h-3.5 text-red-400" />
                            <span>Remove</span>
                          </button>
                        </div>

                        {isOcrRunning && (
                          <div className="p-4 rounded-2xl bg-cyan-950/30 border border-cyan-500/30 space-y-2">
                            <div className="flex items-center justify-between text-xs text-cyan-300 font-semibold">
                              <span className="flex items-center gap-2">
                                <Icon name="RefreshCw" className="w-3.5 h-3.5 animate-spin text-cyan-400" />
                                {ocrProgress.status}
                              </span>
                              <span className="font-mono-numbers">{ocrProgress.progress}%</span>
                            </div>
                            <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                              <div className="bg-gradient-to-r from-cyan-500 to-blue-500 h-full transition-all duration-300" style={{ width: `${ocrProgress.progress}%` }} />
                            </div>
                          </div>
                        )}

                        {!isOcrRunning && extractedOcrText && (
                          <div className="space-y-3">
                            <label className="text-xs font-bold text-slate-300 flex items-center gap-1.5">
                              <Icon name="CheckCircle" className="w-4 h-4 text-emerald-400" />
                              <span>Extracted Text from Screenshot (Editable):</span>
                            </label>
                            <textarea
                              rows={4}
                              value={extractedOcrText}
                              onChange={(e) => setExtractedOcrText(e.target.value)}
                              className="w-full bg-[#0a1226]/90 border border-slate-700 rounded-xl p-3 text-sm text-slate-200 focus:outline-none focus:border-cyan-500 transition font-sans"
                            />
                            <button
                              type="button"
                              onClick={() => handleAnalyze(extractedOcrText, "screenshot")}
                              disabled={!extractedOcrText.trim()}
                              className="w-full py-3 rounded-2xl bg-gradient-to-r from-cyan-500 via-blue-600 to-indigo-600 text-white font-bold text-sm tracking-wide flex items-center justify-center gap-2 shadow-lg shadow-cyan-500/25 hover:shadow-cyan-500/40 transition"
                            >
                              <Icon name="ShieldAlert" className="w-4 h-4" />
                              <span>Analyze Extracted Message</span>
                            </button>
                          </div>
                        )}
                      </div>
                    )}
                  </div>
                )}

                {/* SUB-TAB 3: WEB LINK / URL SCANNER */}
                {scannerSubTab === "url" && (
                  <div className="max-w-3xl mx-auto glass-panel-elevated rounded-3xl p-6 sm:p-8 space-y-6">
                    <div>
                      <h3 className="text-base font-bold text-white flex items-center gap-2">
                        <Icon name="Link2" className="w-5 h-5 text-cyan-400" />
                        <span>Direct Web Link & Domain Threat Intelligence</span>
                      </h3>
                      <p className="text-xs text-slate-400 mt-1">
                        Audits protocol encryption, domain typosquatting, lookalike banks, shortened URLs, and dangerous TLDs.
                      </p>
                    </div>

                    <div className="relative">
                      <input
                        type="url"
                        value={inputUrl}
                        onChange={(e) => setInputUrl(e.target.value)}
                        placeholder="Enter URL (e.g. http://sbi-kyc-verify.xyz/login or https://bit.ly/...)"
                        className="w-full bg-[#0a1226]/90 border border-slate-700/80 rounded-2xl p-4 text-sm sm:text-base text-slate-100 placeholder-slate-500 focus:outline-none focus:border-cyan-500 font-mono"
                      />
                    </div>

                    <div className="flex flex-wrap gap-2">
                      <button
                        type="button"
                        onClick={() => setInputUrl("http://sbi-kyc-verify.xyz/login?otp=pending")}
                        className="px-3 py-1.5 rounded-xl bg-red-500/10 border border-red-500/30 text-red-300 text-xs font-mono hover:bg-red-500/20"
                      >
                        🔴 sbi-kyc-verify.xyz (Phishing)
                      </button>
                      <button
                        type="button"
                        onClick={() => setInputUrl("https://bit.ly/claim-25lakh-prize")}
                        className="px-3 py-1.5 rounded-xl bg-amber-500/10 border border-amber-500/30 text-amber-300 text-xs font-mono hover:bg-amber-500/20"
                      >
                        🟡 bit.ly/claim-prize (Shortened)
                      </button>
                      <button
                        type="button"
                        onClick={() => setInputUrl("https://www.onlinesbi.sbi/")}
                        className="px-3 py-1.5 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-xs font-mono hover:bg-emerald-500/20"
                      >
                        🟢 onlinesbi.sbi (Official)
                      </button>
                    </div>

                    <div className="flex justify-end pt-2">
                      <button
                        type="button"
                        onClick={() => handleAnalyze(inputUrl, "url")}
                        disabled={!inputUrl.trim()}
                        className="px-8 py-3 rounded-2xl bg-gradient-to-r from-cyan-500 via-blue-600 to-indigo-600 text-white font-bold text-sm tracking-wide flex items-center gap-2 shadow-xl hover:scale-[1.02] transition"
                      >
                        <Icon name="Link2" className="w-4 h-4" />
                        <span>Audit Web Link</span>
                      </button>
                    </div>
                  </div>
                )}

                {/* SUB-TAB 4: EMAIL PHISHING SCANNER */}
                {scannerSubTab === "email" && (
                  <div className="max-w-3xl mx-auto glass-panel-elevated rounded-3xl p-6 sm:p-8 space-y-6">
                    <div>
                      <h3 className="text-base font-bold text-white flex items-center gap-2">
                        <Icon name="Mail" className="w-5 h-5 text-cyan-400" />
                        <span>Email Phishing & Header Analyzer</span>
                      </h3>
                      <p className="text-xs text-slate-400 mt-1">
                        Paste the full email body or headers (From, Subject, Body) to detect address spoofing, fake IT department refunds, and urgent credentials verification links.
                      </p>
                    </div>

                    <textarea
                      rows={6}
                      value={inputEmail}
                      onChange={(e) => setInputEmail(e.target.value)}
                      placeholder="Paste email text or headers here... (e.g. From: support@incometax-refund.support Subject: Urgent Refund Approved...)"
                      className="w-full bg-[#0a1226]/90 border border-slate-700/80 rounded-2xl p-4 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-cyan-500 font-mono"
                    />

                    <div className="flex justify-end pt-2">
                      <button
                        type="button"
                        onClick={() => handleAnalyze(inputEmail, "email")}
                        disabled={!inputEmail.trim()}
                        className="px-8 py-3 rounded-2xl bg-gradient-to-r from-cyan-500 via-blue-600 to-indigo-600 text-white font-bold text-sm tracking-wide flex items-center gap-2 shadow-xl hover:scale-[1.02] transition"
                      >
                        <Icon name="Mail" className="w-4 h-4" />
                        <span>Analyze Phishing Email</span>
                      </button>
                    </div>
                  </div>
                )}

                {/* SUB-TAB 5: UPI QR CODE SCANNER */}
                {scannerSubTab === "qr" && (
                  <div className="max-w-3xl mx-auto glass-panel-elevated rounded-3xl p-6 sm:p-8 space-y-6">
                    <div>
                      <h3 className="text-base font-bold text-white flex items-center gap-2">
                        <Icon name="QrCode" className="w-5 h-5 text-cyan-400" />
                        <span>UPI Payment & QR Intent Analyzer</span>
                      </h3>
                      <p className="text-xs text-slate-400 mt-1">
                        Paste a UPI payment link (e.g. upi://pay?pa=...) to check whether it executes a DEBIT transaction and inspect payee authenticity.
                      </p>
                    </div>

                    <input
                      type="text"
                      value={inputQr}
                      onChange={(e) => setInputQr(e.target.value)}
                      placeholder="upi://pay?pa=merchant@upi&pn=Store&am=100"
                      className="w-full bg-[#0a1226]/90 border border-slate-700/80 rounded-2xl p-4 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-cyan-500 font-mono"
                    />

                    <div className="p-3.5 rounded-xl bg-amber-950/30 border border-amber-500/30 text-xs text-amber-200 space-y-1">
                      <span className="font-bold">⚠️ Golden UPI Rule:</span>
                      <p>Entering your UPI PIN or scanning a QR code is strictly for SENDING (debiting) money. You NEVER need to enter your PIN or scan a QR code to RECEIVE money.</p>
                    </div>

                    <div className="flex justify-end pt-2">
                      <button
                        type="button"
                        onClick={() => handleAnalyze(inputQr, "qr")}
                        disabled={!inputQr.trim()}
                        className="px-8 py-3 rounded-2xl bg-gradient-to-r from-cyan-500 via-blue-600 to-indigo-600 text-white font-bold text-sm tracking-wide flex items-center gap-2 shadow-xl hover:scale-[1.02] transition"
                      >
                        <Icon name="QrCode" className="w-4 h-4" />
                        <span>Inspect UPI QR Payload</span>
                      </button>
                    </div>
                  </div>
                )}
              </div>
            )}

            {/* RADAR SCANNING ANIMATION STATE */}
            {appState === "scanning" && (
              <div className="max-w-xl mx-auto glass-panel-elevated rounded-3xl p-8 sm:p-12 text-center space-y-8 animate-fadeIn">
                <div className="relative w-48 h-48 mx-auto flex items-center justify-center">
                  <div className="absolute inset-0 rounded-full border border-cyan-500/20 pulse-glow"></div>
                  <div className="absolute inset-4 rounded-full border border-cyan-500/30"></div>
                  <div className="absolute inset-10 rounded-full border border-cyan-500/40"></div>
                  <div className="absolute inset-16 rounded-full border border-cyan-500/50"></div>
                  <div className="absolute inset-0 radar-sweep">
                    <div className="w-1/2 h-1/2 bg-gradient-to-br from-cyan-400/30 to-transparent rounded-tl-full origin-bottom-right"></div>
                  </div>
                  <div className="relative z-10 w-16 h-16 rounded-2xl bg-[#070d1b] border-2 border-cyan-400 flex items-center justify-center shadow-lg shadow-cyan-500/40">
                    <Icon name="ShieldAlert" className="w-8 h-8 text-cyan-400 animate-pulse" />
                  </div>
                </div>

                <div className="space-y-3">
                  <h3 className="text-xl font-extrabold text-white tracking-tight">
                    Running Multi-Vector Security Assessment...
                  </h3>
                  <p className="text-xs sm:text-sm text-cyan-300/80 max-w-sm mx-auto">
                    Evaluating multilingual panic triggers, credential theft traps, domain reputation, and statutory legal provisions.
                  </p>
                </div>
              </div>
            )}

            {/* REPORT RESULT STATE */}
            {appState === "report" && analysisResult && (
              <div className="max-w-4xl mx-auto space-y-8 animate-fadeIn">
                {/* Header Controls */}
                <div className="flex items-center justify-between">
                  <button
                    onClick={() => { setAppState("idle"); setAnalysisResult(null); }}
                    className="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-slate-900 border border-slate-700 text-xs font-semibold text-slate-300 hover:text-white transition"
                  >
                    <Icon name="ArrowRight" className="w-4 h-4 rotate-180" />
                    <span>Scan Another Content</span>
                  </button>

                  <div className="flex items-center gap-2">
                    <button
                      onClick={handleCopyAdvice}
                      className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-cyan-500/10 border border-cyan-500/30 text-xs font-semibold text-cyan-300 hover:bg-cyan-500/20 transition"
                    >
                      <Icon name="Copy" className="w-3.5 h-3.5" />
                      <span>Copy Safe Advice</span>
                    </button>
                    <button
                      onClick={() => {
                        setEvidenceTitle(`${analysisResult.scamType} - Scan Evidence`);
                        setEvidenceType(analysisResult.scamType);
                        setEvidenceDesc(analysisResult.explanation);
                        setActiveTab("evidence");
                        window.scrollTo({ top: 100, behavior: "smooth" });
                        showToast("Loaded scan data into Evidence Vault!", "success");
                      }}
                      className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-xs font-semibold text-emerald-300 hover:bg-emerald-500/20 transition"
                    >
                      <Icon name="Lock" className="w-3.5 h-3.5" />
                      <span>Preserve in Evidence Vault</span>
                    </button>
                  </div>
                </div>

                {/* Primary Risk Banner */}
                <div className={`rounded-3xl p-6 sm:p-8 border transition-all duration-300 ${
                  analysisResult.riskLevel === "HIGH-RISK SCAM"
                    ? "glass-panel-danger"
                    : analysisResult.riskLevel === "SUSPICIOUS"
                    ? "glass-panel-warning"
                    : "glass-panel-safe"
                }`}>
                  <div className="flex flex-col md:flex-row items-center justify-between gap-6 text-center md:text-left">
                    <div className="space-y-3 flex-1">
                      <div className="flex flex-wrap items-center justify-center md:justify-start gap-2.5">
                        <span className={`text-xs font-extrabold px-3.5 py-1 rounded-full uppercase tracking-wider font-mono ${
                          analysisResult.riskLevel === "HIGH-RISK SCAM"
                            ? "bg-red-500 text-white shadow-lg shadow-red-500/40 animate-pulse"
                            : analysisResult.riskLevel === "SUSPICIOUS"
                            ? "bg-amber-500 text-black shadow-lg shadow-amber-500/40 font-bold"
                            : "bg-emerald-500 text-black shadow-lg shadow-emerald-500/40 font-bold"
                        }`}>
                          {analysisResult.riskLevel}
                        </span>

                        <span className="text-[11px] px-2.5 py-0.5 rounded-full bg-slate-900/80 border border-slate-700 text-slate-300 font-mono">
                          Confidence: {Math.round((analysisResult.confidenceScore || 0.92) * 100)}%
                        </span>

                        <span className="text-[11px] px-2.5 py-0.5 rounded-full bg-slate-900/80 border border-slate-700 text-slate-300 font-mono uppercase">
                          Language: {analysisResult.language}
                        </span>
                      </div>

                      <h2 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
                        {analysisResult.scamType}
                      </h2>

                      <p className="text-xs sm:text-sm text-slate-200 leading-relaxed max-w-xl">
                        {analysisResult.explanation}
                      </p>
                    </div>

                    {/* Circular Score Gauge */}
                    <div className="flex flex-col items-center justify-center shrink-0">
                      <div className="relative w-36 h-36 flex items-center justify-center">
                        <svg className="w-36 h-36 transform -rotate-90" viewBox="0 0 120 120">
                          <circle cx="60" cy="60" r="50" stroke="rgba(255,255,255,0.1)" strokeWidth="10" fill="transparent" />
                          <circle
                            cx="60" cy="60" r="50"
                            stroke={
                              analysisResult.riskLevel === "HIGH-RISK SCAM" ? "#ef4444" : analysisResult.riskLevel === "SUSPICIOUS" ? "#f59e0b" : "#10b981"
                            }
                            strokeWidth="10"
                            strokeDasharray={2 * Math.PI * 50}
                            strokeDashoffset={2 * Math.PI * 50 * (1 - analysisResult.riskScore / 100)}
                            strokeLinecap="round"
                            fill="transparent"
                            className="transition-all duration-1000 ease-out"
                          />
                        </svg>
                        <div className="absolute inset-0 flex flex-col items-center justify-center">
                          <span className="text-3xl font-extrabold font-mono-numbers text-white tracking-tight">
                            {analysisResult.riskScore}
                          </span>
                          <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400">
                            Risk Score
                          </span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                {/* Highlighted Message Inspector */}
                <div className="glass-panel-elevated rounded-3xl p-6 sm:p-8 space-y-4">
                  <div className="flex items-center justify-between border-b border-slate-800 pb-3">
                    <h3 className="text-sm font-bold text-white flex items-center gap-2">
                      <Icon name="AlertTriangle" className="w-4 h-4 text-cyan-400" />
                      <span>Inspected Content (Threat Markers Highlighted)</span>
                    </h3>
                    <span className="text-xs text-slate-400 font-mono">
                      {analysisResult.highlightedPhrases?.length || 0} trigger word(s)
                    </span>
                  </div>

                  <div className="p-5 rounded-2xl bg-[#091124] border border-slate-800 text-sm text-slate-200 leading-relaxed font-sans">
                    {(() => {
                      const text = analysisResult.analyzedText || "";
                      const phrases = analysisResult.highlightedPhrases || [];
                      if (phrases.length === 0) return <span>{text}</span>;

                      try {
                        const escaped = phrases.map(p => p.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"));
                        const regex = new RegExp(`(${escaped.join("|")})`, "gi");
                        const parts = text.split(regex);

                        return parts.map((part, idx) => {
                          const isMatch = phrases.some(p => p.toLowerCase() === part.toLowerCase());
                          if (isMatch) {
                            return (
                              <mark
                                key={idx}
                                className={analysisResult.riskLevel === "HIGH-RISK SCAM" ? "scam-highlight" : "suspicious-highlight"}
                              >
                                {part}
                              </mark>
                            );
                          }
                          return <span key={idx}>{part}</span>;
                        });
                      } catch(e) {
                        return <span>{text}</span>;
                      }
                    })()}
                  </div>
                </div>

                {/* Detected Warning Indicators */}
                {analysisResult.indicators && analysisResult.indicators.length > 0 && (
                  <div className="glass-panel-elevated rounded-3xl p-6 sm:p-8 space-y-4">
                    <h3 className="text-sm font-bold text-white flex items-center gap-2 border-b border-slate-800 pb-3">
                      <Icon name="AlertOctagon" className="w-4 h-4 text-red-400" />
                      <span>Identified Scam Warning Signs ({analysisResult.indicators.length})</span>
                    </h3>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                      {analysisResult.indicators.map((ind, i) => (
                        <div key={i} className="p-4 rounded-2xl bg-slate-900/90 border border-slate-800 space-y-2">
                          <div className="flex items-center justify-between gap-2">
                            <span className="text-xs font-bold text-white">{ind.name}</span>
                            <span className={`text-[9px] font-mono px-2 py-0.5 rounded-full font-bold uppercase ${
                              ind.severity === "CRITICAL" ? "bg-red-500/20 text-red-300 border border-red-500/30" : "bg-amber-500/20 text-amber-300 border border-amber-500/30"
                            }`}>
                              {ind.severity}
                            </span>
                          </div>
                          <p className="text-xs text-slate-400 leading-relaxed font-sans">{ind.description}</p>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* MAPPED INDIAN CYBER LAWS */}
                {analysisResult.legalSections && analysisResult.legalSections.length > 0 && (
                  <div className="glass-panel-elevated rounded-3xl p-6 sm:p-8 space-y-4">
                    <div className="flex items-center justify-between border-b border-slate-800 pb-3">
                      <h3 className="text-sm font-bold text-white flex items-center gap-2">
                        <Icon name="Scale" className="w-4 h-4 text-cyan-400" />
                        <span>Applicable Indian Legal Provisions (IT Act 2000 & BNS 2023)</span>
                      </h3>
                      <button
                        onClick={() => { setActiveTab("laws"); window.scrollTo({ top: 100, behavior: "smooth" }); }}
                        className="text-xs text-cyan-300 hover:underline flex items-center gap-1 font-semibold"
                      >
                        <span>Full Law Directory</span>
                        <Icon name="ArrowRight" className="w-3 h-3" />
                      </button>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                      {analysisResult.legalSections.map((law, idx) => (
                        <div key={idx} className="p-4 rounded-2xl bg-slate-900/80 border border-slate-800 space-y-2">
                          <div className="flex items-center justify-between">
                            <span className="text-xs font-bold text-cyan-300">{law.section}</span>
                            <span className="text-[10px] text-slate-400 font-mono">{law.act}</span>
                          </div>
                          <h4 className="text-xs font-bold text-white">{law.title}</h4>
                          <p className="text-xs text-slate-300 leading-relaxed">{law.simpleExplanation}</p>
                          <div className="pt-1 text-[11px] text-red-300 font-mono">
                            <strong>Penalty:</strong> {law.penalty}
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* RECOMMENDED OFFICIAL GOV SERVICES */}
                {analysisResult.govServices && analysisResult.govServices.length > 0 && (
                  <div className="glass-panel-elevated rounded-3xl p-6 sm:p-8 space-y-4">
                    <div className="flex items-center justify-between border-b border-slate-800 pb-3">
                      <h3 className="text-sm font-bold text-white flex items-center gap-2">
                        <Icon name="Building" className="w-4 h-4 text-emerald-400" />
                        <span>Recommended Official Government Services</span>
                      </h3>
                      <button
                        onClick={() => { setActiveTab("gov"); window.scrollTo({ top: 100, behavior: "smooth" }); }}
                        className="text-xs text-emerald-300 hover:underline flex items-center gap-1 font-semibold"
                      >
                        <span>View All Services</span>
                        <Icon name="ArrowRight" className="w-3 h-3" />
                      </button>
                    </div>

                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                      {analysisResult.govServices.map((srv, idx) => (
                        <div key={idx} className="p-4 rounded-2xl bg-slate-900/80 border border-slate-800 flex flex-col justify-between space-y-3">
                          <div className="space-y-1">
                            <div className="flex items-center justify-between">
                              <span className="text-xs font-bold text-white">{srv.serviceName}</span>
                              {srv.isEmergency && (
                                <span className="text-[9px] px-2 py-0.5 rounded-full bg-red-500/20 text-red-300 border border-red-500/40 font-bold uppercase">
                                  24x7 Helpline
                                </span>
                              )}
                            </div>
                            <p className="text-[11px] text-cyan-300">{srv.responsibleDept}</p>
                            <p className="text-xs text-slate-400 leading-relaxed">{srv.whatItDoes.slice(0, 140)}...</p>
                          </div>
                          <a
                            href={srv.officialUrl}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="inline-flex items-center justify-center gap-1.5 px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-white transition"
                          >
                            <span>Open Official Portal</span>
                            <Icon name="ExternalLink" className="w-3 h-3" />
                          </a>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            )}
          </div>
        )}

        {/* ========================================================
            TAB 2: REAL-WORLD CYBERCRIME ACTION CENTER
        ======================================================== */}
        {activeTab === "actions" && (
          <div className="max-w-5xl mx-auto space-y-8 animate-fadeIn">
            <div className="text-center space-y-2">
              <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-xs font-semibold">
                <Icon name="Zap" className="w-3.5 h-3.5" />
                <span>RAPID INCIDENT RESPONSE PLAYBOOKS</span>
              </div>
              <h2 className="text-3xl font-extrabold text-white">
                Real-World Cybercrime Action Center
              </h2>
              <p className="text-xs sm:text-sm text-slate-400 max-w-2xl mx-auto">
                Step-by-step containment procedures and reporting protocols for the most dangerous digital attacks in India.
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {[
                {
                  title: "1. Bank Phishing & OTP Compromise",
                  desc: "When debit card, netbanking password, or OTP was shared or siphoned.",
                  steps: [
                    "Call bank's 24x7 emergency helpline or use mobile app to freeze debit/credit cards immediately.",
                    "Change your netbanking login password and UPI MPIN from an uncompromised device.",
                    "Dial 1930 within the 2-Hour Golden Window with transaction UTR numbers to hold funds.",
                    "Lodge formal complaint at cybercrime.gov.in."
                  ],
                  laws: "IT Act Sec 66C (Identity Theft) & Sec 66D (Cheating by Personation)"
                },
                {
                  title: "2. Fake Work-From-Home & YouTube Review Scams",
                  desc: "When trapped in 'VIP Tasks' demanding deposits to withdraw salary.",
                  steps: [
                    "Stop depositing money immediately. Never pay 'tax clearance' or 'VIP unlock fees'.",
                    "Export full WhatsApp and Telegram chats with recruiter handles and UPI IDs.",
                    "Report phone numbers to Sanchar Saathi Chakshu (sancharsaathi.gov.in/sfc/).",
                    "Lodge financial cybercrime complaint at cybercrime.gov.in with bank transaction proofs."
                  ],
                  laws: "BNS Section 318(4) (Cheating & Property Inducement) & IT Act Sec 66D"
                },
                {
                  title: "3. Predatory Loan Apps & Harassment",
                  desc: "When illegal loan apps extort money or threaten to leak photo gallery/contacts.",
                  steps: [
                    "Immediately revoke camera, contacts, and storage permissions in Android Settings.",
                    "Check whether the app is on the RBI Sachet Registered NBFC list (sachet.rbi.org.in).",
                    "Do NOT transfer extortionate weekly interest to personal UPI accounts.",
                    "File formal extortion complaint under BNS Section 351 at local cyber police station."
                  ],
                  laws: "IT Act Sec 43 (Unauthorized Access), Sec 66E (Privacy), BNS Sec 351 (Extortion)"
                },
                {
                  title: "4. Digital Arrest & Police Extortion",
                  desc: "When scammers pose as CBI, Police, or Customs over Skype video calls.",
                  steps: [
                    "Recognize that 'Digital Arrest' DOES NOT EXIST in Indian criminal law.",
                    "Hang up the call immediately. Police never conduct video trials or demand escrow payments.",
                    "Never transfer funds to 'safe verification accounts'.",
                    "Report the caller's Skype/WhatsApp ID to 1930 and cybercrime.gov.in."
                  ],
                  laws: "BNS Section 336/338 (Forgery), Section 351 (Extortion), IT Act Sec 66D"
                }
              ].map((pb, i) => (
                <div key={i} className="p-6 rounded-3xl glass-panel-elevated border border-slate-800 space-y-4">
                  <div className="space-y-1">
                    <h3 className="text-base font-bold text-white flex items-center gap-2">
                      <Icon name="ShieldAlert" className="w-5 h-5 text-cyan-400" />
                      <span>{pb.title}</span>
                    </h3>
                    <p className="text-xs text-slate-400">{pb.desc}</p>
                  </div>

                  <div className="space-y-2">
                    <span className="text-[11px] font-bold text-cyan-300 uppercase tracking-wider">Emergency Steps:</span>
                    <ol className="space-y-2 text-xs text-slate-300">
                      {pb.steps.map((st, idx) => (
                        <li key={idx} className="flex items-start gap-2">
                          <span className="w-4 h-4 rounded-full bg-cyan-500/20 text-cyan-300 flex items-center justify-center font-mono text-[10px] shrink-0 mt-0.5">
                            {idx + 1}
                          </span>
                          <span className="leading-relaxed">{st}</span>
                        </li>
                      ))}
                    </ol>
                  </div>

                  <div className="p-3 rounded-xl bg-slate-900/90 border border-slate-800 text-[11px] text-slate-400 font-mono">
                    <strong>Applicable Law:</strong> {pb.laws}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* ========================================================
            TAB 3: GOVERNMENT SERVICES DIRECTORY
        ======================================================== */}
        {activeTab === "gov" && (
          <div className="max-w-5xl mx-auto space-y-8 animate-fadeIn">
            <div className="text-center space-y-2">
              <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-xs font-semibold">
                <Icon name="Building" className="w-3.5 h-3.5" />
                <span>OFFICIAL INDIAN CYBERCRIME SERVICES</span>
              </div>
              <h2 className="text-3xl font-extrabold text-white">
                Government Services & Reporting Center
              </h2>
              <p className="text-xs sm:text-sm text-slate-400 max-w-2xl mx-auto">
                Verified official portals, helplines, and step-by-step reporting instructions. Every link is verified.
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {govServices.map((srv) => (
                <div key={srv.id} className="p-6 rounded-3xl glass-panel-elevated border border-slate-800 space-y-4 flex flex-col justify-between">
                  <div className="space-y-3">
                    <div className="flex items-start justify-between gap-2">
                      <div>
                        <h3 className="text-base font-bold text-white">{srv.serviceName}</h3>
                        <p className="text-xs text-cyan-300 mt-0.5">{srv.responsibleDept}</p>
                      </div>
                      <span className="text-[10px] px-2.5 py-0.5 rounded-full bg-slate-900 border border-slate-700 text-slate-400 font-mono">
                        {srv.category}
                      </span>
                    </div>

                    <p className="text-xs text-slate-300 leading-relaxed">{srv.whatItDoes}</p>

                    <div className="space-y-1">
                      <span className="text-[11px] font-bold text-slate-300">When to use:</span>
                      <p className="text-xs text-slate-400">{srv.whenToUse}</p>
                    </div>

                    <div className="space-y-1.5">
                      <span className="text-[11px] font-bold text-emerald-400">Step-by-step procedure:</span>
                      <ol className="space-y-1 text-xs text-slate-300">
                        {(srv.stepByStepInstructions || []).slice(0, 3).map((st, i) => (
                          <li key={i} className="flex items-start gap-2">
                            <span className="font-mono text-cyan-400 text-[11px]">{i+1}.</span>
                            <span>{st}</span>
                          </li>
                        ))}
                      </ol>
                    </div>
                  </div>

                  <div className="pt-3 border-t border-slate-800 flex items-center justify-between">
                    <span className="text-[10px] text-slate-500 font-mono">Verified: {srv.lastVerified}</span>
                    <a
                      href={srv.officialUrl}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-[#070d1b] font-bold text-xs transition"
                    >
                      <span>Open Official Portal</span>
                      <Icon name="ExternalLink" className="w-3.5 h-3.5" />
                    </a>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* ========================================================
            TAB 4: INDIAN CYBER LAWS & LEGAL RIGHTS
        ======================================================== */}
        {activeTab === "laws" && (
          <div className="max-w-5xl mx-auto space-y-8 animate-fadeIn">
            <div className="text-center space-y-2">
              <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-xs font-semibold">
                <Icon name="Scale" className="w-3.5 h-3.5" />
                <span>STATUTORY CYBERCRIME FRAMEWORK</span>
              </div>
              <h2 className="text-3xl font-extrabold text-white">
                Indian Cyber Laws & Legal Rights Center
              </h2>
              <p className="text-xs sm:text-sm text-slate-400 max-w-2xl mx-auto">
                Authoritative provisions of the Information Technology Act, 2000 and the Bharatiya Nyaya Sanhita, 2023.
              </p>
            </div>

            {/* Disclaimer */}
            <div className="p-4 rounded-2xl bg-slate-900 border border-slate-800 text-xs text-slate-400 leading-relaxed">
              <strong>Notice:</strong> This repository provides general educational information regarding Indian criminal law and digital rights. It does not constitute formal legal counsel. Source: <a href="https://www.indiacode.nic.in" target="_blank" className="text-cyan-400 underline">India Code (indiacode.nic.in)</a>.
            </div>

            {/* Search Input */}
            <div className="relative max-w-md mx-auto">
              <input
                type="text"
                value={lawSearch}
                onChange={(e) => setLawSearch(e.target.value)}
                placeholder="Search legal sections (e.g. 66D, identity theft, cheating)..."
                className="w-full bg-[#0a1226] border border-slate-700 rounded-xl px-4 py-2.5 text-xs text-white focus:outline-none focus:border-cyan-500 font-mono"
              />
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {filteredLaws.map((law) => (
                <div key={law.id} className="p-6 rounded-3xl glass-panel-elevated border border-slate-800 space-y-3 flex flex-col justify-between">
                  <div className="space-y-2">
                    <div className="flex items-center justify-between">
                      <span className="text-sm font-extrabold text-cyan-300 font-mono">{law.section}</span>
                      <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-800 text-slate-400">{law.act}</span>
                    </div>
                    <h3 className="text-sm font-bold text-white">{law.title}</h3>
                    <p className="text-xs text-slate-300 leading-relaxed">{law.simpleExplanation}</p>

                    <div className="p-3 rounded-xl bg-slate-900/80 border border-slate-800 text-[11px] text-slate-400 space-y-1">
                      <strong className="text-slate-300">Educational Scenario:</strong>
                      <p>"{law.educationalExample}"</p>
                    </div>

                    <div className="text-xs text-red-300 font-mono font-semibold">
                      <strong>Prescribed Penalty:</strong> {law.penalty}
                    </div>
                  </div>

                  <div className="pt-3 border-t border-slate-800 flex items-center justify-between">
                    <span className="text-[11px] text-slate-500">Official Statute</span>
                    <a
                      href={law.officialSource}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-xs text-cyan-300 hover:underline flex items-center gap-1 font-semibold"
                    >
                      <span>Read on India Code</span>
                      <Icon name="ExternalLink" className="w-3 h-3" />
                    </a>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* ========================================================
            TAB 5: DIGITAL EVIDENCE VAULT
        ======================================================== */}
        {activeTab === "evidence" && (
          <div className="max-w-5xl mx-auto space-y-8 animate-fadeIn">
            <div className="text-center space-y-2">
              <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-xs font-semibold">
                <Icon name="Lock" className="w-3.5 h-3.5" />
                <span>SECURE EVIDENCE MANAGEMENT</span>
              </div>
              <h2 className="text-3xl font-extrabold text-white">
                Digital Evidence Vault & Incident Docket
              </h2>
              <p className="text-xs sm:text-sm text-slate-400 max-w-2xl mx-auto">
                Securely preserve SMS screenshots, bank transaction receipts, and WhatsApp chats with automatic sensitive PII redaction and printable police dockets.
              </p>
            </div>

            {/* Evidence Upload Form */}
            <div className="glass-panel-elevated rounded-3xl p-6 sm:p-8 space-y-6">
              <h3 className="text-base font-bold text-white flex items-center gap-2">
                <Icon name="UploadCloud" className="w-5 h-5 text-cyan-400" />
                <span>Record New Digital Evidence</span>
              </h3>

              <form onSubmit={handleEvidenceSubmit} className="space-y-4">
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <label className="block text-xs font-semibold text-slate-300 mb-1">Incident Title *</label>
                    <input
                      type="text"
                      required
                      value={evidenceTitle}
                      onChange={(e) => setEvidenceTitle(e.target.value)}
                      placeholder="e.g. SBI Phishing SMS & UPI Debit"
                      className="w-full bg-[#0a1226] border border-slate-700 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-cyan-500"
                    />
                  </div>

                  <div>
                    <label className="block text-xs font-semibold text-slate-300 mb-1">Incident Category</label>
                    <select
                      value={evidenceType}
                      onChange={(e) => setEvidenceType(e.target.value)}
                      className="w-full bg-[#0a1226] border border-slate-700 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-cyan-500"
                    >
                      <option>Bank Phishing & OTP Fraud</option>
                      <option>Work-from-Home Task Scam</option>
                      <option>Predatory Loan App Extortion</option>
                      <option>UPI / QR Payment Trap</option>
                      <option>Digital Arrest / Impersonation</option>
                      <option>Lottery / Prize Bait</option>
                      <option>Other Cybercrime</option>
                    </select>
                  </div>

                  <div>
                    <label className="block text-xs font-semibold text-slate-300 mb-1">Financial Loss Amount (₹)</label>
                    <input
                      type="number"
                      value={evidenceLoss}
                      onChange={(e) => setEvidenceLoss(e.target.value)}
                      placeholder="0.00"
                      className="w-full bg-[#0a1226] border border-slate-700 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-cyan-500 font-mono"
                    />
                  </div>

                  <div>
                    <label className="block text-xs font-semibold text-slate-300 mb-1">Transaction UTR / Ref Number</label>
                    <input
                      type="text"
                      value={evidenceUtr}
                      onChange={(e) => setEvidenceUtr(e.target.value)}
                      placeholder="e.g. UPI/432190876543 or IMPS"
                      className="w-full bg-[#0a1226] border border-slate-700 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-cyan-500 font-mono"
                    />
                  </div>
                </div>

                <div>
                  <label className="block text-xs font-semibold text-slate-300 mb-1">Suspect Details (Phone, UPI ID, Profile, Website)</label>
                  <input
                    type="text"
                    value={evidenceSuspect}
                    onChange={(e) => setEvidenceSuspect(e.target.value)}
                    placeholder="+91-9876543210, scammer@okhdfcbank, http://sbi-fake.xyz"
                    className="w-full bg-[#0a1226] border border-slate-700 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-cyan-500"
                  />
                </div>

                <div>
                  <label className="block text-xs font-semibold text-slate-300 mb-1">Incident Narrative & Description</label>
                  <textarea
                    rows={3}
                    value={evidenceDesc}
                    onChange={(e) => setEvidenceDesc(e.target.value)}
                    placeholder="Describe how the scam occurred, what was said, and what actions you took..."
                    className="w-full bg-[#0a1226] border border-slate-700 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-cyan-500 font-sans"
                  />
                </div>

                <div>
                  <label className="block text-xs font-semibold text-slate-300 mb-1">Upload File (JPG, PNG, PDF, TXT up to 10MB)</label>
                  <input
                    type="file"
                    accept=".jpg,.jpeg,.png,.pdf,.txt"
                    onChange={(e) => setEvidenceFile(e.target.files?.[0] || null)}
                    className="block w-full text-xs text-slate-400 file:mr-4 file:py-2 file:px-4 file:rounded-xl file:border-0 file:text-xs file:font-semibold file:bg-slate-800 file:text-cyan-300 hover:file:bg-slate-700"
                  />
                </div>

                <div className="pt-2 flex justify-end">
                  <button
                    type="submit"
                    disabled={isUploadingEvidence}
                    className="px-6 py-2.5 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 text-white font-bold text-xs tracking-wide shadow-lg shadow-cyan-500/20 transition flex items-center gap-2"
                  >
                    <Icon name="Lock" className="w-4 h-4" />
                    <span>{isUploadingEvidence ? "Processing..." : "Preserve in Vault"}</span>
                  </button>
                </div>
              </form>
            </div>

            {/* Preserved Evidence Records Table */}
            <div className="glass-panel-elevated rounded-3xl p-6 sm:p-8 space-y-4">
              <h3 className="text-base font-bold text-white flex items-center gap-2">
                <Icon name="FileText" className="w-5 h-5 text-emerald-400" />
                <span>Preserved Incident Dockets ({evidenceList.length})</span>
              </h3>

              {evidenceList.length === 0 ? (
                <p className="text-xs text-slate-500 py-6 text-center">No evidence records preserved yet.</p>
              ) : (
                <div className="space-y-3">
                  {evidenceList.map((ev) => (
                    <div key={ev.id} className="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                      <div className="space-y-1">
                        <div className="flex items-center gap-2">
                          <span className="text-xs font-bold text-white">{ev.incident_title}</span>
                          <span className="text-[10px] px-2 py-0.5 rounded bg-slate-800 text-cyan-300 font-mono">
                            {ev.incident_type}
                          </span>
                        </div>
                        <p className="text-[11px] text-slate-400">
                          Date: {ev.incident_date} | Loss: <span className="text-red-400 font-bold">₹{ev.financial_loss}</span> | UTR: {ev.transaction_utr || "N/A"}
                        </p>
                        {ev.redacted_text && (
                          <p className="text-[10px] text-slate-500 font-mono truncate max-w-md">
                            Redacted Text: {ev.redacted_text}
                          </p>
                        )}
                      </div>

                      <div className="flex items-center gap-2 shrink-0">
                        <a
                          href={`/api/evidence/${ev.id}/docket`}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="px-3 py-1.5 rounded-xl bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 hover:bg-cyan-500/20 text-xs font-semibold flex items-center gap-1.5 transition"
                        >
                          <Icon name="Printer" className="w-3.5 h-3.5" />
                          <span>Official Docket</span>
                        </a>

                        <button
                          onClick={async () => {
                            if (window.confirm("Delete this evidence record permanently?")) {
                              await fetch(`/api/evidence/${ev.id}`, { method: "DELETE" });
                              showToast("Evidence record deleted.", "info");
                              fetchEvidence();
                            }
                          }}
                          className="p-1.5 rounded-lg text-slate-500 hover:text-red-400 hover:bg-red-500/10 transition"
                        >
                          <Icon name="Trash2" className="w-4 h-4" />
                        </button>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>
        )}

        {/* ========================================================
            TAB 6: CYBER NEWS & VERIFIED ADVISORIES
        ======================================================== */}
        {activeTab === "advisories" && (
          <div className="max-w-5xl mx-auto space-y-8 animate-fadeIn">
            <div className="text-center space-y-2">
              <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-xs font-semibold">
                <Icon name="Newspaper" className="w-3.5 h-3.5" />
                <span>GENUINE OFFICIAL THREAT INTELLIGENCE</span>
              </div>
              <h2 className="text-3xl font-extrabold text-white">
                Cyber News & Verified Advisories
              </h2>
              <p className="text-xs sm:text-sm text-slate-400 max-w-2xl mx-auto">
                Real, published cybersecurity advisories from CERT-In, RBI, TRAI, and PIB Fact Check.
              </p>
            </div>

            {/* Filter & Search Bar */}
            <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
              <input
                type="text"
                value={advisorySearch}
                onChange={(e) => setAdvisorySearch(e.target.value)}
                placeholder="Search advisories (e.g. digital arrest, UPI, trojan)..."
                className="w-full sm:w-80 bg-[#0a1226] border border-slate-700 rounded-xl px-4 py-2 text-xs text-white focus:outline-none focus:border-cyan-500"
              />

              <div className="flex items-center bg-slate-900 border border-slate-800 p-1 rounded-xl text-xs font-semibold overflow-x-auto max-w-full">
                {["ALL", "Extortion", "UPI", "Malware", "Phishing", "Job"].map(cat => (
                  <button
                    key={cat}
                    onClick={() => setAdvisoryCat(cat)}
                    className={`px-3 py-1 rounded-lg transition ${
                      advisoryCat === cat ? "bg-cyan-500/20 text-cyan-300 font-bold" : "text-slate-400 hover:text-white"
                    }`}
                  >
                    {cat}
                  </button>
                ))}
              </div>
            </div>

            <div className="space-y-4">
              {filteredAdvisories.map((adv) => (
                <div key={adv.id} className="p-6 rounded-3xl glass-panel-elevated border border-slate-800 space-y-3">
                  <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                    <div className="flex items-center gap-2">
                      <span className={`text-[9px] font-mono px-2 py-0.5 rounded-full font-bold uppercase ${
                        adv.severity === "CRITICAL" ? "bg-red-500/20 text-red-300 border border-red-500/40" : "bg-amber-500/20 text-amber-300 border border-amber-500/40"
                      }`}>
                        {adv.severity}
                      </span>
                      <span className="text-xs text-cyan-300 font-semibold">{adv.source}</span>
                    </div>
                    <span className="text-[11px] text-slate-500 font-mono">Published: {adv.publishedDate}</span>
                  </div>

                  <h3 className="text-base font-bold text-white">{adv.title}</h3>
                  <p className="text-xs text-slate-300 leading-relaxed">{adv.summary}</p>

                  <div className="space-y-1 pt-1">
                    <span className="text-[11px] font-bold text-emerald-400">Official Safety Recommendations:</span>
                    <ul className="space-y-1 text-xs text-slate-400">
                      {(adv.actionableAdvice || []).map((step, i) => (
                        <li key={i} className="flex items-start gap-1.5">
                          <span className="text-cyan-400">✔</span>
                          <span>{step}</span>
                        </li>
                      ))}
                    </ul>
                  </div>

                  <div className="pt-2 text-right">
                    <a
                      href={adv.sourceUrl}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-xs text-cyan-300 hover:underline inline-flex items-center gap-1 font-semibold"
                    >
                      <span>Read Original Source Bulletin</span>
                      <Icon name="ExternalLink" className="w-3 h-3" />
                    </a>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* ========================================================
            TAB 7: AI CYBER SAFETY ASSISTANT (CONVERSATIONAL)
        ======================================================== */}
        {activeTab === "assistant" && (
          <div className="max-w-4xl mx-auto space-y-6 animate-fadeIn">
            <div className="text-center space-y-2">
              <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-xs font-semibold">
                <Icon name="Bot" className="w-3.5 h-3.5" />
                <span>INTERACTIVE MULTILINGUAL ADVISOR</span>
              </div>
              <h2 className="text-3xl font-extrabold text-white">
                ZERO CHILL AI Safety Assistant
              </h2>
              <p className="text-xs sm:text-sm text-slate-400 max-w-xl mx-auto">
                Ask questions about scam prevention, emergency 1930 procedures, and Indian Cyber Laws in English, हिन्दी, or తెలుగు.
              </p>
            </div>

            {/* Quick Prompt Chips */}
            <div className="flex flex-wrap items-center justify-center gap-2">
              {[
                "What is the 2-Hour Golden Window for 1930?",
                "What conduct does IT Act Section 66D cover?",
                "How does a Digital Arrest scam work?",
                "पैसे कट गए तो तुरंत क्या करें? (Hindi)",
                "డబ్బులు పోతే ఏం చేయాలి? (Telugu)"
              ].map((chip, idx) => (
                <button
                  key={idx}
                  onClick={() => { setChatInput(chip); }}
                  className="px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-700 text-[11px] text-slate-300 hover:text-white hover:border-cyan-500/40 transition"
                >
                  {chip}
                </button>
              ))}
            </div>

            {/* Chat Box Container */}
            <div className="glass-panel-elevated rounded-3xl p-6 sm:p-8 space-y-4 flex flex-col h-[520px]">
              <div className="flex-1 overflow-y-auto space-y-4 pr-2">
                {chatMessages.map((msg, i) => (
                  <div
                    key={i}
                    className={`flex items-start gap-3 ${msg.role === "user" ? "justify-end" : "justify-start"}`}
                  >
                    {msg.role !== "user" && (
                      <div className="w-8 h-8 rounded-xl bg-cyan-500/20 border border-cyan-500/40 flex items-center justify-center shrink-0">
                        <Icon name="Bot" className="w-4 h-4 text-cyan-400" />
                      </div>
                    )}
                    <div
                      className={`max-w-xl p-4 rounded-2xl text-xs sm:text-sm leading-relaxed whitespace-pre-wrap ${
                        msg.role === "user"
                          ? "bg-gradient-to-r from-cyan-600 to-blue-600 text-white rounded-tr-none font-medium"
                          : "bg-slate-900/90 border border-slate-800 text-slate-200 rounded-tl-none font-sans"
                      }`}
                    >
                      {msg.content}
                    </div>
                  </div>
                ))}
                {isChatThinking && (
                  <div className="flex items-center gap-2 text-xs text-cyan-300 font-mono">
                    <Icon name="RefreshCw" className="w-3.5 h-3.5 animate-spin" />
                    <span>ZERO CHILL AI is synthesizing legal & cyber response...</span>
                  </div>
                )}
              </div>

              {/* Chat Input Bar */}
              <form onSubmit={handleSendChatMessage} className="flex items-center gap-2 pt-2 border-t border-slate-800">
                <input
                  type="text"
                  value={chatInput}
                  onChange={(e) => setChatInput(e.target.value)}
                  placeholder="Ask a question in English, हिन्दी, or తెలుగు..."
                  className="flex-1 bg-[#0a1226] border border-slate-700 rounded-xl px-4 py-2.5 text-xs sm:text-sm text-white focus:outline-none focus:border-cyan-500"
                />
                <button
                  type="submit"
                  disabled={!chatInput.trim() || isChatThinking}
                  className="px-5 py-2.5 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 text-white font-bold text-xs flex items-center gap-1.5 shadow-lg shadow-cyan-500/20 disabled:opacity-50"
                >
                  <span>Send</span>
                  <Icon name="Send" className="w-3.5 h-3.5" />
                </button>
              </form>
            </div>
          </div>
        )}

        {/* ========================================================
            TAB 8: TELEMETRY DASHBOARD & ANALYTICS
        ======================================================== */}
        {activeTab === "dashboard" && (
          <div className="max-w-5xl mx-auto space-y-8 animate-fadeIn">
            <div className="text-center space-y-2">
              <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-xs font-semibold">
                <Icon name="BarChart3" className="w-3.5 h-3.5" />
                <span>DATABASE-BACKED TELEMETRY</span>
              </div>
              <h2 className="text-3xl font-extrabold text-white">
                Live Cyber Threat Intelligence Dashboard
              </h2>
              <p className="text-xs sm:text-sm text-slate-400 max-w-xl mx-auto">
                Real database metrics tracking scam trends, threat distributions, and historical evaluations.
              </p>
            </div>

            {/* Metrics Counters */}
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
              <div className="p-5 rounded-2xl bg-slate-900 border border-slate-800 text-center space-y-1">
                <span className="text-xs text-slate-400 font-medium">Total Messages Scanned</span>
                <div className="text-3xl font-extrabold text-white font-mono">{telemetry.totalScans}</div>
              </div>

              <div className="p-5 rounded-2xl bg-slate-900 border border-red-500/30 text-center space-y-1">
                <span className="text-xs text-red-300 font-medium">High-Risk Scams</span>
                <div className="text-3xl font-extrabold text-red-400 font-mono">{telemetry.highRiskScans}</div>
              </div>

              <div className="p-5 rounded-2xl bg-slate-900 border border-amber-500/30 text-center space-y-1">
                <span className="text-xs text-amber-300 font-medium">Suspicious Content</span>
                <div className="text-3xl font-extrabold text-amber-400 font-mono">{telemetry.suspiciousScans}</div>
              </div>

              <div className="p-5 rounded-2xl bg-slate-900 border border-emerald-500/30 text-center space-y-1">
                <span className="text-xs text-emerald-300 font-medium">Safe Messages</span>
                <div className="text-3xl font-extrabold text-emerald-400 font-mono">{telemetry.safeScans}</div>
              </div>
            </div>

            {/* Top Threat Categories Bar Chart */}
            <div className="glass-panel-elevated rounded-3xl p-6 sm:p-8 space-y-4">
              <h3 className="text-sm font-bold text-white flex items-center gap-2 border-b border-slate-800 pb-3">
                <Icon name="BarChart3" className="w-4 h-4 text-cyan-400" />
                <span>Threat Category Distribution (Active Database Records)</span>
              </h3>

              {(telemetry.topCategories || []).length === 0 ? (
                <p className="text-xs text-slate-500 py-4 text-center">Run scans to generate distribution telemetry.</p>
              ) : (
                <div className="space-y-3">
                  {(telemetry.topCategories || []).map((cat, idx) => {
                    const max = Math.max(...(telemetry.topCategories || []).map(c => c.count)) || 1;
                    const pct = Math.round((cat.count / max) * 100);
                    return (
                      <div key={idx} className="space-y-1">
                        <div className="flex items-center justify-between text-xs">
                          <span className="font-semibold text-slate-200">{cat.category}</span>
                          <span className="font-mono text-cyan-300">{cat.count} scan(s)</span>
                        </div>
                        <div className="w-full bg-slate-800 h-2.5 rounded-full overflow-hidden">
                          <div className="bg-gradient-to-r from-cyan-500 to-blue-500 h-full rounded-full transition-all duration-500" style={{ width: `${pct}%` }}></div>
                        </div>
                      </div>
                    );
                  })}
                </div>
              )}
            </div>

            {/* SQLite Scan History Log */}
            <div className="glass-panel-elevated rounded-3xl p-6 sm:p-8 space-y-4">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-800 pb-3">
                <h3 className="text-sm font-bold text-white flex items-center gap-2">
                  <Icon name="History" className="w-4 h-4 text-cyan-400" />
                  <span>Recent Scan History ({scanHistory.length})</span>
                </h3>

                <div className="flex items-center gap-2">
                  <div className="flex items-center bg-slate-900 border border-slate-800 p-0.5 rounded-xl text-xs font-semibold">
                    {["ALL", "HIGH-RISK SCAM", "SUSPICIOUS", "SAFE"].map(fk => (
                      <button
                        key={fk}
                        onClick={() => setHistoryFilter(fk)}
                        className={`px-2 py-0.5 rounded-lg transition ${historyFilter === fk ? "bg-cyan-500/20 text-cyan-300 font-bold" : "text-slate-400 hover:text-white"}`}
                      >
                        {fk === "HIGH-RISK SCAM" ? "Scams" : fk === "ALL" ? "All" : fk === "SUSPICIOUS" ? "Suspicious" : "Safe"}
                      </button>
                    ))}
                  </div>

                  {scanHistory.length > 0 && (
                    <button
                      onClick={async () => {
                        if (window.confirm("Clear all scan history from SQLite database?")) {
                          await fetch("/api/history", { method: "DELETE" });
                          showToast("Scan history cleared.", "info");
                          fetchHistory();
                          fetchStats();
                        }
                      }}
                      className="p-1.5 rounded-lg text-slate-400 hover:text-red-400 hover:bg-red-500/10 transition"
                      title="Clear database history"
                    >
                      <Icon name="Trash2" className="w-4 h-4" />
                    </button>
                  )}
                </div>
              </div>

              <div className="space-y-3">
                {scanHistory
                  .filter(h => historyFilter === "ALL" || h.risk_level === historyFilter)
                  .map((item) => (
                    <div
                      key={item.id}
                      onClick={() => {
                        handleAnalyze(item.input_text, item.scan_type);
                        setActiveTab("scanner");
                      }}
                      className="p-3.5 rounded-2xl bg-slate-900 border border-slate-800 hover:border-cyan-500/40 cursor-pointer transition flex flex-col sm:flex-row sm:items-center justify-between gap-3 group"
                    >
                      <div className="space-y-1 flex-1 min-w-0">
                        <div className="flex items-center gap-2">
                          <span className={`text-[9px] font-mono px-2 py-0.5 rounded-full font-bold uppercase ${
                            item.risk_level === "HIGH-RISK SCAM" ? "bg-red-500/20 text-red-300 border border-red-500/40" : item.risk_level === "SUSPICIOUS" ? "bg-amber-500/20 text-amber-300 border border-amber-500/40" : "bg-emerald-500/20 text-emerald-300 border border-emerald-500/40"
                          }`}>
                            {item.risk_level}
                          </span>
                          <span className="text-xs font-semibold text-slate-200">{item.scam_category}</span>
                          <span className="text-[10px] text-slate-500 font-mono">[{item.scan_type}]</span>
                        </div>
                        <p className="text-xs text-slate-400 truncate group-hover:text-slate-200">"{item.clean_snippet}"</p>
                      </div>

                      <div className="flex items-center gap-3 shrink-0">
                        <span className="text-xs font-mono font-bold text-white">Score: {item.risk_score}/100</span>
                        <button
                          onClick={async (e) => {
                            e.stopPropagation();
                            await fetch(`/api/history/${item.id}`, { method: "DELETE" });
                            fetchHistory();
                            fetchStats();
                            showToast("Scan entry deleted.", "info");
                          }}
                          className="p-1 rounded text-slate-500 hover:text-red-400"
                        >
                          <Icon name="Trash2" className="w-3.5 h-3.5" />
                        </button>
                      </div>
                    </div>
                  ))}
              </div>
            </div>
          </div>
        )}

      </main>

      {/* FOOTER */}
      <footer className="border-t border-slate-800/80 bg-[#060a16] text-slate-400 text-xs py-8 relative z-10 mt-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-center sm:text-left">
          <div className="space-y-1">
            <div className="flex items-center justify-center sm:justify-start gap-2 text-white font-bold font-mono">
              <Icon name="ShieldAlert" className="w-4 h-4 text-cyan-400" />
              <span>ZERO CHILL 3.0</span>
            </div>
            <p className="text-[11px] text-slate-500">
              National Hackathon Edition: AI Cyber Safety, Cybercrime Prevention & Legal Action Platform.
            </p>
          </div>
          <div className="text-[11px] text-slate-500 max-w-md">
            ZERO CHILL 3.0 is an independent civic defense system. Always report financial loss to 1930 and file formal complaints on cybercrime.gov.in.
          </div>
        </div>
      </footer>

      {/* MODAL: EMERGENCY 1930 GUIDE */}
      {isEmergencyModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/75 backdrop-blur-md animate-fadeIn">
          <div className="max-w-2xl w-full max-h-[85vh] overflow-y-auto glass-panel-elevated rounded-3xl p-6 sm:p-8 space-y-6 border border-red-500/40">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <div className="flex items-center gap-2.5">
                <div className="w-9 h-9 rounded-xl bg-red-500/20 border border-red-500/40 flex items-center justify-center">
                  <Icon name="PhoneCall" className="w-5 h-5 text-red-400 animate-pulse" />
                </div>
                <div>
                  <h3 className="text-base font-extrabold text-white">Emergency Cyber Fraud Protocol</h3>
                  <p className="text-[11px] text-red-300 font-semibold">Golden Window: Act within 2 hours to freeze stolen money</p>
                </div>
              </div>
              <button onClick={() => setIsEmergencyModalOpen(false)} className="p-1 rounded-lg text-slate-400 hover:text-white">
                <Icon name="X" className="w-5 h-5" />
              </button>
            </div>

            <div className="p-4 rounded-2xl bg-gradient-to-r from-red-950/80 to-slate-900 border border-red-500/50 flex flex-col sm:flex-row items-center justify-between gap-4">
              <div>
                <span className="text-[10px] uppercase font-bold tracking-wider text-red-400">National Cyber Crime Helpline (India)</span>
                <div className="text-2xl font-black text-white font-mono flex items-center gap-2">
                  <span>Dial 1930</span>
                  <span className="text-xs font-sans font-semibold text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/30">
                    24x7 Toll-Free
                  </span>
                </div>
                <p className="text-xs text-slate-300 mt-0.5">Operated by MHA / I4C to coordinate immediate bank transfer freezing.</p>
              </div>

              <a
                href="tel:1930"
                className="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-red-600 hover:bg-red-500 text-white font-bold text-xs flex items-center justify-center gap-2 shadow-lg shadow-red-600/40 transition"
              >
                <Icon name="PhoneCall" className="w-4 h-4" />
                <span>Call 1930 Now</span>
              </a>
            </div>

            <div className="space-y-3 text-xs text-slate-300">
              <h4 className="font-bold uppercase tracking-wider text-slate-400">Step-by-Step Instructions:</h4>
              <ol className="space-y-2 list-decimal list-inside leading-relaxed">
                <li><strong>Block Cards & Netbanking:</strong> Open your bank app or call customer care to block your card immediately.</li>
                <li><strong>Call 1930 with UTR:</strong> Provide police operator with your bank account, amount, and transaction UTR number.</li>
                <li><strong>Complete cybercrime.gov.in complaint:</strong> File formal online complaint within 24 hours.</li>
                <li><strong>Preserve Evidence:</strong> Do not delete SMS or WhatsApp chats. Save screenshots in ZERO CHILL Evidence Vault.</li>
              </ol>
            </div>

            <div className="flex justify-end pt-2">
              <button
                onClick={() => setIsEmergencyModalOpen(false)}
                className="px-6 py-2 rounded-xl bg-slate-800 text-white text-xs font-bold hover:bg-slate-700 transition"
              >
                Close Protocol
              </button>
            </div>
          </div>
        </div>
      )}

      {/* MODAL: API KEY & ENGINE SETTINGS */}
      {isApiKeyModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-sm animate-fadeIn">
          <div className="max-w-md w-full glass-panel-elevated rounded-3xl p-6 sm:p-8 space-y-5 border border-slate-700">
            <div className="flex items-center justify-between">
              <h3 className="text-base font-bold text-white flex items-center gap-2">
                <Icon name="Key" className="w-5 h-5 text-cyan-400" />
                <span>AI & Threat Engine Configuration</span>
              </h3>
              <button onClick={() => setIsApiKeyModalOpen(false)} className="p-1 rounded-lg text-slate-400 hover:text-white">
                <Icon name="X" className="w-5 h-5" />
              </button>
            </div>

            <div className="space-y-3 text-xs text-slate-300">
              <div className="p-3 rounded-xl bg-cyan-950/40 border border-cyan-500/30 text-cyan-200">
                <span className="font-bold">✨ Dual Engine Active:</span> ZERO CHILL 3.0 includes an offline natural language heuristic engine that operates 100% reliably without requiring any paid API key.
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1">Optional: Google Gemini API Key</label>
                <input
                  type="password"
                  value={geminiApiKey}
                  onChange={(e) => setGeminiApiKey(e.target.value)}
                  placeholder="Paste AI Studio API key (AIzaSy...)"
                  className="w-full bg-[#0a1226] border border-slate-700 rounded-xl px-3 py-2.5 text-xs text-white focus:outline-none focus:border-cyan-500 font-mono"
                />
              </div>

              <div className="flex items-center gap-2 pt-2">
                <button
                  type="button"
                  onClick={() => {
                    localStorage.setItem("zerochill_gemini_key", geminiApiKey.trim());
                    showToast(geminiApiKey ? "Gemini API key saved!" : "Using Offline Heuristic Engine.", "success");
                    setIsApiKeyModalOpen(false);
                  }}
                  className="flex-1 py-2 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-[#070d1b] font-bold text-xs transition"
                >
                  Save & Apply
                </button>
                {geminiApiKey && (
                  <button
                    type="button"
                    onClick={() => {
                      setGeminiApiKey("");
                      localStorage.removeItem("zerochill_gemini_key");
                      showToast("API key removed. Running in offline mode.", "info");
                    }}
                    className="py-2 px-3 rounded-xl bg-slate-800 text-slate-300 hover:text-white text-xs font-semibold"
                  >
                    Clear Key
                  </button>
                )}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* TOAST FLOATING NOTIFICATION */}
      {toastMessage && (
        <div className="fixed bottom-6 right-6 z-50 animate-bounce">
          <div className={`flex items-center gap-2 px-4 py-2.5 rounded-2xl shadow-2xl border text-xs font-semibold backdrop-blur-xl ${
            toastMessage.type === "error" ? "bg-red-950/90 border-red-500/50 text-red-200" : toastMessage.type === "success" ? "bg-emerald-950/90 border-emerald-500/50 text-emerald-200" : "bg-slate-900/90 border-cyan-500/40 text-cyan-200"
          }`}>
            <Icon name={toastMessage.type === "error" ? "AlertTriangle" : toastMessage.type === "success" ? "CheckCircle" : "Shield"} className="w-4 h-4 shrink-0" />
            <span>{toastMessage.message}</span>
            <button onClick={() => setToastMessage(null)} className="ml-2 text-slate-400 hover:text-white">
              <Icon name="X" className="w-3.5 h-3.5" />
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

// Render root
const rootElement = document.getElementById("root");
if (rootElement) {
  const root = ReactDOM.createRoot(rootElement);
  root.render(<ZeroChillApp />);
}
