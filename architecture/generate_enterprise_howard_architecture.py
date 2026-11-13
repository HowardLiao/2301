#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_enterprise_howard_architecture.py
Enterprise AI Architect Requirements with Howard Security Strategy.
Generates a 5-page publication-grade Draw.io (.drawio) XML file.
ALL card dimensions and swimlanes expanded so text NEVER clips or overflows borders.

Author: Howard Liao Ph.D.
"""

import html
import xml.etree.ElementTree as ET

class DrawioBuilder:
    def __init__(self, filename):
        self.filename = filename
        self.diagrams = []

    def add_page(self, page_id, name, width=1550, height=1400, bg="#FFFFFF"):
        page = DrawioPage(page_id, name, width, height, bg)
        self.diagrams.append(page)
        return page

    def render_xml(self):
        lines = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<mxfile host="app.diagrams.net" modified="2026-11-13T00:00:00.000Z" agent="Howard Liao Ph.D." version="24.7.17" type="device">'
        ]
        for d in self.diagrams:
            lines.append(d.render())
        lines.append('</mxfile>')
        return "\n".join(lines)

    def save(self):
        xml_content = self.render_xml()
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write(xml_content)
        ET.fromstring(xml_content)
        print(f"Successfully generated and validated {self.filename}")


class DrawioPage:
    def __init__(self, page_id, name, width=1550, height=1400, bg="#FFFFFF"):
        self.page_id = page_id
        self.name = name
        self.width = width
        self.height = height
        self.bg = bg
        self.cells = []
        self._counter = 100

    def next_id(self, prefix="c"):
        self._counter += 1
        return f"{prefix}_{self.page_id}_{self._counter}"

    def add_banner(self, title, subtitle, author="Howard Liao Ph.D.", x=50, y=20, w=1420, h=65, fill="#FFFBEB", stroke="#D97706", text_color="#78350F"):
        cid = self.next_id("banner")
        raw_val = f"<div style='font-size:16px; font-weight:bold; color:{text_color};'>{html.escape(title)}</div>" \
                  f"<div style='font-size:11px; color:#92400E; margin-top:3px;'>{html.escape(subtitle)} ｜ <b>架構與策略總設計：{html.escape(author)}</b></div>"
        val = html.escape(raw_val)
        style = f"rounded=1;whiteSpace=wrap;html=1;fillColor={fill};strokeColor={stroke};strokeWidth=2;align=center;verticalAlign=middle;"
        self.cells.append(f'<mxCell id="{cid}" value="{val}" style="{style}" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry" /></mxCell>')
        return cid

    def add_swimlane(self, label, x, y, w, h, fill="#F8FAFC", stroke="#94A3B8", font_color="#0F172A", stroke_width=1.5):
        cid = self.next_id("lane")
        val = html.escape(f"<b>{html.escape(label)}</b>")
        style = f"swimlane;whiteSpace=wrap;html=1;fillColor={fill};strokeColor={stroke};strokeWidth={stroke_width};fontColor={font_color};fontSize=12;rounded=1;collapsible=0;startSize=28;"
        self.cells.append(f'<mxCell id="{cid}" value="{val}" style="{style}" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry" /></mxCell>')
        return cid

    def add_card(self, label, parent_id, x, y, w, h, fill="#FFFFFF", stroke="#CBD5E1", font_color="#1E293B", shape="rectangle", stroke_width=1, rounded=1):
        cid = self.next_id("card")
        clean_label = html.escape(label).replace("\n", "&#xa;")
        style = f"rounded={rounded};whiteSpace=wrap;html=1;fillColor={fill};strokeColor={stroke};strokeWidth={stroke_width};fontColor={font_color};fontSize=11;align=center;verticalAlign=middle;"
        if shape == "component":
            style = f"shape=component;align=left;spacingLeft=36;whiteSpace=wrap;html=1;fillColor={fill};strokeColor={stroke};strokeWidth={stroke_width};fontColor={font_color};fontSize=11;rounded={rounded};"
        elif shape == "cylinder":
            style = f"shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor={fill};strokeColor={stroke};strokeWidth={stroke_width};fontColor={font_color};fontSize=11;align=center;"
        elif shape == "hexagon":
            style = f"shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fixedSize=1;size=20;fillColor={fill};strokeColor={stroke};strokeWidth={stroke_width};fontColor={font_color};fontSize=11;align=center;"

        self.cells.append(f'<mxCell id="{cid}" value="{clean_label}" style="{style}" vertex="1" parent="{parent_id}"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry" /></mxCell>')
        return cid

    def add_edge(self, src, tgt, label="", stroke="#64748B", stroke_width=1.5, dashed=0, style_extra=""):
        cid = self.next_id("edge")
        style = f"edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor={stroke};strokeWidth={stroke_width};dashed={dashed};fontSize=10;fontColor={stroke};{style_extra}"
        val = html.escape(label).replace("\n", "&#xa;")
        self.cells.append(f'<mxCell id="{cid}" value="{val}" style="{style}" edge="1" parent="1" source="{src}" target="{tgt}"><mxGeometry relative="1" as="geometry" /></mxCell>')
        return cid

    def render(self):
        lines = [
            f'  <diagram id="{self.page_id}" name="{html.escape(self.name)}">',
            f'    <mxGraphModel dx="1500" dy="1300" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{self.width}" pageHeight="{self.height}" background="{self.bg}" math="0" shadow="0">',
            '      <root>',
            '        <mxCell id="0" />',
            '        <mxCell id="1" parent="0" />'
        ]
        for c in self.cells:
            lines.append(f"        {c}")
        lines.append('      </root>')
        lines.append('    </mxGraphModel>')
        lines.append('  </diagram>')
        return "\n".join(lines)


def build_all_diagrams(output_path):
    builder = DrawioBuilder(output_path)

    # =========================================================================
    # PAGE 1: Overall Enterprise AI & Howard Security Architecture Blueprint
    # =========================================================================
    p1 = builder.add_page("p1_overview", "1. 企業級 AI 平台 ＆ Howard 全域架構圖", 1550, 1380)
    p1.add_banner(
        "企業級 AI 平台與 Howard 資安防禦全域架構圖",
        "整合 Enterprise GPT、AI Agent Platform、地端 AIDC、Howard Prisma AIRS 與後量子密碼防線",
        "Howard Liao Ph.D.", x=50, y=20, w=1420, h=65
    )

    # Layer 1: Business Users & Clients (h=170)
    l1 = p1.add_swimlane("【使用者與全通路上層業務場景】Consumers, Operations & Corporate Departments", 50, 100, 1420, 170, fill="#F0F9FF", stroke="#0284C7", font_color="#0369A1")
    c_momo_web = p1.add_card("全通路數位入口 Web / App\n• 消費者端 AI 購物助手\n• 智慧搜尋與個人化推薦", l1, 20, 42, 215, 110, fill="#FFFFFF", stroke="#0284C7")
    c_hr_fin = p1.add_card("企業內部營運場景\n• HR 人資行政審核 Agent\n• 財務報銷自動化 Agent", l1, 255, 42, 215, 110, fill="#FFFFFF", stroke="#0284C7")
    c_ops_log = p1.add_card("電商營運與智慧物流\n• 庫存水位智慧預測\n• 智慧物流派件調度", l1, 490, 42, 215, 110, fill="#FFFFFF", stroke="#0284C7")
    c_cs_live = p1.add_card("智慧客服中心\n• 7x24 全時段對話客服\n• 售後投訴智慧分流處理", l1, 725, 42, 215, 110, fill="#FFFFFF", stroke="#0284C7")
    c_devs = p1.add_card("研發團隊與 AI Developer\n• Cursor / IDE 擴充套件\n• 自動化腳本與工具呼叫", l1, 960, 42, 215, 110, fill="#FFFFFF", stroke="#0284C7")
    c_nhi_agents = p1.add_card("非人類身分 (NHI)\n• 自主 Agentic Worker\n• 背景定時批次排程作業", l1, 1195, 42, 205, 110, fill="#FFFFFF", stroke="#0284C7")

    # Layer 2: Howard Edge & Gateway Security (h=180)
    l2 = p1.add_swimlane("【Howard AI 安全入口與治理層】Howard Prisma AIRS & AI Gateway Hub", 50, 285, 1420, 180, fill="#FEF2F2", stroke="#EF4444", font_color="#991B1B")
    c_hw_airs = p1.add_card("<b>Howard Prisma AIRS</b>\nAI Runtime Security 全生命週期防護\n• 提示詞注入攔截・越獄防禦\n• 客戶隱私個資 (PII) 自動遮蔽去識別", l2, 20, 42, 265, 120, fill="#FFF1F2", stroke="#F43F5E", font_color="#881337", rounded=1)
    c_hw_gateway = p1.add_card("<b>Howard AI Gateway (Portkey / LiteLLM)</b>\n多模型動態路由・多租戶隔離\n• 智慧語意快取 (Semantic Cache)\n• 負載平衡與防抖自動降級", l2, 305, 42, 265, 120, fill="#FFF1F2", stroke="#F43F5E", font_color="#881337", rounded=1)
    c_hw_finops = p1.add_card("<b>Howard FinOps & Token 治理中樞</b>\nToken / GPU 即時用量計費 (Chargeback)\n• 部門配額設限 (Resource Quota)\n• 成本效益可視化分析儀表板", l2, 590, 42, 265, 120, fill="#FFF1F2", stroke="#F43F5E", font_color="#881337", rounded=1)
    c_hw_nhi = p1.add_card("<b>Howard NHI 身分與意圖審計中樞</b>\n機器身分生命週期憑證管理\n• 防代理混淆 (Confused Deputy)\n• 推論鏈 Intent Auditability 存證", l2, 875, 42, 265, 120, fill="#FFF1F2", stroke="#F43F5E", font_color="#881337", rounded=1)
    c_hw_obs = p1.add_card("<b>Howard AI 全鏈路可觀測中樞</b>\nLangfuse + OpenTelemetry 深度整合\n• Latency・Error・Token 全方位追蹤\n• 異常調用即時警報與分流", l2, 1160, 42, 240, 120, fill="#FFF1F2", stroke="#F43F5E", font_color="#881337", rounded=1)

    # Layer 3: Enterprise AI Agent Platform & RAG (h=185)
    l3 = p1.add_swimlane("【企業級 AI 核心平台】Enterprise GPT & Agent Platform Ecosystem", 50, 480, 1420, 185, fill="#FAF5FF", stroke="#8B5CF6", font_color="#581C87")
    c_momo_gpt = p1.add_card("<b>Enterprise GPT 企業大腦平台</b>\n企業內部專屬 LLM 互動平台\n• 內部法規 FAQ 與公文自動起草\n• 跨部門知識問答檢索助手", l3, 20, 42, 265, 125, fill="#FFFFFF", stroke="#8B5CF6", shape="component")
    c_agent_flow = p1.add_card("<b>AI Agent Workflow 引擎</b>\n多代理協同架構・任務拆解排程\n• Stateful ReAct / Plan-and-Solve 循環\n• 自動上下文維護與狀態轉移", l3, 305, 42, 265, 125, fill="#FFFFFF", stroke="#8B5CF6", shape="component")
    c_rag_core = p1.add_card("<b>全鏈路 RAG 檢索增強系統</b>\n多路召回 (語意向量 + 關鍵字重排)\n• 企業級文件智慧解析與切片\n• 商品目錄與制度規章知識庫", l3, 590, 42, 265, 125, fill="#FFFFFF", stroke="#8B5CF6", shape="component")
    c_mcp_hub = p1.add_card("<b>MCP (Model Context Protocol) 工具中樞</b>\n標準化外部工具動態調用協定\n• ERP / WMS / CRM / 訂單資料庫介接\n• 權限隔離沙箱與參數校驗", l3, 875, 42, 265, 125, fill="#FFFFFF", stroke="#8B5CF6", shape="component")
    c_fine_tune = p1.add_card("<b>模型選型與微調 Pipeline</b>\n領域專有語意微調 (LoRA / SFT)\n• 開源大模型領域適配 (Domain LLM)\n• 效能評估驗證與基準測試", l3, 1160, 42, 240, 125, fill="#FFFFFF", stroke="#8B5CF6", shape="component")

    # Layer 4: Compute & Models (h=195)
    l4 = p1.add_swimlane("【混合算力與模型推論調度層】Hybrid Cloud & On-Premises AIDC Computing Center", 50, 680, 1420, 195, fill="#ECFDF5", stroke="#10B981", font_color="#065F46")
    c_cloud_models = p1.add_card("<b>公有雲商用模型 API (GCP / AWS)</b>\n• Google Gemini 2.5 Pro (Vertex AI)\n• Anthropic Claude 3.7 Sonnet (Bedrock)\n• OpenAI GPT-4o / O3 模型端點\n• 支援雙 11 大促突發流量彈性擴容", l4, 20, 42, 265, 135, fill="#FFFFFF", stroke="#10B981")
    c_k8s_sched = p1.add_card("<b>Kubernetes GPU 調度中樞 (AIDC)</b>\n• Volcano 智慧排程器 (Priority Queue)\n• NVIDIA MIG 資源切片硬體虛擬化\n• 多租戶命名空間隔離與配額限制\n• 基于 Queue 深度觸發自動擴縮 (HPA)", l4, 305, 42, 265, 135, fill="#FFFFFF", stroke="#10B981")
    c_vllm_cluster = p1.add_card("<b>高效能推論服務叢集 (vLLM / Triton)</b>\n• 開源模型：Llama 3.3 / Qwen / DeepSeek\n• PagedAttention 記憶體快取最佳化\n• Continuous Batching 並行處理\n• FP8 / INT4 模型量化降低推論延遲", l4, 590, 42, 265, 135, fill="#FFFFFF", stroke="#10B981")
    c_gpu_infra = p1.add_card("<b>地端 AIDC GPU 硬體基礎設施</b>\n• NVIDIA H100/H200 / AMD MI300X 叢集\n• 400G RoCE v2 GPUDirect RDMA 無損網路\n• NVMe-oF 高速分散式平行檔案系統\n• 資料 100% 地端留存，降低 40% 租賃成本", l4, 875, 42, 265, 135, fill="#FFFFFF", stroke="#10B981")
    c_data_lake = p1.add_card("<b>企業資料中樞與向量儲存</b>\n• Milvus / Qdrant 高效向量索引\n• Enterprise Lakehouse (BigQuery/S3)\n• 行層級安全 (RLS) 與資料實體隔離\n• 機密資料加密防洩漏防護", l4, 1160, 42, 240, 135, fill="#FFFFFF", stroke="#10B981", shape="cylinder")

    # Layer 5: Foundation Security & Post-Quantum Defense (h=195)
    l5 = p1.add_swimlane("【Howard 端點現代周界、供應鏈防禦與後量子密碼學底座】Enterprise Browser, Supply Chain & Quantum-Safe", 50, 890, 1420, 195, fill="#FFFBEB", stroke="#D97706", font_color="#78350F")
    c_hw_browser = p1.add_card("<b>Howard Enterprise Browser</b>\n安全企業瀏覽器底座 + Wings AI Risk Engine\n• 保護瀏覽器外掛・IDE 擴充套件安全\n• MCP 外部工具現代軟體周界全面監管\n• 在端點下載前即刻完成封鎖隔離", l5, 20, 42, 265, 135, fill="#FFFFFF", stroke="#D97706")
    c_hw_5stage = p1.add_card("<b>Howard 5 階供應鏈防禦鏈</b>\n阻斷類似 Shai-Hulud 自動化供應鏈投毒\n• 1. 入口攔截 ➔ 2. Runtime 行為防護\n• 3. 憑證保護 ➔ 4. CI/CD 冷卻緩衝 (72h)\n• 5. 持續硬隔離收容爆炸半徑", l5, 305, 42, 265, 135, fill="#FFFFFF", stroke="#D97706")
    c_hw_cbom = p1.add_card("<b>Howard Dynamic CBOM 清冊</b>\n全企業密碼技術資產動態清冊\n• 自動盤點加密套件、憑證與金鑰長度\n• AI 評估老舊設備與印表機 PQC 就緒度\n• 動態輸出持續可稽核密碼學地圖", l5, 590, 42, 265, 135, fill="#FFFFFF", stroke="#D97706")
    c_hw_crypto = p1.add_card("<b>Howard Crypto Agility 四階閉環</b>\n密碼學敏捷性完整治理落地\n• 1. Howard NGFW 發現 ➔ 2. 多維風險評估\n• 3. 政策自動下發 / 密碼轉譯中繼防護\n• 4. NIST PQC 國際標準合規報告", l5, 875, 42, 265, 135, fill="#FFFFFF", stroke="#D97706")
    c_hw_hndl = p1.add_card("<b>後量子防禦 (PQC Readiness)</b>\n防範「先截獲、後解密」(HNDL) 長期危機\n• 符合 NIST FIPS 203/204/205 標準\n• ML-KEM / ML-DSA 後量子演算法支援\n• 確保商業機密與個資 10+ 年抗破譯能力", l5, 1160, 42, 240, 135, fill="#FFFFFF", stroke="#D97706", shape="hexagon")

    # Layer 6: Infra & Automation (h=160)
    l6 = p1.add_swimlane("【Infra 平台工程與維運自動化】Platform Engineering, GitOps & SRE Reliability", 50, 1100, 1420, 160, fill="#F1F5F9", stroke="#475569", font_color="#1E293B")
    p1.add_card("GitOps & 宣告式交付\n• ArgoCD + Terraform 雲地 IaC 部署\n• 基礎設施全版本受控、稽核可追蹤", l6, 20, 42, 265, 100, fill="#FFFFFF", stroke="#475569")
    p1.add_card("自動化安全 CI/CD 流水線\n• 整合靜態代碼分析 (SAST) 與依賴掃描\n• 漏洞風險門檻強制中斷阻斷機制", l6, 305, 42, 265, 100, fill="#FFFFFF", stroke="#475569")
    p1.add_card("SRE 智慧維運與告警分流\n• AIOps 根因分析・異常自我修復\n• 智慧降噪與事件自動調查排除", l6, 590, 42, 265, 100, fill="#FFFFFF", stroke="#475569")
    p1.add_card("業務連續性與災難復原 (BCP)\n• 跨雲資料非同步抄寫・地端機房備援\n• 目標 RTO &lt; 1hr, RPO ≈ 0 營運韌性", l6, 875, 42, 265, 100, fill="#FFFFFF", stroke="#475569")
    p1.add_card("雙員工治理與規範手冊\n• 人類員工 vs. 數位員工規則分流管轄\n• 嚴格落實 ISO 27001 / ISO 42001", l6, 1160, 42, 240, 100, fill="#FFFFFF", stroke="#475569")

    # Connectors
    p1.add_edge(c_momo_web, c_hw_airs, "HTTPS / User Prompt", stroke="#0284C7")
    p1.add_edge(c_hw_airs, c_hw_gateway, "Sanitized Request", stroke="#EF4444")
    p1.add_edge(c_hw_gateway, c_agent_flow, "Route to Agent", stroke="#8B5CF6")
    p1.add_edge(c_agent_flow, c_rag_core, "Retrieve Knowledge", stroke="#8B5CF6")
    p1.add_edge(c_agent_flow, c_mcp_hub, "Invoke Tools", stroke="#8B5CF6")
    p1.add_edge(c_agent_flow, c_k8s_sched, "Inference Demand", stroke="#10B981")
    p1.add_edge(c_k8s_sched, c_vllm_cluster, "Dispatch GPUs", stroke="#10B981")
    p1.add_edge(c_hw_browser, c_hw_5stage, "Enforce Inspection", stroke="#D97706")
    p1.add_edge(c_hw_cbom, c_hw_crypto, "Trigger Agility Loop", stroke="#D97706")


    # =========================================================================
    # PAGE 2: Howard AI Agent 意圖審計與防混淆代理流程圖
    # =========================================================================
    p2 = builder.add_page("p2_intent_audit", "2. Howard AI Agent 意圖審計與防混淆代理流程", 1520, 1060)
    p2.add_banner(
        "Howard AI Agent 意圖審計 (Intent Auditability) 與防混淆代理人 (Confused Deputy) 防護流程",
        "解決間接提示詞注入 (Indirect Prompt Injection)、非人類身分 (NHI) 權限擴大與不可審計痛點",
        "Howard Liao Ph.D.", x=50, y=20, w=1420, h=65
    )

    col_w = 340
    box_in = p2.add_swimlane("1. 請求輸入與上下文載入 (Input & Context)", 50, 100, col_w, 900, fill="#F0F9FF", stroke="#0284C7", font_color="#0369A1")
    u_prompt = p2.add_card("<b>使用者 Prompt 或業務觸發事件</b>\n• 終端消費者前台對話請求\n• 內部同仁審批作業指示\n• 外部系統 Webhook 觸發事件", box_in, 20, 50, col_w-40, 125, fill="#FFFFFF", stroke="#0284C7")
    ext_data = p2.add_card("<b>外部檢索資料 / 第三方網頁</b>\n• 供應商外部 API 回應\n• 爬蟲與未受信任外部網頁\n<b>⚠️ 潛藏間接提示詞注入 (Prompt Injection)</b>", box_in, 20, 195, col_w-40, 135, fill="#FEF2F2", stroke="#EF4444", font_color="#991B1B")
    nhi_cred = p2.add_card("<b>非人類身分 (NHI) 特權憑證</b>\n• Agent 專用短期 STS Token\n• MCP Tool 調用授權金鑰\n• 最小權限 Service Account 角色", box_in, 20, 350, col_w-40, 125, fill="#FFFFFF", stroke="#0284C7")
    state_ctx = p2.add_card("<b>執行環境記憶 (Session Context)</b>\n• 短期交談歷程 (Chat History)\n• Agent 當前狀態與變數槽位\n• 任務初始目標約束錨定", box_in, 20, 495, col_w-40, 125, fill="#FFFFFF", stroke="#0284C7")

    box_sec = p2.add_swimlane("2. Howard 核心安全防護中樞 (Howard Security Guardrails)", 410, 100, col_w, 900, fill="#FEF2F2", stroke="#EF4444", font_color="#991B1B")
    hw_air_in = p2.add_card("<b>Howard Prisma AIRS 核心閘門</b>\n• 語意安全過濾與惡意語法攔截\n• 客戶隱私個資 (PII) 自動遮蔽去識別\n• 越獄與敏感詞動態偵測即刻阻斷", box_sec, 20, 50, col_w-40, 125, fill="#FFF1F2", stroke="#F43F5E", font_color="#881337")
    hw_deputy = p2.add_card("<b>Howard 防混淆代理防護 (Anti-Confused Deputy)</b>\n• 嚴格區隔「指令通道」與「資料通道」\n• 標記不可信外部資料，防止誘騙挾持\n• 阻斷攻擊者利用 Agent 特權呼叫工具", box_sec, 20, 195, col_w-40, 135, fill="#FFF1F2", stroke="#F43F5E", font_color="#881337")
    hw_verify = p2.add_card("<b>Howard 意圖驗證引擎 (Intent Verifier)</b>\n• 比對 Agent 工具呼叫是否符合原始目標\n• 參數合理性與資料敏感度動態檢驗\n• 越權調用即刻熔斷攔截並告警", box_sec, 20, 350, col_w-40, 125, fill="#FFF1F2", stroke="#F43F5E", font_color="#881337")
    hw_wings = p2.add_card("<b>Howard Wings AI Risk Engine</b>\n• 即時評估 MCP 工具之安全信譽評等\n• 動態監控 API 請求頻率與封包特徵\n• 阻斷未經認證之外部 MCP 服務呼叫", box_sec, 20, 495, col_w-40, 125, fill="#FFF1F2", stroke="#F43F5E", font_color="#881337")
    hw_log = p2.add_card("<b>Howard 推論鏈審計存證 (Provenance)</b>\n• 完整記錄「Agent 因何推論而決定調用」\n• 留存可解釋之思維鏈 (Reasoning Trace)\n• 具備法律不可否認性之完整稽核日誌", box_sec, 20, 640, col_w-40, 125, fill="#FFF1F2", stroke="#F43F5E", font_color="#881337")

    box_agent = p2.add_swimlane("3. AI Agent 決策推論核心 (Reasoning)", 770, 100, col_w, 900, fill="#FAF5FF", stroke="#8B5CF6", font_color="#581C87")
    core_llm = p2.add_card("<b>Enterprise GPT / 開源 vLLM 核心</b>\n• 接收消毒後之 Prompt 與系統指令\n• 任務邏輯拆解與推理 (Reasoning)\n• 擬定下一步執行方案 (Action Plan)", box_agent, 20, 50, col_w-40, 125, fill="#FFFFFF", stroke="#8B5CF6", shape="component")
    act_step = p2.add_card("<b>Action 決定與參數生成</b>\n• 指定欲調用之 MCP 工具名稱\n• 自動組裝 JSON Schema 調用參數\n• 向安全中樞發起調用宣告請求", box_agent, 20, 195, col_w-40, 125, fill="#FFFFFF", stroke="#8B5CF6", shape="component")
    hitl_gate = p2.add_card("<b>高風險操作人機介入 (HITL Gate)</b>\n• 金融交易轉帳 / 大額請款\n• 資料庫刪除 / 生產組態變更\n• <b>強制啟動主管雙人簽核 (Dual Approval)</b>", box_agent, 20, 340, col_w-40, 135, fill="#4A044E", stroke="#C026D3", font_color="#F5D0FE")
    res_agg = p2.add_card("<b>結果聚合與最終輸出生成</b>\n• 接收工具執行結果並驗證真實性\n• 生成給使用者之高質量專業回覆\n• 關閉工作工作階段並釋放 Token", box_agent, 20, 495, col_w-40, 125, fill="#FFFFFF", stroke="#8B5CF6")

    box_tool = p2.add_swimlane("4. 工具執行與後端系統 (Execution & Systems)", 1130, 100, col_w, 900, fill="#ECFDF5", stroke="#10B981", font_color="#065F46")
    mcp_tool_1 = p2.add_card("<b>WMS / ERP 核心業務系統</b>\n• 即時庫存查詢與鎖定\n• 訂單出貨排程與狀態更新\n• 物流供應鏈派工自動化", box_tool, 20, 50, col_w-40, 125, fill="#FFFFFF", stroke="#10B981")
    mcp_tool_2 = p2.add_card("<b>HR 人資 / 財務系統 API</b>\n• 請款單據立案與審批流程\n• 員工考勤資料彙總與分析\n• 企業差旅預算自動核銷", box_tool, 20, 195, col_w-40, 125, fill="#FFFFFF", stroke="#10B981")
    mcp_tool_3 = p2.add_card("<b>智慧搜尋與推薦資料庫</b>\n• 商品語意嵌入特徵向量庫\n• 即時動態比價資料庫\n• 個人化推薦偏好快照", box_tool, 20, 340, col_w-40, 125, fill="#FFFFFF", stroke="#10B981")
    mcp_tool_4 = p2.add_card("<b>雲地混合資料庫 / 向量庫</b>\n• PostgreSQL / BigQuery / Milvus\n• 行層級安全 (RLS) 權限隔離\n• 零信任存取閘道全面保護", box_tool, 20, 485, col_w-40, 125, fill="#FFFFFF", stroke="#10B981", shape="cylinder")
    audit_db = p2.add_card("<b>不可否認性合規審計日誌</b>\n• 符合 ISO 27001 / ISO 42001 標準\n• WORM (一次寫入多次讀取) 防竄改\n• 完整保存 Agent 決策法律責任歸屬", box_tool, 20, 630, col_w-40, 125, fill="#FFFFFF", stroke="#10B981", shape="cylinder")

    # Connectors
    p2.add_edge(u_prompt, hw_air_in, "檢送對話內容", stroke="#0284C7")
    p2.add_edge(ext_data, hw_deputy, "外部輸入校驗", stroke="#EF4444")
    p2.add_edge(hw_air_in, core_llm, "消毒後 Prompt", stroke="#8B5CF6")
    p2.add_edge(core_llm, act_step, "生成調用決策", stroke="#8B5CF6")
    p2.add_edge(act_step, hw_verify, "提報執行意圖", stroke="#EF4444")
    p2.add_edge(hw_verify, hw_deputy, "比對目標一致性", stroke="#EF4444")
    p2.add_edge(hw_deputy, hitl_gate, "低風險核准 / 高風險攔截", stroke="#8B5CF6")
    p2.add_edge(hitl_gate, hw_wings, "通過授權驗證", stroke="#EF4444")
    p2.add_edge(hw_wings, mcp_tool_1, "放行安全 MCP 調用", stroke="#10B981")
    p2.add_edge(hw_wings, hw_log, "同步推論日誌", stroke="#D97706")
    p2.add_edge(hw_log, audit_db, "寫入合規儲存", stroke="#10B981")


    # =========================================================================
    # PAGE 3: Howard 5 階軟體供應鏈與 MCP 防禦架構圖
    # =========================================================================
    p3 = builder.add_page("p3_supply_chain", "3. Howard 5 階供應鏈與 MCP 防禦鏈", 1520, 1020)
    p3.add_banner(
        "Howard 5 階現代軟體周界與 MCP 供應鏈防禦鏈架構圖 (阻斷類似 Shai-Hulud 投毒攻擊)",
        "治理範疇：瀏覽器外掛、IDE 擴充套件、MCP Tools、開源套件、模型 Weights 與 CI/CD 管道",
        "Howard Liao Ph.D.", x=50, y=20, w=1420, h=65
    )

    col_w = 270
    spacing = 16
    start_x = 50

    stages = [
        ("第 1 階：Shift-Left 入口攔截", "Howard KOI 內嵌安全閘道", "#7F1D1D", "#DC2626", "#FECACA",
         "防護核心目標\n在擴充功能與工具下載「觸及端點前」即時封鎖，不給任何落地機會。",
         "防禦主要對象\n• VS Code / Cursor 擴充套件\n• 瀏覽器 Chrome/Edge 外掛\n• 開源 Python 套件 (PyPI/npm)\n• 外部未授權開源 MCP Server",
         "關鍵技術機制\n• Howard 內嵌網路閘道攔截\n• 套件封包指紋與動態雜湊比對\n• 影子擴充套件即時阻斷\n• 企業私有套件 Proxy 白名單"),
        ("第 2 階：Runtime 行為防護", "Howard 執行階段防護", "#78350F", "#D97706", "#FEF3C7",
         "防護核心目標\n阻斷惡意程式碼、權限越權與工具惡意行為，嚴格限縮沙箱與容器邊界。",
         "防禦主要對象\n• 容器逃逸 (Container Escape)\n• 非法外連 C2 中繼站\n• 未授權磁碟或記憶體讀寫\n• 惡意注入的 Subprocess 行為",
         "關鍵技術機制\n• Howard Enterprise Browser 安全探針\n• eBPF 核心級系統呼叫即時監控\n• 最小權限 SELinux / AppArmor\n• 記憶體動態注入偵測阻斷"),
        ("第 3 階：憑證與管道防護", "Howard 憑證與防洩中樞", "#581C87", "#9333EA", "#F3E8FF",
         "防護核心目標\n防禦開發環境遭竊聽、API Key 與 Token 外洩，收攏 NHI 特權憑證。",
         "防禦主要對象\n• 本地 .env 與 config 敏感檔\n• 記憶體殘留的雲端 Token\n• Git Commit 誤提交金鑰\n• CI/CD 變數與 Runner 快取",
         "關鍵技術機制\n• Howard 機密掃描引擎 (Pre-Commit)\n• 記憶體加密防 Memory Dumper\n• 短生命週期動態憑證 (STS)\n• 特權存取管理 (PAM) 嚴格隔離"),
        ("第 4 階：CI/CD 冷卻緩衝", "Howard 版本更新緩衝機制", "#1E3A8A", "#2563EB", "#DBEAFE",
         "防護核心目標\n在自動部署管道設置冷卻期與審查機制，阻止全自動流水線武器化。",
         "防禦主要對象\n• 自動更新機制的「即時投毒」\n• 上游相依套件的小版本惡意改動\n• 開源維護者帳號遭挾持\n• Shai-Hulud 模式自動感染",
         "關鍵技術機制\n• 72 小時版本發布冷卻緩衝期\n• 主管雙人簽核 (Dual Approval)\n• 隔離沙箱自動回歸測試\n• SBOM 依賴版本鎖定 (Lockfile)"),
        ("第 5 階：持續補救與硬隔離", "Howard 持續微隔離與復原", "#064E3B", "#059669", "#D1FAE5",
         "防護核心目標\n第一時間隔離受感染裝置，收容爆炸半徑，自動化快速復原生產。",
         "防禦主要對象\n• 內部橫向移動 (Lateral Movement)\n• 跨網路區段非授權探測\n• 憑證外洩後的持續駐留\n• 機密資料巨量外傳 (Exfiltration)",
         "關鍵技術機制\n• Howard 一鍵網路微隔離 (Microseg)\n• 快速撤銷被駭 NHI 憑證與 Key\n• 機器人自動化鑑識 (SOAR)\n• 容器與虛擬機無損回滾 Snapshot")
    ]

    for idx, (st_title, st_sub, bg_col, stroke_col, text_col, c1, c2, c3) in enumerate(stages):
        cur_x = start_x + idx * (col_w + spacing)
        lane_id = p3.add_swimlane(st_title, cur_x, 100, col_w, 860, fill=bg_col, stroke=stroke_col, font_color=text_col)
        
        # Subtitle banner inside lane
        p3.add_card(f"<b>{st_sub}</b>", lane_id, 15, 45, col_w-30, 40, fill=stroke_col, stroke=stroke_col, font_color="#FFFFFF")
        
        # 3 Cards with generous heights
        p3.add_card(c1, lane_id, 15, 100, col_w-30, 125, fill="#18181B", stroke=stroke_col, font_color=text_col)
        p3.add_card(c2, lane_id, 15, 245, col_w-30, 155, fill="#18181B", stroke=stroke_col, font_color=text_col)
        p3.add_card(c3, lane_id, 15, 420, col_w-30, 155, fill="#18181B", stroke=stroke_col, font_color=text_col)


    # =========================================================================
    # PAGE 4: 混合雲與地端 AIDC GPU 調度拓撲圖
    # =========================================================================
    p4 = builder.add_page("p4_aidc_hybrid", "4. 混合雲與地端 AIDC GPU 調度拓撲", 1520, 1060)
    p4.add_banner(
        "企業混合雲 (GCP/AWS) 與地端 AIDC 綠能運算中心 GPU 資源調度拓撲圖",
        "涵蓋 K8s 資源排程、GPU MIG 切片、多租戶隔離、vLLM 推論服務與 Token 成本計費優化",
        "Howard Liao Ph.D.", x=50, y=20, w=1420, h=65
    )

    w_zone = 450
    box_cloud = p4.add_swimlane("【公有雲彈性算力層】Public Cloud (GCP Vertex AI / AWS Bedrock)", 50, 100, w_zone, 890, fill="#F0F9FF", stroke="#0284C7", font_color="#0369A1")
    p4.add_card("<b>Google Cloud (GCP) 平台</b>\n• Vertex AI (Gemini 2.5 Flash / Pro 推論)\n• Google Cloud Storage 巨量備份湖\n• BigQuery 巨量分析與即時特徵工程\n• 專用跨國高速骨幹網路", box_cloud, 20, 50, w_zone-40, 140, fill="#FFFFFF", stroke="#0284C7")
    p4.add_card("<b>Amazon Web Services (AWS) 平台</b>\n• AWS Bedrock (Claude 3.7 Sonnet 推論)\n• S3 物件儲存與異地雙向即時抄寫\n• 彈性突增流量 GPU 實例 (G5/P5 節點)\n• 企業級高可用容錯架構", box_cloud, 20, 210, w_zone-40, 140, fill="#FFFFFF", stroke="#0284C7")
    p4.add_card("<b>公有雲主要適用情境</b>\n• 超大長文本 (Long-Context) 深度理解與跨國語意\n• 雙 11 / 年終大促高峰突增算力彈性擴容\n• 尖端商用前瞻模型能力即時 PoC 驗證\n• 降低非尖峰期閒置硬體資本支出", box_cloud, 20, 370, w_zone-40, 150, fill="#FFFFFF", stroke="#0284C7")
    p4.add_card("<b>專用加密傳輸通道</b>\n• AWS Direct Connect / GCP Interconnect 專線\n• Howard NGFW 端點全流量清洗與防護\n• IPSec VPN 後量子加密通道保護", box_cloud, 20, 540, w_zone-40, 140, fill="#FFFFFF", stroke="#0284C7")

    box_k8s = p4.add_swimlane("【K8s 核心調度中樞】Kubernetes Orchestration & GPU Scheduling", 535, 100, w_zone, 890, fill="#FAF5FF", stroke="#8B5CF6", font_color="#581C87")
    k8s_sched = p4.add_card("<b>K8s 智慧排程器 (Volcano / Kube-Scheduler)</b>\n• 多維度資源感知排程 (GPU Memory / Compute)\n• Priority & Preemption 高優先權插隊搶佔機制\n• 拓撲感知 (NUMA / PCIe / NVLink) 就近親和排程\n• 確保 GPU 運算資源高負載均衡", box_k8s, 20, 50, w_zone-40, 140, fill="#FFFFFF", stroke="#8B5CF6")
    k8s_mig = p4.add_card("<b>GPU 資源切片虛擬化 (MIG / vGPU)</b>\n• NVIDIA Multi-Instance GPU (1g.10gb / 2g.20gb)\n• 輕量級推論任務高密度混部提升利用率\n• 硬體層級嚴格記憶體與算力沙箱隔離\n• 靈活支援不同參數量之模型調度", box_k8s, 20, 210, w_zone-40, 140, fill="#FFFFFF", stroke="#8B5CF6")
    k8s_tenant = p4.add_card("<b>多租戶配額與計費 (Multi-Tenancy & FinOps)</b>\n• 部門命名空間隔離 (HR, Finance, Operations)\n• ResourceQuota 與 LimitRange 嚴格限額控管\n• <b>Howard FinOps 即時用量計費 (Chargeback) 看板</b>\n• 支援自動化降級與限額保護機制", box_k8s, 20, 370, w_zone-40, 150, fill="#FFFFFF", stroke="#8B5CF6")
    k8s_vllm = p4.add_card("<b>推論服務叢集 (vLLM / Triton Pods)</b>\n• HPA (Horizontal Pod Autoscaler) 自動彈性擴縮\n• 根據 Queue 深度與 Latency 觸發冷啟動\n• 模型權重熱載入快取 (Model Weight Caching)\n• PagedAttention 大幅減少顯存碎片浪費", box_k8s, 20, 540, w_zone-40, 140, fill="#FFFFFF", stroke="#8B5CF6")

    box_aidc = p4.add_swimlane("【地端 AIDC GPU 硬體機房】On-Premises AI Data Center Infrastructure", 1020, 100, w_zone, 890, fill="#ECFDF5", stroke="#10B981", font_color="#065F46")
    p4.add_card("<b>高效能運算伺服器機櫃</b>\n• NVIDIA H100 / H200 SXM5 節點叢集\n• AMD Instinct MI300X 高性價比替代節點\n• 專屬高效能浸沒式/液冷散熱機櫃系統\n• 實現綠能 PUE &lt; 1.25 高能效指標", box_aidc, 20, 50, w_zone-40, 140, fill="#FFFFFF", stroke="#10B981")
    p4.add_card("<b>高速低延遲無損網路拓撲</b>\n• 400Gbps RoCE v2 / InfiniBand Spine-Leaf 架構\n• GPUDirect RDMA (跨伺服器 GPU 記憶體直通)\n• 零封包遺失 (PFC + ECN 壅塞控制)\n• 極致加速分散式並行推論與訓練", box_aidc, 20, 210, w_zone-40, 140, fill="#FFFFFF", stroke="#10B981")
    p4.add_card("<b>超高速分散式平行儲存架構</b>\n• NVMe-oF 全閃存快顯資料儲存池\n• Lustre / Ceph / Weka 高 IOPS 分散式檔案系統\n• 模型權重秒級並行同步與 Checkpoint 快照\n• 支援高併發向量搜尋特徵抽取", box_aidc, 20, 370, w_zone-40, 150, fill="#FFFFFF", stroke="#10B981", shape="cylinder")
    p4.add_card("<b>地端 AIDC 核心業務效益</b>\n• 機密資料 100% 不落地公有雲，徹底落實合規\n• 長期推論大幅降低 40%~60% 雲端 Token 租用成本\n• 毫秒級極致內部系統推論響應延遲\n• 掌握企業核心自主算力主權", box_aidc, 20, 540, w_zone-40, 140, fill="#FFFFFF", stroke="#10B981")

    # Connectors
    p4.add_edge(k8s_sched, k8s_mig, "動態切分資源", stroke="#8B5CF6")
    p4.add_edge(k8s_mig, k8s_vllm, "分配 GPU 切片", stroke="#8B5CF6")
    p4.add_edge(k8s_vllm, box_aidc, "執行於 AIDC 裸金屬機群", stroke="#10B981")


    # =========================================================================
    # PAGE 5: Howard 後量子密碼學敏捷性四階閉環圖
    # =========================================================================
    p5 = builder.add_page("p5_crypto_agility", "5. Howard 後量子密碼學敏捷性閉環", 1520, 1060)
    p5.add_banner(
        "Howard 後量子安全 (Quantum-Safe) 與密碼學敏捷性 (Crypto Agility) 四階閉環圖",
        "防禦「先截獲、後解密」(Harvest Now, Decrypt Later, HNDL) 威脅，符合 NIST PQC 國家安全標準",
        "Howard Liao Ph.D.", x=50, y=20, w=1420, h=65
    )

    col_w = 340
    q1 = p5.add_swimlane("第 1 階：持續發現與動態盤點 (Continuous Discovery)", 50, 100, col_w, 860, fill="#F0F9FF", stroke="#0284C7", font_color="#0369A1")
    p5.add_card("<b>Howard Dynamic CBOM 引擎</b>\n建立全企業加密套件、憑證、金鑰長度\n與硬體演算能力的動態資產清冊\n實現加密資產即時可視化地圖", q1, 20, 50, col_w-40, 135, fill="#FFFFFF", stroke="#0284C7")
    p5.add_card("<b>Howard NGFW 流量自動嗅探</b>\n利用全網防火牆與日誌流量\n自動擷取所有傳輸中裝置的密碼情境\n精準識別弱加密與過期 TLS 協議", q1, 20, 205, col_w-40, 135, fill="#FFFFFF", stroke="#0284C7")
    p5.add_card("<b>AI 驅動的 PQC 就緒度分析</b>\n精確識別老舊印表機、產線設備、舊伺服器\n無法運行 PQC 的弱點，建議硬體汰換\n產出硬體生命週期升級建議報告", q1, 20, 360, col_w-40, 140, fill="#FFFFFF", stroke="#0284C7")

    q2 = p5.add_swimlane("第 2 階：多維風險評估與優先級 (Risk & Prioritization)", 410, 100, col_w, 860, fill="#FFFBEB", stroke="#D97706", font_color="#78350F")
    p5.add_card("<b>三維情資關聯矩陣</b>\n• 傳輸中加密強度 (Cipher Suite)\n• CMDB 資產關鍵性 (Asset Criticality)\n• SCM 資料機密敏感度 (Data Sensitivity)\n綜合量化全集團加密資產風險", q2, 20, 50, col_w-40, 145, fill="#FFFFFF", stroke="#D97706")
    p5.add_card("<b>HNDL 暴露風險評分模型</b>\n針對存活期長達 10+ 年之商業機密與個資\n計算暴露時間窗，標記最高緊急修復等級\n防範未來量子運算威脅", q2, 20, 215, col_w-40, 135, fill="#FFFFFF", stroke="#D97706")
    p5.add_card("<b>PQC 遷移優先排程與波次</b>\n依業務影響度自動生成波次 (Waves)\n產出跨部門遷移甘特圖與落地時程建議\n動態追蹤修復預算與人力資源", q2, 20, 370, col_w-40, 140, fill="#FFFFFF", stroke="#D97706")

    q3 = p5.add_swimlane("第 3 階：修復、處置與中繼防護 (Remediation & Translation)", 770, 100, col_w, 860, fill="#FEF2F2", stroke="#EF4444", font_color="#991B1B")
    p5.add_card("<b>Howard 政策一鍵自動下發</b>\n對 Howard NGFW、GlobalProtect、Prisma Access\n一鍵啟用量子安全演算法政策\n秒級完成全網安全邊界升級", q3, 20, 50, col_w-40, 135, fill="#FFFFFF", stroke="#EF4444")
    p5.add_card("<b>Howard 密碼轉譯中繼防護\n(Cipher Translation Proxy)</b>\n針對無法升級演算法的老舊系統與設備\n由邊緣閘道進行雙向加密轉譯，實現無痛中繼防護\n延長老舊資產合規服役壽命", q3, 20, 205, col_w-40, 145, fill="#FFF1F2", stroke="#EF4444", font_color="#881337")
    p5.add_card("<b>第三方軟硬體遷移指南</b>\n為企業生態圈外部合作供應商\n產出標準 PQC API 介接規範與升級合規指引\n建立供應鏈量子安全防禦統一戰線", q3, 20, 370, col_w-40, 140, fill="#FFFFFF", stroke="#EF4444")

    q4 = p5.add_swimlane("第 4 階：持續治理與動態合規 (Governance & Compliance)", 1130, 100, col_w, 860, fill="#ECFDF5", stroke="#10B981", font_color="#065F46")
    p5.add_card("<b>常態化密碼學衛生 (Hygiene)</b>\n持續追蹤即將過期或已被破解之傳統演算法\n自動化更新動態停用黑名單\n確保全網密碼資產常保健康狀態", q4, 20, 50, col_w-40, 135, fill="#FFFFFF", stroke="#10B981")
    p5.add_card("<b>國際標準稽核報告 (Audit-Ready)</b>\n自動生成符合 NIST PQC (ML-KEM / ML-DSA)\n與國家級資通安全要求的合規審計報告\n大幅降低外部合規查核成本", q4, 20, 205, col_w-40, 135, fill="#FFFFFF", stroke="#10B981")
    p5.add_card("<b>量子抗性持續成熟度指標</b>\n高管儀表板展示全集團 PQC 覆蓋率 (0%~100%)\n協助決策層掌握企業長期量子存亡韌性\n量化呈報董事會與資安委員會", q4, 20, 360, col_w-40, 140, fill="#FFFFFF", stroke="#10B981")

    # Connectors
    p5.add_edge(q1, q2, "輸出 CBOM 與弱點數據", stroke="#0284C7")
    p5.add_edge(q2, q3, "下發遷移與轉譯工單", stroke="#D97706")
    p5.add_edge(q3, q4, "回報修復狀態", stroke="#EF4444")
    p5.add_edge(q4, q1, "反饋常態監控巡檢", stroke="#10B981", style_extra="curved=1;")

    builder.save()

if __name__ == "__main__":
    out_file1 = "/Users/howardliao/Desktop/HermesAgent/Temp/Enterprise_AI_Architect_Howard_Security_Architecture.drawio"
    out_file2 = "/Users/howardliao/Desktop/HermesAgent/Temp/momo_AI_Architect_Howard_Security_Architecture.drawio"
    build_all_diagrams(out_file1)
    build_all_diagrams(out_file2)
