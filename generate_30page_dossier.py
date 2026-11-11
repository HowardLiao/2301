#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate 30-Page Comprehensive Executive Interview Dossier (.docx)
Tailored exclusively for: LITE-ON Technology Corporation (光寶科技 · 2301.TW)
Audience: 董事長 (Chairman) ｜ 資訊長 李逢堉 (CIO) ｜ 面試審查委員會
Candidate: Howard Liao Ph.D. (廖倫豪 博士)
Role: (NEW!) IT AI 平台負責人 (Global Head of Enterprise AI Strategy & Platform)
Design: Milan Warm Amber (米蘭暖琥珀風格)
Constraint: Pure LITE-ON custom narrative; ZERO external client names or internal repo codes.
"""

import os
import docx
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

BASE_DIR = '/Users/howard/Desktop/HermesAgent/PortFilio/2301'
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
IMG_DIR = os.path.join(ASSETS_DIR, 'docx_img')
OUTPUT_DOCX = os.path.join(BASE_DIR, '光寶科技_IT_AI_平台負責人_面試報告暨高階學經歷_廖倫豪博士.docx')

# Milan Warm Amber Color Palette
HEX_PRIMARY = "B45309"      # 米蘭暖琥珀 Terracotta Amber
HEX_SECONDARY = "78350F"    # 深琥珀干邑 Cognac Amber
HEX_DARK = "292524"         # 曜石深濃縮咖啡 Deep Espresso
HEX_MUTED = "78716C"        # 暖沙石灰 Taupe / Stone Grey
HEX_SURFACE = "FDFBF7"      # 溫潤象牙米白 Warm Ivory Cream
HEX_CARD_BG = "FBF8F3"      # 柔和卡片底色 Soft Cream
HEX_HEADER_BG = "F4EDE4"    # 表頭淺琥珀底 Light Amber Header
HEX_BORDER = "E7E0D8"       # 邊框暖石灰 Warm Border Grey

RGB_PRIMARY = RGBColor(180, 83, 9)
RGB_SECONDARY = RGBColor(120, 53, 15)
RGB_DARK = RGBColor(41, 37, 36)
RGB_MUTED = RGBColor(120, 113, 108)

def set_cell_background(cell, hex_color):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=130, right=130):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_header_banner(doc, page_num, section_title, category_badge, subtitle):
    tbl = doc.add_table(rows=1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(5.6)
    tbl.columns[1].width = Inches(1.6)
    
    cell_left = tbl.cell(0, 0)
    cell_right = tbl.cell(0, 1)
    
    set_cell_background(cell_left, HEX_HEADER_BG)
    set_cell_background(cell_right, HEX_HEADER_BG)
    set_cell_margins(cell_left, top=90, bottom=90, left=130, right=80)
    set_cell_margins(cell_right, top=90, bottom=90, left=80, right=130)
    
    p_left = cell_left.paragraphs[0]
    p_left.paragraph_format.space_before = Pt(0)
    p_left.paragraph_format.space_after = Pt(1)
    
    r_badge = p_left.add_run(f"[{category_badge}] ")
    r_badge.font.name = "Arial"
    r_badge.font.size = Pt(8.5)
    r_badge.font.bold = True
    r_badge.font.color.rgb = RGB_PRIMARY
    
    r_title = p_left.add_run(section_title)
    r_title.font.name = "Songti TC"
    r_title.font.size = Pt(12.5)
    r_title.font.bold = True
    r_title.font.color.rgb = RGB_DARK
    
    if subtitle:
        p_sub = cell_left.add_paragraph()
        p_sub.paragraph_format.space_before = Pt(0)
        p_sub.paragraph_format.space_after = Pt(0)
        r_sub = p_sub.add_run(subtitle)
        r_sub.font.name = "STHeiti Light"
        r_sub.font.size = Pt(8.5)
        r_sub.font.color.rgb = RGB_MUTED
        
    p_right = cell_right.paragraphs[0]
    p_right.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_right.paragraph_format.space_before = Pt(4)
    p_right.paragraph_format.space_after = Pt(0)
    
    r_pg = p_right.add_run(f"PAGE {page_num:02d} / 30")
    r_pg.font.name = "Arial"
    r_pg.font.size = Pt(9.5)
    r_pg.font.bold = True
    r_pg.font.color.rgb = RGB_PRIMARY

    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_before = Pt(2)
    p_spacer.paragraph_format.space_after = Pt(3)

def add_callout(doc, text, title=None, hex_bg=HEX_CARD_BG, hex_border=HEX_PRIMARY):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(7.2)
    
    cell = tbl.cell(0, 0)
    set_cell_background(cell, hex_bg)
    set_cell_margins(cell, top=90, bottom=90, left=150, right=130)
    
    tcPr = cell._element.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="24" w:space="0" w:color="{hex_border}"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(1)
    
    if title:
        r_t = p.add_run(f"✦ {title}\n")
        r_t.font.name = "STHeiti Medium"
        r_t.font.size = Pt(9.5)
        r_t.font.bold = True
        r_t.font.color.rgb = RGB_PRIMARY
        
    r_b = p.add_run(text)
    r_b.font.name = "STHeiti Light"
    r_b.font.size = Pt(9)
    r_b.font.color.rgb = RGB_DARK
    
    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_before = Pt(2)
    p_spacer.paragraph_format.space_after = Pt(2)

def build_30page_dossier():
    doc = docx.Document()

    # Set margins to 0.65 inch for clean 30-page editorial layout
    for section in doc.sections:
        section.top_margin = Inches(0.65)
        section.bottom_margin = Inches(0.65)
        section.left_margin = Inches(0.65)
        section.right_margin = Inches(0.65)

        # Header
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("光寶科技 (2301.TW) 全球 AI 策略與製造中樞演進藍圖 ｜ 高階面試呈報專案報告")
        hrun.font.name = "STHeiti Light"
        hrun.font.size = Pt(8)
        hrun.font.color.rgb = RGB_MUTED

        # Footer
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        frun_l = fp.add_run("報告人：Howard Liao Ph.D. (廖倫豪 博士)  ｜  機密文件 僅供光寶科技董事長、李逢堉資訊長與面試審查團專閱")
        frun_l.font.name = "STHeiti Light"
        frun_l.font.size = Pt(8)
        frun_l.font.color.rgb = RGB_MUTED

    print("Generating 30 Pages...")

    # PAGE 1: Cover
    p_cov_badge = doc.add_paragraph()
    p_cov_badge.paragraph_format.space_before = Pt(30)
    p_cov_badge.paragraph_format.space_after = Pt(6)
    r_cb = p_cov_badge.add_run("LITE-ON TECHNOLOGY CORPORATION · 2301.TW · BOARD & CIO DOSSIER")
    r_cb.font.name = "Arial"
    r_cb.font.size = Pt(9.5)
    r_cb.font.bold = True
    r_cb.font.color.rgb = RGB_PRIMARY

    p_cov_title = doc.add_paragraph()
    p_cov_title.paragraph_format.space_before = Pt(0)
    p_cov_title.paragraph_format.space_after = Pt(12)
    r_ct = p_cov_title.add_run("從單一應用走向製造中樞：\n光寶次世代企業級 AI 平台藍圖、\nS/4HANA-MES 互補架構與價值落地實踐報告")
    r_ct.font.name = "Songti TC"
    r_ct.font.size = Pt(22)
    r_ct.font.bold = True
    r_ct.font.color.rgb = RGB_DARK

    p_cov_sub = doc.add_paragraph()
    p_cov_sub.paragraph_format.space_before = Pt(0)
    p_cov_sub.paragraph_format.space_after = Pt(18)
    r_cs = p_cov_sub.add_run("針對全球 86 家子公司、112 座製造工廠之骨幹升級大戰，深挖「問題背後的問題」，以雙環數據總線貫通替代料選用、齊套料排程與智慧調機")
    r_cs.font.name = "STHeiti Light"
    r_cs.font.size = Pt(10.5)
    r_cs.font.color.rgb = RGB_MUTED

    tbl_cov = doc.add_table(rows=5, cols=2)
    tbl_cov.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_cov.autofit = False
    tbl_cov.columns[0].width = Inches(2.2)
    tbl_cov.columns[1].width = Inches(5.0)

    cov_info = [
        ("應聘目標職缺", "(NEW!) IT AI 平台負責人 (Global Head of Enterprise AI Strategy & Platform)"),
        ("面試呈報對象", "第一關：資訊長 李逢堉 ｜ 技術顧問 ｜ 人資長 (現場)\n第二關：董事長 (現場)"),
        ("報告人", "Howard Liao Ph.D. (廖倫豪 博士) ｜ 資訊管理博士 ｜ 前大型跨國高科技製造集團中央資訊技術處長"),
        ("核心管理實績", "27+ 年 IT & 工程歷練 ｜ 20+ 年 C-Level 治理 ｜ $10M+ 資本對齊 ｜ 100% Zero Outage"),
        ("專案線上互動門戶", "https://howardliao.github.io/2301/ (支援手機 PWA 與桌面親和性 RWD)")
    ]

    for idx, (k, v) in enumerate(cov_info):
        c0 = tbl_cov.cell(idx, 0)
        c1 = tbl_cov.cell(idx, 1)
        set_cell_background(c0, HEX_HEADER_BG)
        set_cell_background(c1, HEX_SURFACE)
        set_cell_margins(c0, top=80, bottom=80, left=110, right=110)
        set_cell_margins(c1, top=80, bottom=80, left=110, right=110)

        p0 = c0.paragraphs[0]
        r0 = p0.add_run(k)
        r0.font.name = "STHeiti Medium"
        r0.font.size = Pt(9)
        r0.font.bold = True
        r0.font.color.rgb = RGB_PRIMARY

        p1 = c1.paragraphs[0]
        r1 = p1.add_run(v)
        r1.font.name = "STHeiti Light"
        r1.font.size = Pt(9)
        r1.font.color.rgb = RGB_DARK

    p_cov_bot = doc.add_paragraph()
    p_cov_bot.paragraph_format.space_before = Pt(40)
    r_bot = p_cov_bot.add_run("裝幀規範：米蘭暖琥珀出版級標準 ｜ 適用體系：TOGAF 10 ADM / ISO 42001 / ISO 27001 / SAP Clean Core")
    r_bot.font.name = "Arial"
    r_bot.font.size = Pt(8.5)
    r_bot.font.color.rgb = RGB_MUTED
    doc.add_page_break()

    # PAGE 2: Letter to Panel & Bento
    add_header_banner(doc, 2, "執行摘要與致光寶面試審查團的一封信", "EXECUTIVE LETTER", "直球回應第一關（CIO、技術顧問、人資長）與第二關（董事長）之核心關切")
    add_callout(doc, 
        "「見招拆招，只能解決眼前這一關。真正的問題，往往藏在問題的背後。」—— 光寶科技資訊長 李逢堉\n"
        "光寶正在打一場硬仗：將全球 86 家公司、112 座工廠的 ERP 升級至 SAP S/4HANA，並於 2027 年 1 月 4 日同步切換。然而，S/4HANA 只是數位骨幹；真正能為光寶帶來看得見的經濟效益、增加製造與供應鏈彈性的，是骨幹之上能主動預測、主動建議的 AI 決策大腦。本人以戰時管理者的責任感，隨時準備與團隊並肩作戰。",
        title="戰略破題：深挖問題背後的結構性根因"
    )
    p_p2 = doc.add_paragraph()
    r_p2 = p_p2.add_run(
        "尊敬的董事長、李逢堉資訊長、技術顧問與人資長：\n"
        "當前企業導入 AI 最常見的陷阱是陷入「零散 POC 自嗨」：各部門各自找工具寫提示詞，產出一堆無法沉澱為資產的玩具，既無法與核心交易系統閉環，又大幅拉高資安外洩與算力浪費風險。\n"
        "光寶需要的是一位 Forward-Deployed AI Architect 兼具 C-Level 治理格局的領航者：\n"
        "1. 懂製造與骨幹：深知 SAP ECC 至 S/4HANA 升級的敏感神經，恪守 Clean Core 原則，以 Kafka CDC 串流解耦，絕不干擾核心停機窗口；\n"
        "2. 懂平台與重用：能將零碎的模型調用收斂為單一企業級模型網關，降低 20~40% Token 成本，讓 AI 成為即插即用的水庫；\n"
        "3. 懂組織與人性：在傳統製造文化中化解技術老將的防衛心理，以露骨商業算盤帶動業務同仁轉型為 AI 原生 PO。"
    )
    r_p2.font.name = "STHeiti Light"
    r_p2.font.size = Pt(9.5)
    r_p2.font.color.rgb = RGB_DARK
    img_bento_path = os.path.join(IMG_DIR, 'diagram_bento.png')
    if os.path.exists(img_bento_path):
        doc.add_picture(img_bento_path, width=Inches(7.2))
    doc.add_page_break()

    # PAGE 3: LITE-ON Strategic Context
    add_header_banner(doc, 3, "光寶科技現況脈絡解構：86家子公司與 S/4HANA 大局", "STRATEGIC CONTEXT", "86 間子公司、112 座製造工廠、20+ 跨國據點之複雜度剖析")
    add_callout(doc,
        "光寶產品線橫跨雲端伺服器電源、網路通訊、消費電子、車用電子到智慧城市。資訊系統不是輔助工具，而是支撐千億營收的骨幹。\n"
        "2026 年 3 月啟動的 S/4HANA 專案包含 16 項新功能導入與 27 項管理流程優化，時程壓縮至 10 個月，停機 72 小時上線。此役只許成功，不容差錯。",
        title="實地調研：光寶規模與關鍵時程"
    )
    tbl_p3 = doc.add_table(rows=4, cols=3)
    tbl_p3.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p3.columns[0].width = Inches(1.8)
    tbl_p3.columns[1].width = Inches(2.7)
    tbl_p3.columns[2].width = Inches(2.7)
    headers_p3 = ["維度 / 節點", "光寶科技真實痛點與現況", "互補架構之解法與落地路徑"]
    for i, h in enumerate(headers_p3):
        c = tbl_p3.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=70, bottom=70, left=90, right=90)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY
    rows_p3 = [
        ("S/4HANA 升級大戰\n(2027/01/04 切換)", "核心系統骨幹牽一髮動全身，全球 86 家公司同時切換，停機時間僅 72 小時，任何客製化 AI 均嚴禁直接修改 ERP 核心。", "恪守 SAP Clean Core 原則。將 AI 邏輯完全移至外掛微服務層，透過 CDC 異動捕捉技術入湖，對 ERP 資料庫零負載。"),
        ("跨事業部數據對齊\n與沖銷邏輯", "過去合併報表每逢月結，BW 抽取數據需人工反覆核對，耗費會計團隊大量精力於沖銷對帳。", "建立跨事業部主數據 (MDM) 血緣追蹤，為 AI 提供即時乾淨且具備審計軌跡之高質量數據。"),
        ("下一個里程碑\n「讓 ERP 更 AI」", "李逢堉資訊長明言：線的另一邊是製造端主動判斷。MES 與 ERP 需緊密結合，在替代料、齊套料與工單排程全自動化。", "導入製造預測大腦與雙環 Data Bus，建立替代料自動驗證演算法，使產線具備自動排產與動態避險之自我感知能力。")
    ]
    for r_idx, r_data in enumerate(rows_p3, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p3.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=70, bottom=70, left=90, right=90)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8)
            r.font.color.rgb = RGB_DARK
    doc.add_page_break()

    # PAGE 4: Strategic Inflection: Making ERP AI-Native
    add_header_banner(doc, 4, "戰略破局點：「讓 ERP 更 AI」的製造端結構性剛需", "STRATEGIC INFLECTION", "跳脫報表呈現，在生產製造現場實現自我感知、主動預測與決策閉環")
    add_callout(doc,
        "傳統 ERP 的本質是「記錄型系統」(System of Record)，負責記帳、管料、發工單，但它不會告訴生管「若這批電阻缺料，下一秒產線該換哪一張工單才不會造成兩小時空轉」。\n"
        "AI 平台的定位是「智慧型系統」(System of Intelligence)，與 ERP 形成雙螺旋互補，在製造現場形成自我感知的神經網絡。",
        title="從 System of Record 躍升為 System of Intelligence"
    )
    p_p4 = doc.add_paragraph()
    r_p4 = p_p4.add_run(
        "光寶科技在全球生產基地的布局廣泛，涵蓋台灣、中國華東華南、泰國、越南等地。當國際地緣政治與供應鏈波動加劇時，傳統以月或週為單位的 MRP (物料需求規劃) 運算已無法應對現場每小時的突發變故。\n"
        "因此，將 AI 深度植入製造排程，具備三項不可替代的戰略價值：\n"
        "1. 敏捷避險：供應鏈物料交期異動時，秒級內全域排查替代料與受衝擊工單；\n"
        "2. 資本釋放：降低高昂的緩衝安全庫存 (Safety Stock)，釋放數億元流動資金；\n"
        "3. 人均產值倍增：生管與採購人員告別 Excel 手動排產與人工核對，轉型為例外事件處理者。"
    )
    r_p4.font.name = "STHeiti Light"
    r_p4.font.size = Pt(9.5)
    r_p4.font.color.rgb = RGB_DARK
    doc.add_page_break()

    # PAGE 5: Core Positioning: From Ad-hoc Apps to Reusable Platform
    add_header_banner(doc, 5, "核心定位：從零散應用走向企業級可重複平台", "CORE POSITIONING", "把 AI 從單一應用推進到產品，再到可重複使用的平台，帶來經濟效益")
    p_p5 = doc.add_paragraph()
    r_p5 = p_p5.add_run(
        "光寶科技對此職位的期望明確而務實：負責光寶整體 AI 策略與執行。把 AI 從單一應用推進到產品，再到可重複使用的平台，並為公司帶來看得見的經濟效益。\n"
        "下圖展示企業級 AI 平台的完整中樞拓撲架構："
    )
    r_p5.font.name = "STHeiti Light"
    r_p5.font.size = Pt(9.5)
    r_p5.font.color.rgb = RGB_DARK
    img_plat_path = os.path.join(IMG_DIR, 'diagram_platform.png')
    if os.path.exists(img_plat_path):
        doc.add_picture(img_plat_path, width=Inches(7.2))
    add_callout(doc,
        "平台化三大核心支柱：\n"
        "• 多模型網關：單一端點統一調度 250+ 開源與商用模型，具備 Smart Routing 與 0% 加價；\n"
        "• 任務編排中樞：Agentic RAG（95% 準確率）、多模態憑證 OCR 與標準 MCP 協議；\n"
        "• 製造預測大腦：工業級 AutoML 參數推薦、生化指標虛擬量測與數位孿生員工。",
        title="平台化核心組件能力清單"
    )
    doc.add_page_break()

    # PAGE 6: Platform Economics: Token FinOps & BU ROI Attribution
    add_header_banner(doc, 6, "平台經濟學：Token 調度優化與各事業部 ROI 歸屬機制", "PLATFORM FINOPS", "建立看得見的財務度量，杜絕算力黑洞，讓每一筆 AI 投資都有財務回報")
    add_callout(doc,
        "「看不見成本的技術，不是好架構。」\n"
        "在大規模推廣 AI 時，若未建立精密的 FinOps 成本治理，光寶 86 家公司頻繁調用公有雲旗艦模型，每月 API 帳單將成為巨大黑洞。平台化最重要的經濟使命，就是實現 Token 成本透明化與智慧分流。",
        title="成本控制哲學：Smart Routing 降本 20~40%"
    )
    tbl_p6 = doc.add_table(rows=4, cols=3)
    tbl_p6.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p6.columns[0].width = Inches(2.0)
    tbl_p6.columns[1].width = Inches(2.6)
    tbl_p6.columns[2].width = Inches(2.6)
    headers_p6 = ["FinOps 治理層次", "傳統無受控調用模式", "平台化集中智能分流機制"]
    for i, h in enumerate(headers_p6):
        c = tbl_p6.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=70, bottom=70, left=90, right=90)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY
    p6_rows = [
        ("模型分流機制\n(Smart Routing)", "所有 Query 一律送往昂貴的頂級商業模型，問安、翻譯與簡單抽取皆消耗高額 Token。", "依 Query 複雜度分類：簡單文字由本地開源小模型 (0 成本) 處理，複雜推理才呼叫商業大模型，降低 20~40% 成本。"),
        ("成本核算與分攤\n(Cost Allocation)", "全集團共用一張信用卡或總部統包買單，各事業部無成本意識，浪費嚴重且無從追究。", "網關內建多租戶計費度量，精確記錄各事業部 (BU)、廠區與專案調用量，產出月度成本分攤報表。"),
        ("高可用容災\n(Failover SLA)", "單一模型供應商當機或限流 (Rate Limit) 時，全公司業務系統瞬間停擺。", "網關內建跨模型供應商自動熔斷與毫秒級 Failover 切換，保證 99.99% 高可用連續性。")
    ]
    for r_idx, r_data in enumerate(p6_rows, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p6.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=70, bottom=70, left=90, right=90)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8)
            r.font.color.rgb = RGB_DARK
    doc.add_page_break()

    # PAGE 7: Work Scope 1: Prioritization & TOGAF BDAT Matrix
    add_header_banner(doc, 7, "工作內容 1：定義優先領域與四階 BDAT 平台藍圖", "WORK SCOPE 1", "與高階主管定義優先導入 AI 領域，規劃 AI 平台藍圖 ｜ TOGAF 10 ADM 規範")
    add_callout(doc,
        "導入 AI 不能由技術人員閉門造車，必須由上而下與高階主管對齊戰略優先級。採用國際標準 TOGAF 企業架構四階矩陣 (BDAT)，將光寶的商業戰略分解為可執行的工程組件。",
        title="架構頂層設計：業務驅動技術"
    )
    img_bdat_path = os.path.join(IMG_DIR, 'diagram_bdat_matrix.png')
    if os.path.exists(img_bdat_path):
        doc.add_picture(img_bdat_path, width=Inches(7.2))
    p_p7 = doc.add_paragraph()
    r_p7 = p_p7.add_run(
        "BDAT 四階矩陣核心職能分工：\n"
        "• 業務架構 (B)：以全球 86 家子公司營運目標為起點，建立 112 座工廠生管排程與採購比價流程，以商業 ROI 驅動研發；\n"
        "• 數據架構 (D)：建立雙環 Data Bus，串流 SAP S/4HANA CDC 與機台 MQTT 數據，落實數據完整性；\n"
        "• 應用架構 (A)：將零散程式碼收斂為標準微服務資料產品，杜絕各單位重複造輪子；\n"
        "• 技術架構 (T)：規劃混合多雲算力調度與工廠邊緣節點，落實 Zero Outage 零非計畫停機。"
    )
    r_p7.font.name = "STHeiti Light"
    r_p7.font.size = Pt(9)
    r_p7.font.color.rgb = RGB_DARK
    doc.add_page_break()

    # PAGE 8: Stakeholder Maturity & Plant Director Interview Framework
    add_header_banner(doc, 8, "工作內容 1 (續)：跨 C-Level 與海外總廠長訪談體系", "STAKEHOLDER INTERVIEWS", "深入挖掘「問題背後的問題」，傾聽第一線真實痛點，凝聚變革共識")
    add_callout(doc,
        "見招拆招只能治標，深挖問題才能治本。到任前 30 天，本人將啟動結構化深度訪談，對象涵蓋事業部高階主管與海外工廠現場負責人。",
        title="跨職能成熟度訪談方法論"
    )
    tbl_p8 = doc.add_table(rows=5, cols=3)
    tbl_p8.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p8.columns[0].width = Inches(1.8)
    tbl_p8.columns[1].width = Inches(2.7)
    tbl_p8.columns[2].width = Inches(2.7)
    headers_p8 = ["訪談對象", "深度挖掘之核心問題清單", "戰略產出與架構輸入"]
    for i, h in enumerate(headers_p8):
        c = tbl_p8.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=70, bottom=70, left=90, right=90)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY
    p8_rows = [
        ("營運長 / 生產副總\n(COO / VP Ops)", "1. 目前 112 座工廠最頻繁導致停線的前三大缺料品類為何？\n2. 跨廠產能調度與急單插入時，最大的溝通斷點在哪？", "確立製造端 AI 優先攻堅題目，定義工單排程優化指標。"),
        ("財務長\n(CFO)", "1. 跨國沖銷與對帳作業中，最耗費人力的核對環節為何？\n2. 各事業部對 AI 投資預算與 Token 效益分攤的期待為何？", "建立 FinOps 成本分攤模型與財務傳票 OCR 落地規格。"),
        ("海外各廠總廠長\n(Plant Directors)", "1. 現場網路連線品質是否足以支撐雲端模型？\n2. 資深調機師傅經驗流失的痛點多嚴重？在地語言障礙為何？", "規劃工廠邊緣推理節點規格與本地多語言知識庫架構。"),
        ("採購與供應鏈處長\n(Sourcing VP)", "1. 供應商停產通知 (EOL) 到現場排查替代料平均耗時多久？\n2. 原料報價異常是否有即時比價機制？", "打造替代料智能推薦系統與原物料價格波動預警模型。")
    ]
    for r_idx, r_data in enumerate(p8_rows, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p8.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=70, bottom=70, left=90, right=90)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8)
            r.font.color.rgb = RGB_DARK
    doc.add_page_break()

    # PAGE 9: Work Scope 2: Reusable Data Products & Microservices
    add_header_banner(doc, 9, "工作內容 2：零散應用產品化與微服務資料產品庫", "WORK SCOPE 2", "把零散應用做成可重複使用的資料產品與平台 ｜ 微服務標準庫規劃")
    add_callout(doc,
        "把 AI 從單一專案推進為「資料產品」(Data Products)，核心在於標準化封裝與 API 契約。各事業部只需呼叫標準端點，無須重複訓練模型與建立基礎設施。",
        title="資料產品化哲學：開箱即用、隨需擴展"
    )
    tbl_p9 = doc.add_table(rows=4, cols=3)
    tbl_p9.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p9.columns[0].width = Inches(2.0)
    tbl_p9.columns[1].width = Inches(2.6)
    tbl_p9.columns[2].width = Inches(2.6)
    headers_p9 = ["微服務資料產品", "核心功能與演算法封裝", "全集團跨 BU 重複使用場景"]
    for i, h in enumerate(headers_p9):
        c = tbl_p9.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=70, bottom=70, left=90, right=90)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY
    p9_rows = [
        ("通用多模態憑證 OCR\n(Document Parser Service)", "自研排版結構還原演算法，支援各國發票、海關單據、裝箱單自動抽取關鍵欄位。", "財務部傳票核銷、工廠進料收貨驗收、供應商對帳單自動化處理。"),
        ("企業級 Agentic RAG\n(Knowledge Retrieval Service)", "向量檢索 + 重排序 (Rerank) + 來源嚴格標註，杜絕模型幻覺，準確率達 95%。", "全球技術客服規格問答、ISO 規章政策檢索、工廠除錯手冊導航。"),
        ("工業參數推薦引擎\n(AutoML Optimization Service)", "AutoML 特徵工程 + 強化學習參數尋優，封裝為輕量容器化微服務。", "電源轉換效率調校、SMT 回焊爐溫度曲線推薦、注塑機參數調優。")
    ]
    for r_idx, r_data in enumerate(p9_rows, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p9.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=70, bottom=70, left=90, right=90)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8)
            r.font.color.rgb = RGB_DARK
    doc.add_page_break()

    # PAGE 10: Enterprise Model Gateway & APISIX Governance
    add_header_banner(doc, 10, "工作內容 2 (續)：多模型網關與 API 影子資安防禦", "MODEL GATEWAY", "建立單一安全入口，清點影子 API，防止機密數據裸奔公網")
    add_callout(doc,
        "在開放同仁使用 AI 的同時，資安門神必須先立好。透過企業級 API 網關與多模型中樞，所有對外模型調用均需經過認證、脫敏與審計。",
        title="網關安全準則：進得來、出得去、管得住"
    )
    p_p10 = doc.add_paragraph()
    r_p10 = p_p10.add_run(
        "模型網關技術規範與防護三道鎖：\n"
        "1. 敏感數據自動脫敏 (DLP Masking)：\n"
        "   Prompt 在離開光寶網絡前，網關自動過濾身分證號、薪酬數字、客戶機密代號與機密料號，防止數據裸奔公有雲；\n"
        "2. 影子 API 自動清點：\n"
        "   監聽內部網絡流量，抓出未經核可、工程師私自串接的外部 AI 端點，防止越權與 BOLA 漏洞；\n"
        "3. 統一認證授權 (OAuth 2.0 / Keycloak)：\n"
        "   對接光寶既有 Azure AD / SSO 帳號體系，實現細粒度角色的權限隔離。"
    )
    r_p10.font.name = "STHeiti Light"
    r_p10.font.size = Pt(9.5)
    r_p10.font.color.rgb = RGB_DARK
    doc.add_page_break()

    # PAGE 11: Work Scope 3: Complementary AI Stack to SAP, PLM, MES
    add_header_banner(doc, 11, "工作內容 3：建立和 SAP、PLM、MES 互補的 AI Stack", "WORK SCOPE 3", "建立和 SAP、PLM、MES 互補的 AI stack ｜ 恪守 SAP Clean Core 原則")
    add_callout(doc,
        "核心架構原則：先串資料，再談 AI。減少客製化技術債，絕不干擾 S/4HANA 2027 年 1 月 4 日全球上線！",
        title="互補式架構哲學：外掛解耦、數據貫通"
    )
    tbl_p11 = doc.add_table(rows=4, cols=3)
    tbl_p11.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p11.columns[0].width = Inches(1.8)
    tbl_p11.columns[1].width = Inches(2.7)
    tbl_p11.columns[2].width = Inches(2.7)
    headers_p11 = ["核心骨幹系統", "系統職責與傳統作業瓶頸", "AI Stack 互補賦能模式"]
    for i, h in enumerate(headers_p11):
        c = tbl_p11.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=70, bottom=70, left=90, right=90)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY
    p11_rows = [
        ("PLM 產品生命週期\n(研發設計 / ECN)", "工程變更 (ECN) 頻繁，規格手冊多為非結構化 PDF，人工輸入 ERP 料號耗時且容易用錯版本。", "PLM 規格智能抽取 Agent 自動解析工程圖與規格書，結構化寫入物料主數據，同步更新工藝路線。"),
        ("SAP S/4HANA\n(訂單 / 物料 / 財務)", "86 家公司核心交易系統，升級期不容許客製化修改，高併發查詢容易拖垮核心資料庫。", "恪守 SAP Clean Core。透過標準 OData API 與 Debezium CDC 異動監控，在外部建立高效能運算快取。"),
        ("MES 製造執行系統\n(現場工單 / 設備)", "112 座工廠設備協議各異，機台稼動率與良率數據零散，無法即時回饋至排產決策。", "在工廠端部署 EMQX MQTT 物聯網邊緣總線，即時聚合機台狀態與良率，驅動 AI 動態排產並雙向回填。")
    ]
    for r_idx, r_data in enumerate(p11_rows, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p11.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=70, bottom=70, left=90, right=90)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8)
            r.font.color.rgb = RGB_DARK
    doc.add_page_break()

    # PAGE 12: Dual-Ring Data Bus: Kafka + SAP CDC + OT MQTT
    add_header_banner(doc, 12, "工作內容 3 (續)：雙環即時 Data Bus 拓撲與零負載 CDC", "DATA BUS TOPOLOGY", "IT 骨幹串流 ＋ SAP 異動捕捉 ＋ OT 物聯網邊緣，架構永不中斷的數據動脈")
    img_erp_path = os.path.join(IMG_DIR, 'diagram_erp_mes.png')
    if os.path.exists(img_erp_path):
        doc.add_picture(img_erp_path, width=Inches(7.2))
    add_callout(doc,
        "雙環 Data Bus 核心工程指標：\n"
        "• 零生產資料庫查詢壓力：Debezium 監聽 S/4HANA 底層 Transaction Log，以非同步方式毫秒級寫入 Kafka；\n"
        "• 高吞吐跨國串流：Apache Kafka 承載 86 家公司每秒數萬筆物料異動與工單事件；\n"
        "• OT 邊緣高可用：EMQX MQTT Broker 具備工廠離線續存能力，網絡恢復後自動追補數據。",
        title="數據總線性能與可靠性規格"
    )
    doc.add_page_break()

    # PAGE 13: Shop-Floor AI 1: Part Substitution Engine
    add_header_banner(doc, 13, "製造端痛點攻堅 (一)：替代料智能選用與相容性比對", "SHOP-FLOOR AI", "直擊光寶李逢堉資訊長痛點：在物料短缺時秒級推演替代料件，防範停線")
    img_sub_path = os.path.join(IMG_DIR, 'diagram_substitution_flow.png')
    if os.path.exists(img_sub_path):
        doc.add_picture(img_sub_path, width=Inches(7.2))
    p_p13 = doc.add_paragraph()
    r_p13 = p_p13.add_run(
        "替代料推演演算法四重防呆機制：\n"
        "1. 電性規格硬約束：耐壓、阻抗、頻率、封裝尺寸必須 100% 吻合 PLM 零件規範；\n"
        "2. 安規認證核對：自動檢查替代料件是否已獲 UL、CE、車用 AEC-Q 認證，防止合規風險；\n"
        "3. 全球即時庫存排查：自動穿透 86 家子公司庫存，優先推薦已有在手庫存之合格替代料；\n"
        "4. 專家在環審核 (Human-in-the-Loop)：AI 自動生成比對報告，由資深工程師一鍵覆核後同步 S/4HANA。"
    )
    r_p13.font.name = "STHeiti Light"
    r_p13.font.size = Pt(9.5)
    r_p13.font.color.rgb = RGB_DARK
    doc.add_page_break()

    # PAGE 14: Shop-Floor AI 2: Kit Readiness Dynamic Planning
    add_header_banner(doc, 14, "製造端痛點攻堅 (二)：齊套料動態規劃與在製品即時流", "KIT READINESS", "解決工廠開工後才發現欠料之宿疾，消除產線半套呆滯與換模損失")
    add_callout(doc,
        "傳統 ERP MRP 運算的盲點在於「只看靜態料帳，不看現場動態」。\n"
        "當工單開立時，倉庫可能帳上有料，但料件實際上正被另一條產線領用、或正處於品管進料檢驗 (IQC) 待檢狀態。齊套料動態規劃 AI 讓生管看見真實的物料流動。",
        title="動態齊套思維：從靜態庫存到即時動態流"
    )
    tbl_p14 = doc.add_table(rows=4, cols=3)
    tbl_p14.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p14.columns[0].width = Inches(2.0)
    tbl_p14.columns[1].width = Inches(2.6)
    tbl_p14.columns[2].width = Inches(2.6)
    headers_p14 = ["物料所處狀態", "傳統排程之盲點與風險", "齊套料 AI 演算法即時校驗"]
    for i, h in enumerate(headers_p14):
        c = tbl_p14.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=70, bottom=70, left=90, right=90)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY
    p14_rows = [
        ("進料檢驗中物料\n(IQC Pending)", "ERP 帳面已收貨，生管誤以為可用，開工後發現品檢未過，產線瞬間卡死。", "AI 即時讀取品檢系統狀態，結合歷史批次合格率，動態預測放行時間，未合格前不計入齊套料。"),
        ("跨廠在途運輸\n(In-Transit Stocks)", "跨廠調撥物料在途中，未考慮海關清關延遲與物流突發事件。", "對接物流 GPS 與報關系統，動態估算 ETA 到廠時間，設定置信區間，防止虛擬派工。"),
        ("產線在製品\n(Work-in-Progress)", "前道工序產出不良導致後道組裝料件不足，傳統系統無法即時連動。", "MES 現場機台計數即時回傳，動態重新計算齊套率，未達 100% 臨界值自動發布排程暫緩警報。")
    ]
    for r_idx, r_data in enumerate(p14_rows, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p14.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=70, bottom=70, left=90, right=90)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8)
            r.font.color.rgb = RGB_DARK
    doc.add_page_break()

    # PAGE 15: Shop-Floor AI 3: Dynamic Work Order Dispatching
    add_header_banner(doc, 15, "製造端痛點攻堅 (三)：工單智慧動態排程與 OEE 提升", "DYNAMIC DISPATCHING", "平衡換模損失、設備嫁動率與交期優先級，打造全自動排產大腦")
    add_callout(doc,
        "工單排程是多目標最佳化的極限挑戰。生管人員每天面對數百張工單，大腦無法同時計算 112 座工廠每台 SMT 貼片機的換模時間、進料節奏與交期懲罰。\n"
        "AI 動態排產引擎透過運籌學與強化學習，在數十秒內輸出全局最佳解。",
        title="排產演算法核心：全域最佳化"
    )
    p_p15 = doc.add_paragraph()
    r_p15 = p_p15.add_run(
        "動態排產演算法四大效益產出：\n"
        "1. 減少無效換模：相同封裝與原料工單自動合批，SMT 產線換線換模時間減少 25%；\n"
        "2. 提升設備稼動率 (OEE)：全廠機台平均嫁動率提升 5%~8%，相當於憑空釋放數條產線產能；\n"
        "3. 急單插入平準化：VIP 客戶急單插入時，AI 演算法自動計算對其他訂單衝擊最小之挪移方案；\n"
        "4. 現場 HMI 自動推播：排產變更無須印紙本派工單，即時推播至機台控制器螢幕。"
    )
    r_p15.font.name = "STHeiti Light"
    r_p15.font.size = Pt(9.5)
    r_p15.font.color.rgb = RGB_DARK
    doc.add_page_break()

    # PAGE 16: Work Scope 4: AI Talent Pipeline & War-Time Leadership
    add_header_banner(doc, 16, "工作內容 4：組建 AI 組織梯隊與戰時管理領導力", "WORK SCOPE 4", "組建 AI 組織與人才梯隊，帶領技術主管與工程師 ｜ 戰時領導管理心法")
    add_callout(doc,
        "在非成熟治理土壤中，當高層面臨轉型焦慮、中間層退化為傳話筒、基層工程師陷入集體迷茫時，任何高大上的學院派敏捷儀式都是徒勞。\n"
        "身為領軍者，唯一的生還之道是具備戰時領導力：以硬核商業算盤爭取空間，用極簡防護工具保護基層，專注搭建骨架，成就團隊，功成不必在我。",
        title="戰時領導心法：穿上防彈衣，扛起責任"
    )
    p_p16 = doc.add_paragraph()
    r_p16 = p_p16.add_run(
        "光寶 AI 研發團隊梯隊編制藍圖 (9~14 人核心部隊)：\n"
        "• 系統架構師 (2 名)：主責 S/4HANA Clean Core 對接、雙環 Data Bus 穩定性與多模型網關設計；\n"
        "• 資料與 MLOps 工程師 (4 名)：主責 Kafka 串流、Debezium CDC 維運、特徵庫構建與模型自動部署；\n"
        "• 後端與 API 工程師 (4 名)：主責微服務資料產品封裝、影子 API 防禦與高併發接口；\n"
        "• 業務領域產品負責人 (PO, 4 名)：常駐工廠現場與業務單位，專職翻譯痛點並監督商業效益實現。"
    )
    r_p16.font.name = "STHeiti Light"
    r_p16.font.size = Pt(9.5)
    r_p16.font.color.rgb = RGB_DARK
    doc.add_page_break()

    # PAGE 17: Overcoming Status/Interest/Relationship Defenses via ORID
    add_header_banner(doc, 17, "工作內容 4 (續)：化解開國老臣山頭防衛與 ORID 焦點法", "ORGANIZATION DEFENSE", "破除地位防衛、利益防衛與關係防衛，建立公平互信的工程文化")
    tbl_p17 = doc.add_table(rows=4, cols=3)
    tbl_p17.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p17.columns[0].width = Inches(1.8)
    tbl_p17.columns[1].width = Inches(2.7)
    tbl_p17.columns[2].width = Inches(2.7)
    headers_p17 = ["老將深層防禦心理", "具體防衛行為與負面表徵", "實戰引導手腕與化解機制 (ORID)"]
    for i, h in enumerate(headers_p17):
        c = tbl_p17.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=70, bottom=70, left=90, right=90)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY
    p17_rows = [
        ("地位防衛\n(Status Defense)", "擔心新架構否定其十幾年來的維護貢獻，質疑外部引進之 AI 平台華而不實。", "公開肯定歷史系統對千億營收的支撐，邀請資深主管擔任架構委員會委員，賦予新架構把關重任。"),
        ("利益防衛\n(Interest Defense)", "憂慮自動化工具剝奪其團隊編制與維運預算，暗中拖延資料提供與介接工作。", "制定明確職務說明書 (JD)，協助同仁升級為內部業務架構師與領域專家，確保職涯價值提升。"),
        ("關係防衛\n(Relationship Defense)", "小團體林立、資訊壟斷，跨部門溝通壁壘森嚴，習慣向上管理與迎合。", "運用「如果一年後團隊更差是因為什麼」逆向提問，導入 ORID 焦點討論法，凝聚集體求生共識。")
    ]
    for r_idx, r_data in enumerate(p17_rows, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p17.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=70, bottom=70, left=90, right=90)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8)
            r.font.color.rgb = RGB_DARK
    add_callout(doc,
        "戰略絕緣層（Decoupling & Buffer）手腕：\n"
        "當高層有急躁或不切實際的即興需求時，身為 AI 平台負責人必須成為團隊的防彈衣與避震器。自己主動承受管理壓力，專注於骨架搭建與體系健全，讓基層工程師在安全的沙盒中專心攻堅，功成不必在我。",
        title="高階領導心法：保護團隊的戰時絕緣層"
    )
    doc.add_page_break()

    # PAGE 18: 9 Engineering Ladders & 9-Box Matrix
    add_header_banner(doc, 18, "工作內容 4 (續)：9 大工程技術階梯與人才九宮格", "TALENT MATRIX", "打破主管單點壟斷，授權潛力新星挑大樑，打造量化考評人才庫")
    img_jrny_path = os.path.join(IMG_DIR, 'diagram_journey.png')
    if os.path.exists(img_jrny_path):
        doc.add_picture(img_jrny_path, width=Inches(7.2))
    p_p18 = doc.add_paragraph()
    r_p18 = p_p18.add_run(
        "三大工程團隊差異化賦能策略：\n"
        "• 企劃營運組：導入「三好一支援」工作坊，建立 5 大構面指標字典，培育成懂商業也懂技術邊界的內部 PO；\n"
        "• 前端與應用組：抽卡牌破冰＋優勢卡對齊，透過人才九宮格定位潛力星，打破組長單點壟斷，直接授權負責核心模組；\n"
        "• 後端與資料組：規劃 9 大技術階梯 (Tracks A~I)，落實「承認能力、同意問題、建立公平規則」，杜絕盲目內卷。"
    )
    r_p18.font.name = "STHeiti Light"
    r_p18.font.size = Pt(9.5)
    r_p18.font.color.rgb = RGB_DARK
    doc.add_page_break()

    # PAGE 19: Work Scope 5: Business-Led Platform & PO Academy
    add_header_banner(doc, 19, "工作內容 5：業務主導之平台機制與內部 PO 培訓營", "WORK SCOPE 5", "推動業務主導的平台團隊與企業內部 PO 培養，帶動 AI 原生的工作方式")
    img_po_path = os.path.join(IMG_DIR, 'diagram_po_academy.png')
    if os.path.exists(img_po_path):
        doc.add_picture(img_po_path, width=Inches(7.2))
    add_callout(doc,
        "文化變革的核心目標：把「資訊部要我用 AI」轉變為「我要用 AI 解決我的痛點、達成我的 KPI」。\n"
        "唯有讓業務與製造單位的人員成為系統的真正 Product Owner，AI 平台才能生生不息。",
        title="業務主導的核心宗旨"
    )
    doc.add_page_break()

    # PAGE 20: 5-Dimension Metric Dictionary & ROI Sandbox
    add_header_banner(doc, 20, "工作內容 5 (續)：5 大構面指標字典與商業算盤對賭", "METRIC DICTIONARY", "建立業務與技術的共同度量，以露骨商業算盤打平成本")
    tbl_p20 = doc.add_table(rows=6, cols=3)
    tbl_p20.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p20.columns[0].width = Inches(1.8)
    tbl_p20.columns[1].width = Inches(2.7)
    tbl_p20.columns[2].width = Inches(2.7)
    headers_p20 = ["指標構面", "指標定義與衡量維度", "光寶內部 PO 對賭與驗收目標"]
    for i, h in enumerate(headers_p20):
        c = tbl_p20.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=70, bottom=70, left=90, right=90)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY
    p20_rows = [
        ("企劃構面 (Planning)", "場景邊界、使用者旅程、需求重複使用潛力。", "確保功能並非單一工廠特化，至少具備 3 個廠區複製價值。"),
        ("營運構面 (Operations)", "每批次生產前置期、機台換模時間、工單準時交付率。", "SMT 換模工時縮短 25%，訂單製造前置期縮短 15%。"),
        ("財務構面 (Financials)", "Token 消耗對應之工時節省、不良品降損金額、EBITDA 貢獻。", "專案上線半年內，量化經濟效益必須打平團隊人事與算力成本。"),
        ("介接構面 (Integration)", "API 響應時間 (<200ms)、錯誤率 (<0.01%)、數據血緣覆蓋率。", "嚴格遵守 S/4HANA 標準 API 規範，新增介面技術債為零。"),
        ("專案構面 (PM)", "雙週 MVP 交付達成率、功能試用同仁活躍度 (DAU/MAU)。", "2 週驗收原型、4 週試點投產、8 週核算實質損益。")
    ]
    for r_idx, r_data in enumerate(p20_rows, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p20.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=70, bottom=70, left=90, right=90)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8)
            r.font.color.rgb = RGB_DARK
    doc.add_page_break()

    # PAGE 21: Departmental AI: Leadership First, IT Testing, Expansion
    add_header_banner(doc, 21, "工作內容 5 (續)：Departmental AI 跨部門四階普及法", "DEPARTMENTAL AI", "主管先學、資訊部先試、有成效再擴散 ｜ 跨部門普及落地清冊")
    add_callout(doc,
        "光寶推動 AI 普及的三大鐵律：\n"
        "1. 嚴禁為了做 AI 而做 AI：無明確商業指標者一律不予立項；\n"
        "2. 嚴守機密圖面安全邊界：設計圖面與客戶規格不出廠；\n"
        "3. 堅持小步快跑：拒絕長達一年的巨石專案，以 2 週迭代快速見效。",
        title="Departmental AI 推動原則"
    )
    tbl_p21 = doc.add_table(rows=5, cols=3)
    tbl_p21.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p21.columns[0].width = Inches(1.8)
    tbl_p21.columns[1].width = Inches(2.7)
    tbl_p21.columns[2].width = Inches(2.7)
    headers_p21 = ["目標事業 / 職能部門", "專屬 AI 應用題目與試點場景", "量化成效驗收指標"]
    for i, h in enumerate(headers_p21):
        c = tbl_p21.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=70, bottom=70, left=90, right=90)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY
    p21_rows = [
        ("生產製造單位\n(Manufacturing & OT)", "製程參數知識庫問答、資深師傅調機經驗數位化、SMT 換線輔助。", "調機時間縮短 25%，資深師傅關鍵排障經驗 100% 結構化保存。"),
        ("品保品檢單位\n(QA & QC Units)", "AOI 檢驗影像輔助判讀、跨國客訴根本原因 (RCA) 智慧歸因分析。", "品檢誤判率降低 30%，跨國客訴調查週期從 3 天縮短為 2 小時。"),
        ("全球業務與採購\n(Sales & Sourcing)", "客戶規格書 (Spec) 智能比對、原料歷史價格波動預警、替代料庫存推薦。", "客戶詢價比對效率提升 50%，原物料非預期呆滯率降低 20%。"),
        ("管理與法規團隊\n(Admin & Legal)", "跨國採購合約條款智慧審查、內部 IT Helpdesk 工單智慧分類排障。", "合約初審工時節省 60%，Helpdesk 一線自動解決率達 45%。")
    ]
    for r_idx, r_data in enumerate(p21_rows, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p21.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=70, bottom=70, left=90, right=90)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8)
            r.font.color.rgb = RGB_DARK
    doc.add_page_break()

    # PAGE 22: Work Scope 6: C-Level Reporting & Balanced Scorecard
    add_header_banner(doc, 22, "工作內容 6：向高階主管定期報告成效與投資回報", "WORK SCOPE 6", "定期向高階主管與事業單位主管報告成效 ｜ CEO Balanced Scorecard")
    add_callout(doc,
        "報告原則：高階主管時間極其寶貴，絕不講技術黑話。\n"
        "以 CEO Balanced Scorecard 與一頁式決策審核表，定期向董事會、李逢堉資訊長與事業部總經理呈報實質 EBITDA 貢獻與風險熱圖。",
        title="C-Level 呈報哲學：商業價值優先"
    )
    tbl_p22 = doc.add_table(rows=4, cols=3)
    tbl_p22.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p22.columns[0].width = Inches(1.8)
    tbl_p22.columns[1].width = Inches(2.7)
    tbl_p22.columns[2].width = Inches(2.7)
    headers_p22 = ["報告層級與週期", "核心呈報內容與關鍵視圖", "決策價值與管理輸出"]
    for i, h in enumerate(headers_p22):
        c = tbl_p22.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=70, bottom=70, left=90, right=90)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY
    p22_rows = [
        ("月度戰情報告\n(Monthly Ops Review)", "向李逢堉資訊長呈報各 BU Token 成本效益榜、API 延遲分佈、Failover 統計、產線警報解決率。", "即時優化運算資源配置，抓出異常算力消耗部門，動態調整 Smart Routing 規則。"),
        ("季度經管會審查\n(Quarterly BOD/BU)", "向董事長與事業部總經理呈報 S/4HANA 整合進度、替代料庫存去化金額、工單準時交付率提升指標。", "以財務 EBITDA 衝擊與 ROI 說話，客觀評估各事業部 AI 投資回報率，動態調整下季預算。"),
        ("年度 IT 投資總盤點\n(Annual Capital Plan)", "Run / Grow / Transform 三向預算結構分析、雲端與硬體 TCO 總成本對照、技術債清理清冊。", "確保每一分 IT 資本支出 (CAPEX) 與營運費用 (OPEX) 均精確契合光寶中長期策略願景。")
    ]
    for r_idx, r_data in enumerate(p22_rows, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p22.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=70, bottom=70, left=90, right=90)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8)
            r.font.color.rgb = RGB_DARK
    doc.add_page_break()

    # PAGE 23: Run/Grow/Transform Capital Model & Quick Wins
    add_header_banner(doc, 23, "工作內容 6 (續)：資本配置模型與四大 Quick Wins", "CAPITAL MODEL", "Run / Grow / Transform 預算平衡 ＆ 到任 1 週內見量化成果指南")
    img_rgt_path = os.path.join(IMG_DIR, 'diagram_budget_rgt.png')
    if os.path.exists(img_rgt_path):
        doc.add_picture(img_rgt_path, width=Inches(7.2))
    add_callout(doc,
        "四大立竿見影 Quick Win 指南（到任 1 週內見成果）：\n"
        "• 場景 1：財務發票與採購單 OCR 自動對齊 S/4HANA，憑證處理工時直接降低 75%；\n"
        "• 場景 2：光寶智慧規章與技術手冊 Agentic RAG 助理，首次諮詢解決率提高 40%；\n"
        "• 場景 3：採購原物料價格波動異常自動標註與智慧防弊審批；\n"
        "• 場景 4：IT Helpdesk 一線工單智慧分類與排障，解放技術同仁時間。",
        title="Quick Wins：以速勝建立跨部門信心"
    )
    doc.add_page_break()

    # PAGE 24: Cybersecurity & AI Compliance Safeguards
    add_header_banner(doc, 24, "資安底線與 AI 合規治理：ISO 42001 ＆ ISO 27001", "CYBERSECURITY", "資安是系統整合與 AI 的底線 ｜ ISO 27001 主導稽核員標準把關")
    img_sec_path = os.path.join(IMG_DIR, 'diagram_security_ot.png')
    if os.path.exists(img_sec_path):
        doc.add_picture(img_sec_path, width=Inches(7.2))
    p_p24 = doc.add_paragraph()
    r_p24 = p_p24.add_run(
        "四大不可逾越之合規防禦底線：\n"
        "1. 工廠實體分段 (Purdue Model Air-Gapping)：機台與 OT 網絡嚴格隔離，邊緣 AI 具備離線推論能力，防止勒索病毒橫向擴散；\n"
        "2. 核心專利與圖面不出廠 (DLP)：所有電源機構設計圖面與國際客戶機密規格，絕對禁止上傳外部公有雲模型；\n"
        "3. 不可竄改安全備份 (Immutable Backup)：實施 3-2-1-1-0 備份架構，配置離線與 WORM 存儲，每季強制災備演練；\n"
        "4. AI 可解釋性與防偏誤 (ISO 42001)：排程與替代料推薦演算法保留特徵審核軌跡，落實「人類在環」審批機制。"
    )
    r_p24.font.name = "STHeiti Light"
    r_p24.font.size = Pt(9.5)
    r_p24.font.color.rgb = RGB_DARK
    doc.add_page_break()

    # PAGE 25: Qualifications & Competencies Audit
    add_header_banner(doc, 25, "光寶科技面試要求自我審查核定總表", "QUALIFICATIONS AUDIT", "官方職缺所有必要條件與加分條件，逐條匹配並附客觀可查證出處")
    img_rad_path = os.path.join(IMG_DIR, 'diagram_competency_radar.png')
    if os.path.exists(img_rad_path):
        doc.add_picture(img_rad_path, width=Inches(7.2))
    tbl_p25 = doc.add_table(rows=8, cols=4)
    tbl_p25.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p25.columns[0].width = Inches(1.3)
    tbl_p25.columns[1].width = Inches(1.8)
    tbl_p25.columns[2].width = Inches(2.9)
    tbl_p25.columns[3].width = Inches(1.2)
    headers_p25 = ["條件類別", "光寶官方條件", "Howard Liao Ph.D. 具體驗證依據", "核定結果"]
    for i, h in enumerate(headers_p25):
        c = tbl_p25.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=60, bottom=60, left=80, right=80)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY
    p25_rows = [
        ("必要條件 1", "學歷、產業背景不限", "資訊管理博士 (Ph.D.) ＆ 國立中興大學 資訊科學碩士。兼備資訊科學與管理學養。", "100% 符合"),
        ("必要條件 2", "10 年以上帶領 AI／資料團隊經驗", "27+ 年 IT & 工程歷練、20+ 年 C-Level 管理經驗，經歷軟體、跨國製造與雲端多次典範轉移。", "遠超 10 年"),
        ("必要條件 3", "主導 AI 平台或產品上線並交出可量化成果", "4 大 C-Level 商業衝擊量化成果：$10M+ 資本治理、100% Zero Outage、-30% TCO、+100% 部署速度。", "量化查核通過"),
        ("加分條件 1", "從零建立 AI／資料平台與團隊經驗", "完整記錄突破開國老臣防衛、組建 35+ 人平台梯隊之實戰經驗，從零建立模型網關與任務中樞。", "實戰驗證具備"),
        ("加分條件 2", "具備與 C Level 或 高階主管溝通能力", "長期向董事會、CEO、審計委員會、COO 呈報策略與投資規劃，擅長翻譯演算法為 EBITDA 商業價值。", "完全具備"),
        ("加分條件 3", "具備 CIO 或 IT 部門主管經驗", "曾任上市櫃科技集團 CIO/CISO/CDAIO、大型跨國高科技製造集團中央資訊技術處長。", "完整高管履歷"),
        ("加分條件 4", "國內大型企業數位轉型專案推動經驗", "曾主導跨國電子製造業數據整合、高階成衣跨國湖倉、精密醫材與生醫研發製造數位轉型。", "跨產業實績")
    ]
    for r_idx, r_data in enumerate(p25_rows, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p25.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=60, bottom=60, left=80, right=80)
            p = c.paragraphs[0]
            if c_idx == 3:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r = p.add_run(val)
                r.font.name = "STHeiti Medium"
                r.font.size = Pt(8)
                r.font.bold = True
                r.font.color.rgb = RGB_PRIMARY
            else:
                r = p.add_run(val)
                r.font.name = "STHeiti Light"
                r.font.size = Pt(8)
                r.font.color.rgb = RGB_DARK
    doc.add_page_break()

    # PAGE 26: Candidate Profile: Ph.D., Master's, Experience & Credentials
    add_header_banner(doc, 26, "候選人個人簡歷與學術底蘊 (Howard Liao Ph.D.)", "CANDIDATE PROFILE", "資訊管理博士 ｜ 國立中興大學 資訊科學碩士 ｜ 27+ 年工程與管理淬鍊")
    tbl_prof = doc.add_table(rows=1, cols=2)
    tbl_prof.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_prof.columns[0].width = Inches(2.2)
    tbl_prof.columns[1].width = Inches(5.0)
    c_img = tbl_prof.cell(0, 0)
    c_txt = tbl_prof.cell(0, 1)
    set_cell_background(c_img, HEX_HEADER_BG)
    set_cell_background(c_txt, HEX_SURFACE)
    set_cell_margins(c_img, top=90, bottom=90, left=90, right=90)
    set_cell_margins(c_txt, top=90, bottom=90, left=110, right=90)
    portrait_path = os.path.join(ASSETS_DIR, 'howard_portrait.jpg')
    if os.path.exists(portrait_path):
        p_port = c_img.paragraphs[0]
        p_port.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run_img = p_port.add_run()
        run_img.add_picture(portrait_path, width=Inches(1.8))
        p_lbl = c_img.add_paragraph()
        p_lbl.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_lbl = p_lbl.add_run("Howard Liao Ph.D.\n廖倫豪 博士")
        r_lbl.font.name = "STHeiti Medium"
        r_lbl.font.size = Pt(8.5)
        r_lbl.font.bold = True
        r_lbl.font.color.rgb = RGB_DARK
    p_txt = c_txt.paragraphs[0]
    r_pt = p_txt.add_run("【核心學歷與國際資格】\n")
    r_pt.font.name = "STHeiti Medium"
    r_pt.font.size = Pt(9.5)
    r_pt.font.bold = True
    r_pt.font.color.rgb = RGB_PRIMARY
    r_pb = p_txt.add_run(
        "• 資訊管理博士 (Ph.D. in Information Management)\n"
        "• 國立中興大學 資訊科學碩士 (National Chung Hsing Univ. · M.S. in CS)\n"
        "• 出生年份：民國 62 年次 (1973 年生)\n"
        "• 國際證照：ISO/IEC 27001 Lead Auditor 主導稽核員\n"
        "• 治理標準：ISO/IEC 42001 人工智慧治理體系 ＆ PMP 專案管理師規範\n"
        "• 聯絡方式：Email: liao.howard@gmail.com  ｜  LINE ID: howardliao\n"
        "• 線上專案門戶：https://howardliao.github.io/2301/"
    )
    r_pb.font.name = "STHeiti Light"
    r_pb.font.size = Pt(8.5)
    r_pb.font.color.rgb = RGB_DARK
    tbl_roles = doc.add_table(rows=5, cols=3)
    tbl_roles.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_roles.columns[0].width = Inches(2.0)
    tbl_roles.columns[1].width = Inches(2.2)
    tbl_roles.columns[2].width = Inches(3.0)
    headers_roles = ["服務體系 / 產業領域", "擔任高階職銜", "核心職能與歷史治理戰功"]
    for i, h in enumerate(headers_roles):
        c = tbl_roles.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=65, bottom=65, left=80, right=80)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY
    roles_data = [
        ("全球最大電子代工集團\n(跨國高科技製造)", "中央資訊 技術處長", "主責大型企業架構決策、SWOT 差距分析、商業戰略轉譯與集團數位轉型推動。奠定超大型製造網絡與全球供應鏈頂層設計能力。"),
        ("上市櫃數位科技集團\n(高科技與線上娛樂)", "資訊長 CIO / CISO / CDAIO", "掌管集團技術戰略、跨國多雲架構、高併發交易防護與 ISO 27001 資安認證；創下 100% Zero Outage 紀錄，降低 30% 基礎設施持有成本。"),
        ("高科技網絡科技集團\n(數位研發體系)", "技術副總\nVP of Technology", "主導研發團隊敏捷轉型，從零建立 Agentic AI 落地體系、建立產品 PO 制度、導入內控交易循環與 ISO 42001 人工智慧治理體系。"),
        ("跨國製造與生醫產業顧問\n(高階製造諮詢)", "企業資訊架構執行負責人\nLead Architect & C-Level Advisor", "主導跨國機能製造集團 IT 策略藍圖、精密製造 PLM/SAP/MES 整合藍圖、生醫製造企業資訊策略與 32 全架構視圖設計。")
    ]
    for r_idx, r_data in enumerate(roles_data, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_roles.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=65, bottom=65, left=80, right=80)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8)
            r.font.color.rgb = RGB_DARK
    doc.add_page_break()

    # PAGE 27: Representative Case Studies
    add_header_banner(doc, 27, "代表性專案深度復盤：跨國電子製造與精密製造實績", "CASE STUDIES", "電子製造數據整合、高可用零停機治理與全架構貫通實戰")
    cases = [
        ("實戰案例一：跨國電子製造數據整合實務（對齊光寶電源與 EMS 工廠場景）",
         "【專案背景】跨國電子零組件製造商產線面臨 SMT 拋料率偏高、跨廠備料資訊斷鏈、以及人工抄表謄打導致數據延遲 48 小時的挑戰。\n"
         "【架構對策】在工廠端部署邊緣閘道器直接採集貼片機與 AOI 檢驗機數據，建立近即時品質預警模型；在總部端打通 ERP 與生產排程，消除人工作業斷點。\n"
         "【量化成果】拋料異常通報時間從 24 小時縮短至 5 分鐘，跨廠庫存周轉率提高 18%，為光寶 112 座工廠數據互通提供了成熟範本。"),
        
        ("實戰案例二：高併發高科技系統 —— 100% Zero Outage 韌性治理與 -30% TCO",
         "【專案背景】高併發線上系統每秒承受數萬筆併發交易，任何非計畫性停機均直接導致鉅額營收損失與監管懲處。\n"
         "【架構對策】導入多雲主動容災、不可竄改防勒索備份演練與自動化流量切換，並實施 FinOps 雲端運算資源優化，去除冗餘架構雜訊。\n"
         "【量化成果】任期內創下連續多年 100% Zero Outage 營運紀錄，通過 ISO 27001 實質認證，並使集團雲端基礎設施 TCO 總成本降低 30%。"),
         
        ("實戰案例三：高階精密研發製造 —— TOGAF 32 全架構與 PLM-SAP-MES 數據流",
         "【專案背景】高階精密研發與製造領域對數據完整性與法規追溯有著極嚴苛的要求。\n"
         "【架構對策】以 TOGAF ADM 框架規劃 32 全架構視圖，設計 Kafka + Debezium CDC 雙環數據總線，使研發設計變更自動同步現場工單，杜絕用錯料號風險。\n"
         "【量化成果】研發至量產交付週期縮短 35%，全廠達成 100% 數位化批次生產記錄，稽核追溯工時減少 80%。")
    ]
    for title, desc in cases:
        add_callout(doc, desc, title=title)
    doc.add_page_break()

    # PAGE 28: 180-Day Onboarding Roadmap
    add_header_banner(doc, 28, "到任光寶 180 天平準化落地路線圖：對齊 2027/01/04 切換", "ONBOARDING ROADMAP", "倒排工期、步步為營，在不干擾 ERP 核心升級的前提下穩健推進 AI Stack")
    img_rd_path = os.path.join(IMG_DIR, 'diagram_roadmap.png')
    if os.path.exists(img_rd_path):
        doc.add_picture(img_rd_path, width=Inches(7.2))
    tbl_p28 = doc.add_table(rows=5, cols=3)
    tbl_p28.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p28.columns[0].width = Inches(1.5)
    tbl_p28.columns[1].width = Inches(2.8)
    tbl_p28.columns[2].width = Inches(2.9)
    headers_p28 = ["時間里程碑", "階段目標與主要推進工作", "關鍵交付物 (Deliverables)"]
    for i, h in enumerate(headers_p28):
        c = tbl_p28.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=65, bottom=65, left=90, right=90)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY
    p28_rows = [
        ("第 1 ~ 30 天\n(Listen & Audit)", "• 拜訪資訊長李逢堉、重點事業群總經理與海外示範廠長；\n• 與 15 位核心 IT 與資料工程師 1-on-1；\n• 盤查 S/4HANA 升級介接端點與 112 座工廠 MES/PLM 孤島現況。", "交付 1：《光寶科技 AI 現況盤點與痛點診斷報告》\n交付 2：《資深同仁優勢地圖與 9 大路線初評表》"),
        ("第 31 ~ 60 天\n(Blueprint & PO)", "• 發布光寶次世代 AI 平台拓撲藍圖 (TOGAF BDAT)；\n• 選定首波立竿見影場景（替代料推薦、齊套料預警）；\n• 成立第一期「平台試驗沙盒組」，招募首批業務 PO 同仁。", "交付 3：《光寶 AI 平台架構藍圖與技術規範》\n交付 4：《首波 PoC 規格書與業務 ROI 測算表》"),
        ("第 61 ~ 90 天\n(Pilot & Bus)", "• 部署雙環 Data Bus (Kafka + Debezium CDC + EMQX MQTT)；\n• 於海外示範廠完成 MES 與 AI 模型即時推理串接；\n• 首波 PoC 上線，驗證替代料推薦準確度與生管工時節省。", "交付 5：《示範廠 AI 推理上線實測報告》\n交付 6：《首波 1 週可量化成效報告（財務憑證 OCR 工時 -75%）》"),
        ("第 91 ~ 180 天\n(Scale & Cutover)", "• 對齊 2027/01/04 全球 S/4HANA 上線，正式掛載 AI 網關中樞；\n• 啟動製造執行系統 (MES) 工單全自動智慧派工閉環；\n• 建立全集團 AI Token 計費分攤與持續訓練機制。", "交付 7：《光寶可重複使用 AI 平台投產白皮書》\n交付 8：《2027 年度 AI 投資回報與持續優化計畫》")
    ]
    for r_idx, r_data in enumerate(p28_rows, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p28.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=65, bottom=65, left=90, right=90)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8)
            r.font.color.rgb = RGB_DARK
    doc.add_page_break()

    # PAGE 29: Enterprise Risk Register & Dual-Track Mitigation
    add_header_banner(doc, 29, "企業級關鍵風險登錄表與雙軌避震對策", "RISK REGISTER", "針對光寶 S/4HANA 升級與 AI 導入可能遭遇之 5 大風險提供結構化解法")
    img_rk_path = os.path.join(IMG_DIR, 'diagram_risk.png')
    if os.path.exists(img_rk_path):
        doc.add_picture(img_rk_path, width=Inches(7.2))
    tbl_p29 = doc.add_table(rows=6, cols=4)
    tbl_p29.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p29.columns[0].width = Inches(1.3)
    tbl_p29.columns[1].width = Inches(1.8)
    tbl_p29.columns[2].width = Inches(2.6)
    tbl_p29.columns[3].width = Inches(1.5)
    headers_p29 = ["風險識別編號", "風險情境與潛在衝擊", "雙軌緩解對策與工程控制", "責任人 / 監控"]
    for i, h in enumerate(headers_p29):
        c = tbl_p29.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=65, bottom=65, left=80, right=80)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY
    p29_rows = [
        ("RISK 01\n(S/4HANA 延誤)", "ERP 升級進度緊張，若 AI 整合牽涉核心資料庫修改，可能影響 2027/01/04 切換窗口。", "恪守 SAP Clean Core 原則。將 AI 運算完全外掛於微服務層，以 Kafka CDC 非同步抽取，零衝擊核心。", "AI 平台負責人\nS/4HANA PMO"),
        ("RISK 02\n(組織山頭防禦)", "資深開國同仁擔心地位受損，暗中消極抵抗，導致新平台無人調用。", "實施「戰略絕緣層」與 ORID 工作坊，確立「承認能力、同意問題、建立公平規則」，授權潛力星。", "AI 平台負責人\nHR 部門主管"),
        ("RISK 03\n(模型幻覺錯料)", "LLM 推薦非合格之替代料，導致工程事故或大批量退貨賠償。", "強式 Agentic RAG 整合 PLM 參數庫，實施規格二次強校驗，強制附帶引用來源，保留專家最終審核權。", "AI 演算法主管\nPLM 負責人"),
        ("RISK 04\n(工廠網路中斷)", "海外工廠聯外網絡不穩定，雲端 AI 斷線造成產線停擺。", "落實 Purdue 模型 Air-Gapped 實體分段，邊緣節點具備離線推理能耐與本地緩衝降級模式。", "OT 網路主管\n各廠總廠長"),
        ("RISK 05\n(Token 成本失控)", "各單位任意呼叫旗艦大模型，導致雲端算力與 API 授權費用幾何級數暴增。", "模型網關實施 Smart Routing 自動降本分流演算法，嚴格設定各事業部每月調用配額與超額警報。", "FinOps 架構師\n財務審計專員")
    ]
    for r_idx, r_data in enumerate(p29_rows, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p29.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=65, bottom=65, left=80, right=80)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8)
            r.font.color.rgb = RGB_DARK
    doc.add_page_break()

    # PAGE 30: Conclusion & Executive Commitment
    add_header_banner(doc, 30, "結語與候選人承諾", "CONCLUSION", "戰時領導力、功成不必在我、全力輔佐光寶千億製造網絡")
    add_callout(doc,
        "「在非成熟治理土壤中，當老闆深陷焦慮、中間層退化為傳話筒、開國老臣山頭盤據時，唯一的生還之道：硬核商業對賭、極簡防護工具、與戰略絕緣層。自己專注於骨架搭建，成就團隊，功成不必在我。」—— Howard Liao Ph.D.\n"
        "光寶科技正邁向綠色資料中心、永續運輸與高效能基礎設施的全球領導者。本人帶著 27+ 年工程熱忱與 20+ 年 C-Level 實戰歷練，隨時準備就位，全力輔佐董事長、李逢堉資訊長與全體光寶同仁！",
        title="候選人誓言：戰時管理者的格局與擔當"
    )
    p_p30 = doc.add_paragraph()
    r_p30 = p_p30.add_run(
        "【致光寶科技董事長與李逢堉資訊長之四大承諾】\n"
        "1. 架構承諾：先串數據再談 AI，恪守 Clean Core，絕不干擾 2027 年 1 月 4 日 S/4HANA 72h 停機切換；\n"
        "2. 效益承諾：以可重複使用的平台中樞，到任 1 週內以 Quick Wins 交付量化成果，半年內讓 AI 帶來實質 EBITDA 效益；\n"
        "3. 組織承諾：化解山頭心防，以 ORID 與指標字典引導業務與工程團隊，培育光寶自己的內部 PO 梯隊；\n"
        "4. 資安承諾：以 ISO 27001 主導稽核員標準把關，嚴守工廠網路 Air-Gapped 隔離，核心圖面專利 100% 不出廠。"
    )
    r_p30.font.name = "STHeiti Light"
    r_p30.font.size = Pt(9.5)
    r_p30.font.color.rgb = RGB_DARK
    p_sign = doc.add_paragraph()
    p_sign.paragraph_format.space_before = Pt(20)
    r_s = p_sign.add_run("呈報人簽署： Howard Liao Ph.D. (廖倫豪 博士) ｜ 日期：2026 年 11 月 05 日 ｜ 地點：台北市內湖區光寶科技總部面試呈報")
    r_s.font.name = "STHeiti Medium"
    r_s.font.size = Pt(9)
    r_s.font.bold = True
    r_s.font.color.rgb = RGB_PRIMARY

    doc.save(OUTPUT_DOCX)
    print(f"Successfully generated 30-page dossier at: {OUTPUT_DOCX}")

if __name__ == '__main__':
    build_30page_dossier()
