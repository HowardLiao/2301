#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_full_visual_html.py
Renders 5 publication-grade SVG enterprise architecture diagrams in
STRICT MILAN WARM AMBER / EGYPTIAN PHARAOH STYLE (米蘭風格):
- Canvas background: Soft alabaster paper (#FAF7F2 / #FFFFFF).
- Swimlanes: Card white (#FFFFFF) with warm borders (#B8AFA3) and Milan green headers (#2F4538).
- Cards: Pure white with warm line borders (#B8AFA3), Milan green titles, gold tag badges (#C8A96A).
- Interactive: EVERY CARD is a clickable <g class="milan-card"> that invokes inspectCard(key)
  and dynamically highlights with Egyptian Gold border and reveals the deep specification below!
- Zero black/cyber terminal colors.
- Authored by Howard Liao Ph.D.

Author: Howard Liao Ph.D.
"""

import html

def make_defs():
    return """
    <defs>
      <marker id="arr-green" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#2F4538"/>
      </marker>
      <marker id="arr-gold" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#C8A96A"/>
      </marker>
      <marker id="arr-brick" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#9C5B4A"/>
      </marker>
      <filter id="milan-hover-shadow" x="-10%" y="-10%" width="120%" height="120%">
        <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#C8A96A" flood-opacity="0.3"/>
      </filter>
    </defs>
    """

def svg_card(x, y, w, h, title, subtitle="", tag="", key="", fill="#FFFFFF", stroke="#B8AFA3", title_color="#2F4538", sub_color="#6B6459", tag_bg="#E8E2D9", tag_color="#2F4538"):
    sub_lines = [s for s in subtitle.split("\n") if s.strip()] if subtitle else []
    offset_y = 44 if tag else 24
    line_spacing = 17
    text_bottom = (offset_y + 4 + len(sub_lines) * line_spacing) if sub_lines else (offset_y + 4)
    actual_h = max(h, text_bottom + 18)  # Safe bottom padding

    node_key = key if key else title.replace(" ", "_")
    
    lines = [f'<g class="milan-card" data-key="{node_key}" onclick="inspectCard(\'{node_key}\')" cursor="pointer" transform="translate({x},{y})">']
    lines.append(f'<rect width="{w}" height="{actual_h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.5" class="card-bg"/>')
    
    if tag:
        tag_w = min(w - 24, len(tag) * 11 + 16)
        lines.append(f'<rect x="12" y="8" width="{tag_w}" height="18" rx="4" fill="{tag_bg}"/>')
        lines.append(f'<text x="{12 + tag_w/2}" y="21" font-size="10" font-weight="700" fill="{tag_color}" text-anchor="middle" font-family="sans-serif">{html.escape(tag)}</text>')
    
    # Title in Milan deep green
    lines.append(f'<text x="14" y="{offset_y}" font-size="12" font-weight="700" fill="{title_color}" font-family="sans-serif">{html.escape(title)}</text>')
    
    # Subtitles in Milan warm charcoal
    if sub_lines:
        curr_y = offset_y + 18
        for sl in sub_lines:
            lines.append(f'<text x="14" y="{curr_y}" font-size="10.5" fill="{sub_color}" font-family="sans-serif">{html.escape(sl)}</text>')
            curr_y += line_spacing
            
    lines.append('</g>')
    return "\n".join(lines)

def svg_lane(x, y, w, h, title, fill="#FFFFFF", stroke="#B8AFA3", title_color="#2F4538"):
    return f"""
    <g transform="translate({x},{y})">
      <rect width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>
      <rect width="{w}" height="32" rx="10" fill="#E8E2D9" stroke="{stroke}" stroke-width="0.5"/>
      <text x="16" y="21" font-size="12.5" font-weight="800" fill="{title_color}" font-family="sans-serif">{html.escape(title)}</text>
    </g>
    """

def generate_svg_page1():
    # Page 1: Overview in Milan Style
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 1240" width="100%" height="100%" style="background:#FAF7F2; border-radius:10px;">']
    svg.append(make_defs())
    
    # Milan Header Banner
    svg.append("""
    <rect x="20" y="15" width="1400" height="58" rx="8" fill="#FFFFFF" stroke="#C8A96A" stroke-width="2"/>
    <text x="720" y="38" font-size="16" font-weight="800" fill="#2F4538" text-anchor="middle" font-family="sans-serif">企業級 AI 平台 ＆ Howard 資安防禦全域架構圖 (Blueprint)</text>
    <text x="720" y="58" font-size="11.5" fill="#6B6459" text-anchor="middle" font-family="sans-serif">Enterprise GPT・AI Agent Platform・地端 AIDC・Howard AIRS 核心防護・後量子密碼防線 ｜ 架構總設計：Howard Liao Ph.D.</text>
    """)
    
    # Layer 1: Business Access (y=90, h=165)
    svg.append(svg_lane(20, 90, 1400, 165, "【使用者與全通路上層業務場景】Consumers, Corporate Operations & Agents"))
    svg.append(svg_card(35, 132, 215, 105, "全通路數位入口", "消費者端 AI 購物助手\n智慧搜尋與個人化推薦", "Digital Portal", "p1_l1_web"))
    svg.append(svg_card(268, 132, 215, 105, "企業內部營運場景", "HR 人資行政審核 Agent\n財務報銷自動化 Agent", "Internal ERP", "p1_l1_erp"))
    svg.append(svg_card(501, 132, 215, 105, "電商營運與智慧物流", "庫存水位智慧預測\n智慧物流派件調度", "Supply Chain", "p1_l1_scm"))
    svg.append(svg_card(734, 132, 215, 105, "智慧客服中心", "7x24 全時段對話客服\n售後投訴智慧分流處理", "Customer Ops", "p1_l1_cs"))
    svg.append(svg_card(967, 132, 215, 105, "研發團隊與 AI Developer", "Cursor / IDE 擴充套件\n自動化腳本與工具呼叫", "Developers", "p1_l1_dev"))
    svg.append(svg_card(1200, 132, 205, 105, "非人類身分 (NHI)", "自主 Agentic Worker\n背景定時批次排程作業", "NHI Identity", "p1_l1_nhi"))

    # Layer 2: Howard Edge Security (y=270, h=175)
    svg.append(svg_lane(20, 270, 1400, 175, "【Howard AI 安全入口與治理層】Howard AIRS 核心閘門 & AI Gateway Hub"))
    svg.append(svg_card(35, 312, 265, 115, "Howard AIRS 核心防護", "AI Runtime Security 全生命週期防護\n提示詞注入攔截・越獄防禦\n客戶隱私個資 (PII) 自動遮蔽去識別", "Runtime Sec", "p1_l2_airs", tag_bg="#C8A96A", tag_color="#FFF"))
    svg.append(svg_card(318, 312, 265, 115, "Howard AI Gateway", "多模型動態路由・多租戶隔離\n智慧語意快取 (Semantic Cache)\n負載平衡與防抖自動降級", "LLM Gateway", "p1_l2_gateway"))
    svg.append(svg_card(601, 312, 265, 115, "Howard FinOps 治理中樞", "Token / GPU 即時用量計費 (Chargeback)\n部門配額設限 (Resource Quota)\n成本效益可視化分析儀表板", "Cost Control", "p1_l2_finops"))
    svg.append(svg_card(884, 312, 265, 115, "Howard NHI 身分與意圖審計", "機器身分生命週期憑證管理\n防代理混淆 (Confused Deputy)\n推論鏈 Intent Auditability 存證", "Identity Auth", "p1_l2_intent"))
    svg.append(svg_card(1167, 312, 238, 115, "Howard 全鏈路可觀測中樞", "Langfuse + OpenTelemetry 深度整合\nLatency・Error・Token 全方位追蹤\n異常調用即時警報與分流", "Observability", "p1_l2_obs"))

    # Layer 3: Enterprise Platform (y=460, h=180)
    svg.append(svg_lane(20, 460, 1400, 180, "【企業級 AI 核心平台】Enterprise GPT & Agent Platform Ecosystem"))
    svg.append(svg_card(35, 502, 265, 120, "Enterprise GPT 企業大腦平台", "企業內部專屬 LLM 互動平台\n內部法規 FAQ 與公文自動起草\n跨部門知識問答檢索助手", "Core Brain", "p1_l3_gpt", tag_bg="#C8A96A", tag_color="#FFF"))
    svg.append(svg_card(318, 502, 265, 120, "AI Agent Workflow 引擎", "多代理協同架構・任務拆解排程\nStateful ReAct / Plan-and-Solve 循環\n自動上下文維護與狀態轉移", "Agent Engine", "p1_l3_agent"))
    svg.append(svg_card(601, 502, 265, 120, "全鏈路 RAG 檢索增強系統", "多路召回 (語意向量 + 關鍵字重排)\n企業級文件智慧解析與切片\n商品目錄與制度規章知識庫", "Hybrid RAG", "p1_l3_rag"))
    svg.append(svg_card(884, 502, 265, 120, "MCP 工具整合中樞", "標準化外部工具動態調用協定\nERP / WMS / CRM / 訂單資料庫介接\n權限隔離沙箱與參數校驗", "MCP Tool Hub", "p1_l3_mcp"))
    svg.append(svg_card(1167, 502, 238, 120, "模型選型與微調 Pipeline", "領域專有語意微調 (LoRA / SFT)\n開源大模型領域適配 (Domain LLM)\n效能評估驗證與基準測試", "Fine-Tuning", "p1_l3_fine"))

    # Layer 4: Compute & Models (y=655, h=190)
    svg.append(svg_lane(20, 655, 1400, 190, "【混合算力與模型推論調度層】Hybrid Cloud & On-Premises AIDC Computing Center"))
    svg.append(svg_card(35, 697, 265, 130, "公有雲商用模型 API", "• Google Gemini 2.5 Pro (Vertex AI)\n• Anthropic Claude 3.7 Sonnet (Bedrock)\n• 支援雙 11 大促突發流量彈性擴容\n• 雲端專屬無資料訓練承諾", "Public Cloud", "p1_l4_cloud"))
    svg.append(svg_card(318, 697, 265, 130, "Kubernetes GPU 調度中樞", "• Volcano 智慧排程器 (Priority Queue)\n• NVIDIA MIG 資源切片硬體虛擬化\n• 多租戶命名空間隔離與配額限制\n• 基于 Queue 深度觸發自動擴縮 (HPA)", "K8s Scheduling", "p1_l4_sched", tag_bg="#C8A96A", tag_color="#FFF"))
    svg.append(svg_card(601, 697, 265, 130, "高效能推論服務叢集", "• 開源模型：Llama 3.3 / Qwen / DeepSeek\n• PagedAttention 記憶體快取最佳化\n• Continuous Batching 並行處理\n• FP8 / INT4 模型量化降低推論延遲", "vLLM Cluster", "p1_l4_vllm"))
    svg.append(svg_card(884, 697, 265, 130, "地端 AIDC GPU 硬體基礎設施", "• NVIDIA H100/H200 / AMD MI300X 叢集\n• 400G RoCE v2 GPUDirect RDMA 無損網路\n• NVMe-oF 高速分散式平行檔案系統\n• 資料 100% 地端留存，降低 42.8% TCO", "AIDC Infra", "p1_l4_aidc"))
    svg.append(svg_card(1167, 697, 238, 130, "企業資料中樞與向量儲存", "• Milvus / Qdrant 高效向量索引\n• Enterprise Lakehouse (BigQuery/S3)\n• 行層級安全 (RLS) 與資料實體隔離\n• 機密資料加密防洩漏防護", "Storage & DB", "p1_l4_storage"))

    # Layer 5: Foundation Security (y=860, h=190)
    svg.append(svg_lane(20, 860, 1400, 190, "【Howard 端點現代周界、供應鏈防禦與後量子密碼學底座】Enterprise Browser, Supply Chain & Quantum-Safe"))
    svg.append(svg_card(35, 902, 265, 130, "Howard Enterprise Browser", "安全企業瀏覽器底座 + Wings AI Risk Engine\n• 保護瀏覽器外掛・IDE 擴充套件安全\n• MCP 外部工具現代軟體周界全面監管\n• 在端點下載前即刻完成封鎖隔離", "Modern Edge", "p1_l5_browser", tag_bg="#C8A96A", tag_color="#FFF"))
    svg.append(svg_card(318, 902, 265, 130, "Howard 5 階供應鏈防禦鏈", "阻斷類似 Shai-Hulud 自動化供應鏈投毒\n• 1. 入口攔截 ➔ 2. Runtime 行為防護\n• 3. 憑證保護 ➔ 4. CI/CD 冷卻緩衝 (72h)\n• 5. 持續硬隔離收容爆炸半徑", "Supply Chain", "p1_l5_supply"))
    svg.append(svg_card(601, 902, 265, 130, "Howard Dynamic CBOM 清冊", "全企業密碼技術資產動態清冊\n• 自動盤點加密套件、憑證與金鑰長度\n• AI 評估老舊設備與印表機 PQC 就緒度\n• 動態輸出持續可稽核密碼學地圖", "CBOM Inventory", "p1_l5_cbom"))
    svg.append(svg_card(884, 902, 265, 130, "Howard Crypto Agility 四階閉環", "密碼學敏捷性完整治理落地\n• 1. Howard NGFW 發現 ➔ 2. 多維風險評估\n• 3. 政策自動下發 / 密碼轉譯中繼防護\n• 4. NIST PQC 國際標準合規報告", "Crypto Agility", "p1_l5_crypto"))
    svg.append(svg_card(1167, 902, 238, 130, "後量子防禦 (PQC Readiness)", "防範「先截獲、後解密」(HNDL) 長期危機\n• 符合 NIST FIPS 203/204/205 標準\n• ML-KEM / ML-DSA 後量子演算法支援\n• 確保商業機密與個資 10+ 年抗破譯能力", "Quantum-Safe", "p1_l5_pqc"))

    # Layer 6: Infra & SRE (y=1065, h=155)
    svg.append(svg_lane(20, 1065, 1400, 155, "【Infra 平台工程與維運自動化】Platform Engineering, GitOps & SRE Reliability"))
    svg.append(svg_card(35, 1107, 265, 95, "GitOps & 宣告式交付", "• ArgoCD + Terraform 雲地 IaC 部署\n• 基礎設施全版本受控、稽核可追蹤", "GitOps", "p1_l6_gitops"))
    svg.append(svg_card(318, 1107, 265, 95, "自動化安全 CI/CD 流水線", "• 整合靜態代碼分析 (SAST) 與依賴掃描\n• 漏洞風險門檻強制中斷阻斷機制", "DevSecOps", "p1_l6_cicd"))
    svg.append(svg_card(601, 1107, 265, 95, "SRE 智慧維運與告警分流", "• AIOps 根因分析・異常自我修復\n• 智慧降噪與事件自動調查排除", "AIOps / SRE", "p1_l6_sre"))
    svg.append(svg_card(884, 1107, 265, 95, "業務連續性與災難復原 (BCP)", "• 跨雲資料非同步抄寫・地端機房備援\n• 目標 RTO &lt; 1hr, RPO ≈ 0 營運韌性", "BCP / DR", "p1_l6_bcp"))
    svg.append(svg_card(1167, 1107, 238, 95, "雙員工治理與規範手冊", "• 人類員工 vs. 數位員工規則分流管轄\n• 嚴格落實 ISO 27001 / ISO 42001", "Governance", "p1_l6_gov"))

    svg.append('</svg>')
    return "".join(svg)


def generate_svg_page2():
    # Page 2: Intent Audit Flow in Milan Style
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 960" width="100%" height="100%" style="background:#FAF7F2; border-radius:10px;">']
    svg.append(make_defs())
    svg.append("""
    <rect x="20" y="15" width="1400" height="58" rx="8" fill="#FFFFFF" stroke="#C8A96A" stroke-width="2"/>
    <text x="720" y="38" font-size="16" font-weight="800" fill="#2F4538" text-anchor="middle" font-family="sans-serif">Howard AI Agent 意圖審計 (Intent Auditability) 與防混淆代理人防護流程</text>
    <text x="720" y="58" font-size="11.5" fill="#6B6459" text-anchor="middle" font-family="sans-serif">解決間接提示詞注入 (Indirect Prompt Injection)、非人類身分 (NHI) 權限擴大與不可審計痛點 ｜ 架構總設計：Howard Liao Ph.D.</text>
    """)

    col_w = 335
    spacing = 20
    start_x = 25

    # 4 Columns in Milan style
    svg.append(svg_lane(start_x, 90, col_w, 850, "1. 請求輸入與上下文載入 (Input & Context)"))
    svg.append(svg_card(start_x+15, 135, col_w-30, 115, "使用者 Prompt 或業務事件", "• 終端消費者前台對話請求\n• 內部同仁審批作業指示\n• 外部系統 Webhook 觸發事件", "User Input", "p2_input_user"))
    svg.append(svg_card(start_x+15, 275, col_w-30, 125, "外部檢索資料 / 第三方網頁", "• 供應商外部 API 回應\n• 爬蟲與未受信任外部網頁\n⚠️ 潛藏間接提示詞注入風險", "Untrusted", "p2_input_untrusted", tag_bg="#9C5B4A", tag_color="#FFF"))
    svg.append(svg_card(start_x+15, 425, col_w-30, 115, "非人類身分 (NHI) 特權憑證", "• Agent 專用短期 STS Token\n• MCP Tool 調用授權金鑰\n• 最小權限 Service Account 角色", "NHI Credential", "p2_input_nhi"))
    svg.append(svg_card(start_x+15, 565, col_w-30, 115, "執行環境記憶 (Session Context)", "• 短期交談歷程 (Chat History)\n• Agent 當前狀態與變數槽位\n• 任務初始目標約束錨定", "Context Memory", "p2_input_mem"))

    cur_x = start_x + col_w + spacing
    svg.append(svg_lane(cur_x, 90, col_w, 850, "2. Howard 安全中樞 (Security Guardrails)"))
    svg.append(svg_card(cur_x+15, 135, col_w-30, 120, "Howard AIRS 核心安全閘門", "• 語意安全過濾與惡意語法攔截\n• 客戶隱私個資 (PII) 自動遮蔽去識別\n• 越獄與敏感詞動態偵測即刻阻斷", "Runtime Sec", "p2_sec_airs", tag_bg="#C8A96A", tag_color="#FFF"))
    svg.append(svg_card(cur_x+15, 275, col_w-30, 125, "Howard 防混淆代理防護", "• 嚴格區隔「指令通道」與「資料通道」\n• 標記不可信外部資料，防止誘騙挾持\n• 阻斷攻擊者利用 Agent 特權呼叫工具", "Anti-Deputy", "p2_sec_deputy"))
    svg.append(svg_card(cur_x+15, 425, col_w-30, 120, "Howard 意圖驗證引擎", "• 比對 Agent 工具呼叫是否符合原始目標\n• 參數合理性與資料敏感度動態檢驗\n• 越權調用即刻熔斷攔截並告警", "Intent Verify", "p2_sec_verify"))
    svg.append(svg_card(cur_x+15, 565, col_w-30, 120, "Howard Wings AI Risk Engine", "• 即時評估 MCP 工具之安全信譽評等\n• 動態監控 API 請求頻率與封包特徵\n• 阻斷未經認證之外部 MCP 服務呼叫", "Tool Risk", "p2_sec_wings"))
    svg.append(svg_card(cur_x+15, 705, col_w-30, 120, "Howard 推論鏈審計存證", "• 完整記錄「Agent 因何推論而決定調用」\n• 留存可解釋之思維鏈 (Reasoning Trace)\n• 具備法律不可否認性之完整稽核日誌", "Provenance", "p2_sec_provenance"))

    cur_x += col_w + spacing
    svg.append(svg_lane(cur_x, 90, col_w, 850, "3. AI Agent 決策推論核心 (Reasoning)"))
    svg.append(svg_card(cur_x+15, 135, col_w-30, 115, "Enterprise GPT / 開源 vLLM 核心", "• 接收消毒後之 Prompt 與系統指令\n• 任務邏輯拆解與推理 (Reasoning)\n• 擬定下一步執行方案 (Action Plan)", "Core Model", "p2_core_model"))
    svg.append(svg_card(cur_x+15, 275, col_w-30, 115, "Action 決定與參數生成", "• 指定欲調用之 MCP 工具名稱\n• 自動組裝 JSON Schema 調用參數\n• 向安全中樞發起調用宣告請求", "Action Step", "p2_core_action"))
    svg.append(svg_card(cur_x+15, 415, col_w-30, 125, "高風險操作人機介入 (HITL Gate)", "• 金融交易轉帳 / 大額請款\n• 資料庫刪除 / 生產組態變更\n• 強制啟動主管雙人簽核 (Dual Approval)", "HITL Gate", "p2_core_hitl", tag_bg="#C8A96A", tag_color="#FFF"))
    svg.append(svg_card(cur_x+15, 565, col_w-30, 115, "結果聚合與最終輸出生成", "• 接收工具執行結果並驗證真實性\n• 生成給使用者之高質量專業回覆\n• 關閉工作工作階段並釋放 Token", "Result Synth", "p2_core_synth"))

    cur_x += col_w + spacing
    svg.append(svg_lane(cur_x, 90, col_w, 850, "4. 工具執行與後端系統 (Execution & Systems)"))
    svg.append(svg_card(cur_x+15, 135, col_w-30, 115, "WMS / ERP 核心業務系統", "• 即時庫存查詢與鎖定\n• 訂單出貨排程與狀態更新\n• 物流供應鏈派工自動化", "Core ERP", "p2_exec_erp"))
    svg.append(svg_card(cur_x+15, 275, col_w-30, 115, "HR 人資 / 財務系統 API", "• 請款單據立案與審批流程\n• 員工考勤資料彙總與分析\n• 企業差旅預算自動核銷", "Finance & HR", "p2_exec_hr"))
    svg.append(svg_card(cur_x+15, 415, col_w-30, 115, "智慧搜尋與推薦資料庫", "• 商品語意嵌入特徵向量庫\n• 即時動態比價資料庫\n• 個人化推薦偏好快照", "Search & Rec", "p2_exec_search"))
    svg.append(svg_card(cur_x+15, 555, col_w-30, 115, "雲地混合資料庫 / 向量庫", "• PostgreSQL / BigQuery / Milvus\n• 行層級安全 (RLS) 權限隔離\n• 零信任存取閘道全面保護", "Databases", "p2_exec_db"))
    svg.append(svg_card(cur_x+15, 695, col_w-30, 115, "不可否認性合規審計日誌", "• 符合 ISO 27001 / ISO 42001 標準\n• WORM (一次寫入多次讀取) 防竄改\n• 完整保存 Agent 決策法律責任歸屬", "Audit Ledger", "p2_exec_audit"))

    # Connective Arrows in Milan Gold
    svg.append("""
    <path d="M 360 190 L 410 190" fill="none" stroke="#C8A96A" stroke-width="2" marker-end="url(#arr-gold)"/>
    <path d="M 360 330 L 410 330" fill="none" stroke="#9C5B4A" stroke-width="2" marker-end="url(#arr-brick)"/>
    <path d="M 730 190 L 785 190" fill="none" stroke="#2F4538" stroke-width="2" marker-end="url(#arr-green)"/>
    <path d="M 785 330 L 730 330" fill="none" stroke="#C8A96A" stroke-width="2" marker-end="url(#arr-gold)"/>
    <path d="M 730 470 L 785 470" fill="none" stroke="#2F4538" stroke-width="2" marker-end="url(#arr-green)"/>
    <path d="M 1105 470 L 1145 470" fill="none" stroke="#2F4538" stroke-width="2" marker-end="url(#arr-green)"/>
    <path d="M 730 760 L 1145 760" fill="none" stroke="#C8A96A" stroke-width="2" marker-end="url(#arr-gold)"/>
    """)

    svg.append('</svg>')
    return "".join(svg)


def generate_svg_page3():
    # Page 3: 5-Stage Supply Chain in Milan Style
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 960" width="100%" height="100%" style="background:#FAF7F2; border-radius:10px;">']
    svg.append(make_defs())
    svg.append("""
    <rect x="20" y="15" width="1400" height="58" rx="8" fill="#FFFFFF" stroke="#C8A96A" stroke-width="2"/>
    <text x="720" y="38" font-size="16" font-weight="800" fill="#2F4538" text-anchor="middle" font-family="sans-serif">Howard 5 階現代軟體周界與 MCP 供應鏈防禦鏈架構圖</text>
    <text x="720" y="58" font-size="11.5" fill="#6B6459" text-anchor="middle" font-family="sans-serif">治理範疇：瀏覽器外掛、IDE 擴充套件、MCP Tools、開源套件、模型 Weights 與 CI/CD 管道 ｜ 架構總設計：Howard Liao Ph.D.</text>
    """)

    stages = [
        ("第 1 階：Shift-Left 入口攔截", "Howard KOI 內嵌安全閘道", [
            ("防護核心目標", "在擴充功能與工具下載「觸及端點前」即時封鎖，不給任何落地機會。"),
            ("防禦主要對象", "• VS Code / Cursor 擴充套件\n• 瀏覽器 Chrome/Edge 外掛\n• 開源 Python 套件 (PyPI/npm)\n• 外部未授權開源 MCP Server"),
            ("關鍵技術機制", "• Howard 內嵌網路閘道攔截\n• 套件封包指紋與動態雜湊比對\n• 影子擴充套件即時阻斷\n• 企業私有套件 Proxy 白名單"),
            ("MCP 工具動態認證", "• 強制 MCP Server 具備數位簽名\n• 靜態分析 Tool Description 語意\n• 阻斷偽冒與被污染之外部工具")
        ], "p3_stage1"),
        ("第 2 階：Runtime 行為防護", "Howard 執行階段防護", [
            ("防護核心目標", "阻斷惡意程式碼、權限越權與工具惡意行為，嚴格限縮沙箱與容器邊界。"),
            ("防禦主要對象", "• 容器逃逸 (Container Escape)\n• 非法外連 C2 中繼站\n• 未授權磁碟或記憶體讀寫\n• 惡意注入的 Subprocess 行為"),
            ("關鍵技術機制", "• Howard Enterprise Browser 安全探針\n• eBPF 核心級系統呼叫即時監控\n• 最小權限 SELinux / AppArmor\n• 記憶體動態注入偵測阻斷"),
            ("直譯器權限沙箱", "• 限制 Python/Node 直譯器目錄\n• 嚴禁讀取本地 ~/.ssh 與金鑰\n• 異常行程呼叫秒級 SIGKILL 終止")
        ], "p3_stage2"),
        ("第 3 階：憑證與管道防護", "Howard 憑證與防洩中樞", [
            ("防護核心目標", "防禦開發環境遭竊聽、API Key 與 Token 外洩，收攏 NHI 特權憑證。"),
            ("防禦主要對象", "• 本地 .env 與 config 敏感檔\n• 記憶體殘留的雲端 Token\n• Git Commit 誤提交金鑰\n• CI/CD 變數與 Runner 快取"),
            ("關鍵技術機制", "• Howard 機密掃描引擎 (Pre-Commit)\n• 記憶體加密防 Memory Dumper\n• 短生命週期動態憑證 (STS)\n• 特權存取管理 (PAM) 嚴格隔離"),
            ("動態 STS 憑證簽發", "• 密鑰由 Vault 動態產生發放\n• 強制 15 分鐘生命週期過期\n• 徹底根絕長期靜態金鑰外洩")
        ], "p3_stage3"),
        ("第 4 階：CI/CD 冷卻緩衝", "Howard 版本更新緩衝機制", [
            ("防護核心目標", "在自動部署管道設置冷卻期與審查機制，阻止全自動流水線武器化。"),
            ("防禦主要對象", "• 自動更新機制的「即時投毒」\n• 上游相依套件的小版本惡意改動\n• 開源維護者帳號遭挾持\n• Shai-Hulud 模式自動感染"),
            ("關鍵技術機制", "• 強制 72 小時版本發布冷卻緩衝期\n• 主管雙人簽核 (Dual Approval)\n• 隔離沙箱自動回歸測試\n• SBOM 依賴版本鎖定 (Lockfile)"),
            ("自動化沙箱測試", "• 在隔離容器執行全量集成測試\n• 網路行為探測是否有異常廣播\n• 偵測通過後方可由主管批准放行")
        ], "p3_stage4"),
        ("第 5 階：持續補救與硬隔離", "Howard 持續微隔離與復原", [
            ("防護核心目標", "第一時間隔離受感染裝置，收容爆炸半徑，自動化快速復原生產。"),
            ("防禦主要對象", "• 內部橫向移動 (Lateral Movement)\n• 跨網路區段非授權探測\n• 憑證外洩後的持續駐留\n• 機密資料巨量外傳 (Exfiltration)"),
            ("關鍵技術機制", "• Howard 一鍵網路微隔離 (Microseg)\n• 快速撤銷被駭 NHI 憑證與 Key\n• 機器人自動化鑑識 (SOAR)\n• 容器與虛擬機無損回滾 Snapshot"),
            ("黃金鏡像秒級復原", "• 宣告式重置 Pod 至安全基準\n• 3 秒內自動銷毀受感染容器\n• 阻斷橫向滲透並產生鑑識報告")
        ], "p3_stage5")
    ]

    col_w = 268
    spacing = 15
    start_x = 25

    for idx, (stage_title, sub_title, cards, stage_key) in enumerate(stages):
        cur_x = start_x + idx * (col_w + spacing)
        svg.append(svg_lane(cur_x, 90, col_w, 850, stage_title))
        
        # Subtitle banner inside lane
        svg.append(f"""
        <rect x="{cur_x+12}" y="132" width="{col_w-24}" height="32" rx="6" fill="#F2EEE8" stroke="#B8AFA3"/>
        <text x="{cur_x+col_w/2}" y="152" font-size="11.5" font-weight="700" fill="#2F4538" text-anchor="middle" font-family="sans-serif">{sub_title}</text>
        """)

        card_y = 175
        card_heights = [115, 140, 140, 130]
        for c_idx, (c_title, c_desc) in enumerate(cards):
            c_h = card_heights[c_idx]
            sub_key = f"{stage_key}_c{c_idx}"
            svg.append(svg_card(cur_x+12, card_y, col_w-24, c_h, c_title, c_desc, "", sub_key))
            card_y += c_h + 16

        # Stage Transition Arrow
        if idx < 4:
            arrow_x = cur_x + col_w + 1
            svg.append(f"""
            <path d="M {arrow_x} 450 L {arrow_x + spacing - 3} 450" fill="none" stroke="#C8A96A" stroke-width="2.5" marker-end="url(#arr-gold)"/>
            """)

    svg.append('</svg>')
    return "".join(svg)


def generate_svg_page4():
    # Page 4: Hybrid Cloud & AIDC GPU Scheduling in Milan Style
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 960" width="100%" height="100%" style="background:#FAF7F2; border-radius:10px;">']
    svg.append(make_defs())
    svg.append("""
    <rect x="20" y="15" width="1400" height="58" rx="8" fill="#FFFFFF" stroke="#C8A96A" stroke-width="2"/>
    <text x="720" y="38" font-size="16" font-weight="800" fill="#2F4538" text-anchor="middle" font-family="sans-serif">企業混合雲 (GCP/AWS) 與地端 AIDC 綠能運算中心 GPU 資源調度拓撲圖</text>
    <text x="720" y="58" font-size="11.5" fill="#6B6459" text-anchor="middle" font-family="sans-serif">K8s 資源排程・GPU MIG 切片・多租戶隔離・vLLM 推論叢集與 Token 成本計費優化 ｜ 架構總設計：Howard Liao Ph.D.</text>
    """)

    w_zone = 445
    spacing = 25
    start_x = 25

    # Zone 1: Public Cloud
    svg.append(svg_lane(start_x, 90, w_zone, 850, "【公有雲彈性算力層】Public Cloud (GCP Vertex AI / AWS Bedrock)"))
    svg.append(svg_card(start_x+15, 135, w_zone-30, 135, "Google Cloud (GCP) 平台", "• Vertex AI (Gemini 2.5 Flash / Pro 推論)\n• Google Cloud Storage 巨量備份湖\n• BigQuery 巨量分析與即時特徵工程\n• 專用跨國高速骨幹網路", "GCP Cloud", "p4_cloud_gcp"))
    svg.append(svg_card(start_x+15, 290, w_zone-30, 135, "Amazon Web Services (AWS) 平台", "• AWS Bedrock (Claude 3.7 Sonnet 推論)\n• S3 物件儲存與異地雙向即時抄寫\n• 彈性突增流量 GPU 實例 (G5/P5 節點)\n• 企業級高可用容錯架構", "AWS Cloud", "p4_cloud_aws"))
    svg.append(svg_card(start_x+15, 445, w_zone-30, 145, "公有雲主要適用情境", "• 超大長文本 (Long-Context) 深度理解與跨國語意\n• 雙 11 / 年終大促高峰突增算力彈性擴容\n• 尖端商用前瞻模型能力即時 PoC 驗證\n• 降低非尖峰期閒置硬體資本支出", "Cloud Use Cases", "p4_cloud_use"))
    svg.append(svg_card(start_x+15, 610, w_zone-30, 135, "專用加密傳輸通道", "• AWS Direct Connect / GCP Interconnect 專線\n• Howard NGFW 端點全流量清洗與防護\n• IPSec VPN 後量子加密通道保護", "Hybrid Connect", "p4_cloud_vpn"))

    # Zone 2: K8s Scheduler
    cur_x = start_x + w_zone + spacing
    svg.append(svg_lane(cur_x, 90, w_zone, 850, "【K8s 核心調度中樞】Kubernetes Orchestration & GPU Scheduling"))
    svg.append(svg_card(cur_x+15, 135, w_zone-30, 135, "K8s 智慧排程器 (Volcano / Kube-Scheduler)", "• 多維度資源感知排程 (GPU Memory / Compute)\n• Priority & Preemption 高優先權插隊搶佔機制\n• 拓撲感知 (NUMA / PCIe / NVLink) 就近親和排程\n• 確保 GPU 運算資源高負載均衡", "Scheduler", "p4_k8s_sched", tag_bg="#C8A96A", tag_color="#FFF"))
    svg.append(svg_card(cur_x+15, 290, w_zone-30, 135, "GPU 資源切片虛擬化 (MIG / vGPU)", "• NVIDIA Multi-Instance GPU (1g.10gb / 2g.20gb)\n• 輕量級推論任務高密度混部提升利用率\n• 硬體層級嚴格記憶體與算力沙箱隔離\n• 靈活支援不同參數量之模型調度", "GPU Slicing", "p4_k8s_mig"))
    svg.append(svg_card(cur_x+15, 445, w_zone-30, 145, "多租戶配額與計費 (Multi-Tenancy & FinOps)", "• 部門命名空間隔離 (HR, Finance, Operations)\n• ResourceQuota 與 LimitRange 嚴格限額控管\n• Howard FinOps 即時用量計費 (Chargeback) 看板\n• 支援自動化降級與限額保護機制", "FinOps Quota", "p4_k8s_finops"))
    svg.append(svg_card(cur_x+15, 610, w_zone-30, 135, "推論服務叢集 (vLLM / Triton Pods)", "• HPA (Horizontal Pod Autoscaler) 自動彈性擴縮\n• 根據 Queue 深度與 Latency 觸發冷啟動\n• 模型權重熱載入快取 (Model Weight Caching)\n• PagedAttention 大幅減少顯存碎片浪費", "vLLM Engine", "p4_k8s_vllm"))

    # Zone 3: AIDC Hardware
    cur_x += w_zone + spacing
    svg.append(svg_lane(cur_x, 90, w_zone, 850, "【地端 AIDC GPU 硬體機房】On-Premises AI Data Center Infrastructure"))
    svg.append(svg_card(cur_x+15, 135, w_zone-30, 135, "高效能運算伺服器機櫃", "• NVIDIA H100 / H200 SXM5 節點叢集\n• AMD Instinct MI300X 高性價比替代節點\n• 專屬高效能浸沒式/液冷散熱機櫃系統\n• 實現綠能 PUE &lt; 1.25 高能效指標", "GPU Nodes", "p4_aidc_nodes", tag_bg="#C8A96A", tag_color="#FFF"))
    svg.append(svg_card(cur_x+15, 290, w_zone-30, 135, "高速低延遲無損網路拓撲", "• 400Gbps RoCE v2 / InfiniBand Spine-Leaf 架構\n• GPUDirect RDMA (跨伺服器 GPU 記憶體直通)\n• 零封包遺失 (PFC + ECN 壅塞控制)\n• 極致加速分散式並行推論與訓練", "RDMA Network", "p4_aidc_net"))
    svg.append(svg_card(cur_x+15, 445, w_zone-30, 145, "超高速分散式平行儲存架構", "• NVMe-oF 全閃存快顯資料儲存池\n• Lustre / Ceph / Weka 高 IOPS 分散式檔案系統\n• 模型權重秒級並行同步與 Checkpoint 快照\n• 支援高併發向量搜尋特徵抽取", "Storage Infra", "p4_aidc_storage"))
    svg.append(svg_card(cur_x+15, 610, w_zone-30, 135, "地端 AIDC 核心業務效益", "• 機密資料 100% 不落地公有雲，徹底落實合規\n• 長期推論大幅降低 42.8% 雲端 Token 租用成本\n• 毫秒級極致內部系統推論響應延遲\n• 掌握企業核心自主算力主權", "Business Value", "p4_aidc_val"))

    # Connectors in Milan Gold
    svg.append("""
    <path d="M 470 200 L 515 200" fill="none" stroke="#C8A96A" stroke-width="2" marker-end="url(#arr-gold)"/>
    <path d="M 940 350 L 985 350" fill="none" stroke="#2F4538" stroke-width="2" marker-end="url(#arr-green)"/>
    <path d="M 940 670 L 985 670" fill="none" stroke="#C8A96A" stroke-width="2" marker-end="url(#arr-gold)"/>
    """)

    svg.append('</svg>')
    return "".join(svg)


def generate_svg_page5():
    # Page 5: Post-Quantum Crypto Agility in Milan Style
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 960" width="100%" height="100%" style="background:#FAF7F2; border-radius:10px;">']
    svg.append(make_defs())
    svg.append("""
    <rect x="20" y="15" width="1400" height="58" rx="8" fill="#FFFFFF" stroke="#C8A96A" stroke-width="2"/>
    <text x="720" y="38" font-size="16" font-weight="800" fill="#2F4538" text-anchor="middle" font-family="sans-serif">Howard 後量子安全 (Quantum-Safe) 與密碼學敏捷性四階閉環圖</text>
    <text x="720" y="58" font-size="11.5" fill="#6B6459" text-anchor="middle" font-family="sans-serif">防禦「先截獲、後解密」(Harvest Now, Decrypt Later, HNDL) 威脅，符合 NIST PQC 國家安全標準 ｜ 架構總設計：Howard Liao Ph.D.</text>
    """)

    phases = [
        ("第 1 階：持續發現與動態盤點", "Continuous Discovery", [
            ("Howard Dynamic CBOM 引擎", "建立全企業加密套件、憑證、金鑰長度\n與硬體演算能力的動態資產清冊\n實現加密資產即時可視化地圖"),
            ("Howard NGFW 流量自動嗅探", "利用全網防火牆與日誌流量\n自動擷取所有傳輸中裝置的密碼情境\n精準識別弱加密與過期 TLS 協議"),
            ("AI 驅動的 PQC 就緒度分析", "精確識別老舊印表機、產線設備、舊伺服器\n無法運行 PQC 的弱點，建議硬體汰換\n產出硬體生命週期升級建議報告"),
            ("TLS 1.3 密碼套件深度檢測", "DPI 深入檢驗 ClientHello 與 ServerHello\n識別老舊 RSA-1024/2048 弱密鑰\n掃描全網廢止 SHA-1 憑證分佈")
        ], "p5_stage1"),
        ("第 2 階：多維風險評估與優先級", "Risk & Prioritization", [
            ("三維情資關聯矩陣", "• 傳輸中加密強度 (Cipher Suite)\n• CMDB 資產關鍵性 (Asset Criticality)\n• SCM 資料機密敏感度 (Data Sensitivity)\n綜合量化全集團加密資產風險"),
            ("HNDL 暴露風險評分模型", "針對存活期長達 10+ 年之商業機密與個資\n計算暴露時間窗，標記最高緊急修復等級\n防範未來量子運算威脅"),
            ("PQC 遷移優先排程與波次", "依業務影響度自動生成波次 (Waves)\n產出跨部門遷移甘特圖與落地時程建議\n動態追蹤修復預算與人力資源"),
            ("資料壽命半衰期分析模型", "量化機密商業合約、研發專利與財務資料\n計算量子威脅時間窗與密碼破譯臨界點\n強制排定前置防護時程表")
        ], "p5_stage2"),
        ("第 3 階：修復、處置與中繼防護", "Remediation & Translation", [
            ("Howard 政策一鍵自動下發", "對 Howard NGFW、Howard ZTNA、Howard Secure Edge\n一鍵啟用量子安全演算法政策\n秒級完成全網安全邊界升級"),
            ("Howard 密碼轉譯中繼防護", "針對無法升級演算法的老舊系統與設備\n由邊緣閘道進行雙向加密轉譯，實現無痛中繼防護\n延長老舊資產合規服役壽命"),
            ("第三方軟硬體遷移指南", "為企業生態圈外部合作供應商\n產出標準 PQC API 介接規範與升級合規指引\n建立供應鏈量子安全防禦統一戰線"),
            ("混合雙模密鑰過渡協議", "同時封裝傳統 ECDH 與 ML-KEM\n確保過渡期向下相容與抗量子雙重防線\n實現平滑無感演算法切換升級")
        ], "p5_stage3"),
        ("第 4 階：持續治理與動態合規", "Governance & Compliance", [
            ("常態化密碼學衛生 (Hygiene)", "持續追蹤即將過期或已被破解之傳統演算法\n自動化更新動態停用黑名單\n確保全網密碼資產常保健康狀態"),
            ("國際標準稽核報告 (Audit-Ready)", "自動生成符合 NIST PQC (ML-KEM / ML-DSA)\n與國家級資通安全要求的合規審計報告\n大幅降低外部合規查核成本"),
            ("量子抗性持續成熟度指標", "高管儀表板展示全集團 PQC 覆蓋率 (0%~100%)\n協助決策層掌握企業長期量子存亡韌性\n量化呈報董事會與資安委員會"),
            ("全網弱密碼即時警報機制", "監控全網未授權之傳統降級連線 (Downgrade)\n即刻阻斷不安全協商請求\n定期產出資安防禦態勢週報")
        ], "p5_stage4")
    ]

    col_w = 335
    spacing = 20
    start_x = 25

    for idx, (p_title, p_sub, cards, p_key) in enumerate(phases):
        cur_x = start_x + idx * (col_w + spacing)
        svg.append(svg_lane(cur_x, 90, col_w, 850, p_title))
        
        svg.append(f"""
        <rect x="{cur_x+12}" y="132" width="{col_w-24}" height="32" rx="6" fill="#F2EEE8" stroke="#B8AFA3"/>
        <text x="{cur_x+col_w/2}" y="152" font-size="11.5" font-weight="700" fill="#2F4538" text-anchor="middle" font-family="sans-serif">{p_sub}</text>
        """)

        card_y = 175
        card_heights = [125, 125, 130, 125]
        for c_idx, (c_title, c_desc) in enumerate(cards):
            c_h = card_heights[c_idx]
            sub_k = f"{p_key}_c{c_idx}"
            svg.append(svg_card(cur_x+12, card_y, col_w-24, c_h, c_title, c_desc, "", sub_k))
            card_y += c_h + 16

        # Circular arrows between phases in Gold
        if idx < 3:
            arrow_x = cur_x + col_w + 2
            svg.append(f"""
            <path d="M {arrow_x} 450 L {arrow_x + spacing - 4} 450" fill="none" stroke="#C8A96A" stroke-width="2.5" marker-end="url(#arr-gold)"/>
            """)

    # Feedback loop arrow from Phase 4 back to Phase 1 in Green
    svg.append("""
    <path d="M 1200 810 L 1200 855 L 190 855 L 190 810" fill="none" stroke="#2F4538" stroke-width="2.5" stroke-dasharray="6,4" marker-end="url(#arr-green)"/>
    <text x="700" y="850" font-size="11.5" font-weight="700" fill="#2F4538" text-anchor="middle" font-family="sans-serif">↺ 反饋至第 1 階常態動態盤點巡檢 (Continuous Crypto Agility Feedback Loop)</text>
    """)

    svg.append('</svg>')
    return "".join(svg)
