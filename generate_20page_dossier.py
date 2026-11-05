#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate 20-Page Comprehensive Executive Interview Dossier (.docx)
Role: (NEW!) IT AI 平台負責人 (Global Head of Enterprise AI Strategy & Platform)
Company: 光寶科技 (LITE-ON Technology Corporation · 2301.TW)
Author: Howard Liao Ph.D. (廖倫豪 博士)
Style: Milan Warm Amber (米蘭暖琥珀風格)
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
HEX_ACCENT_GOLD = "D97706"  # 琥珀金 Ochre Gold

RGB_PRIMARY = RGBColor(180, 83, 9)
RGB_SECONDARY = RGBColor(120, 53, 15)
RGB_DARK = RGBColor(41, 37, 36)
RGB_MUTED = RGBColor(120, 113, 108)
RGB_ACCENT_GOLD = RGBColor(217, 119, 6)

def set_cell_background(cell, hex_color):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
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
    set_cell_margins(cell_left, top=100, bottom=100, left=150, right=80)
    set_cell_margins(cell_right, top=100, bottom=100, left=80, right=150)
    
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
    r_title.font.size = Pt(13)
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
    
    r_pg = p_right.add_run(f"PAGE {page_num:02d} / 20")
    r_pg.font.name = "Arial"
    r_pg.font.size = Pt(9.5)
    r_pg.font.bold = True
    r_pg.font.color.rgb = RGB_PRIMARY

    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_before = Pt(2)
    p_spacer.paragraph_format.space_after = Pt(4)

def add_callout(doc, text, title=None, hex_bg=HEX_CARD_BG, hex_border=HEX_PRIMARY):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(7.2)
    
    cell = tbl.cell(0, 0)
    set_cell_background(cell, hex_bg)
    set_cell_margins(cell, top=100, bottom=100, left=160, right=140)
    
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

def build_dossier():
    doc = docx.Document()

    # Set margins to 0.65 inch for rich 20-page layout
    for section in doc.sections:
        section.top_margin = Inches(0.65)
        section.bottom_margin = Inches(0.65)
        section.left_margin = Inches(0.65)
        section.right_margin = Inches(0.65)

        # Header
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("光寶科技 (2301.TW) 全球 AI 策略與平台演進藍圖 ｜ 高階面試呈報專案報告")
        hrun.font.name = "STHeiti Light"
        hrun.font.size = Pt(8)
        hrun.font.color.rgb = RGB_MUTED

        # Footer
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        frun_l = fp.add_run("報告人：Howard Liao Ph.D. (廖倫豪 博士)  ｜  機密文件 僅供光寶科技董事長、CIO 與面試審查團專閱")
        frun_l.font.name = "STHeiti Light"
        frun_l.font.size = Pt(8)
        frun_l.font.color.rgb = RGB_MUTED

    print("Building Page 1: Cover Page...")
    # =========================================================================
    # PAGE 1: 封面 (Executive Cover Page)
    # =========================================================================
    p_cov_badge = doc.add_paragraph()
    p_cov_badge.paragraph_format.space_before = Pt(30)
    p_cov_badge.paragraph_format.space_after = Pt(8)
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
    r_ct.font.size = Pt(23)
    r_ct.font.bold = True
    r_ct.font.color.rgb = RGB_DARK

    p_cov_sub = doc.add_paragraph()
    p_cov_sub.paragraph_format.space_before = Pt(0)
    p_cov_sub.paragraph_format.space_after = Pt(20)
    r_cs = p_cov_sub.add_run("針對全球 86 家子公司、112 座製造工廠之骨幹升級大戰，深挖「問題背後的問題」，以雙環數據總線貫通替代料選用、齊套料排程與智慧調機")
    r_cs.font.name = "STHeiti Light"
    r_cs.font.size = Pt(11)
    r_cs.font.color.rgb = RGB_MUTED

    # Table with Candidate & Interview Info
    tbl_cov = doc.add_table(rows=5, cols=2)
    tbl_cov.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_cov.autofit = False
    tbl_cov.columns[0].width = Inches(2.2)
    tbl_cov.columns[1].width = Inches(5.0)

    cov_info = [
        ("應聘目標職缺", "(NEW!) IT AI 平台負責人 (Global Head of Enterprise AI Strategy & Platform)"),
        ("面試呈報對象", "第一關：資訊長 李逢堉 ｜ 技術顧問 ｜ 人資長 (現場)\n第二關：董事長 (現場)"),
        ("報告人", "Howard Liao Ph.D. (廖倫豪 博士) ｜ 資訊管理博士 ｜ 前鴻海中央資訊技術處長"),
        ("核心管理實績", "27+ 年 IT & 工程歷練 ｜ 20+ 年 C-Level 治理 ｜ $10M+ 資本對齊 ｜ 100% Zero Outage"),
        ("專案線上互動門戶", "https://howardliao.github.io/2301/ (支援手機 PWA 與桌面親和性 RWD)")
    ]

    for idx, (k, v) in enumerate(cov_info):
        c0 = tbl_cov.cell(idx, 0)
        c1 = tbl_cov.cell(idx, 1)
        set_cell_background(c0, HEX_HEADER_BG)
        set_cell_background(c1, HEX_SURFACE)
        set_cell_margins(c0, top=90, bottom=90, left=120, right=120)
        set_cell_margins(c1, top=90, bottom=90, left=120, right=120)

        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(0)
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(k)
        r0.font.name = "STHeiti Medium"
        r0.font.size = Pt(9.5)
        r0.font.bold = True
        r0.font.color.rgb = RGB_PRIMARY

        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_before = Pt(0)
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run(v)
        r1.font.name = "STHeiti Light"
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = RGB_DARK

    p_cov_bot = doc.add_paragraph()
    p_cov_bot.paragraph_format.space_before = Pt(45)
    p_cov_bot.paragraph_format.space_after = Pt(0)
    r_bot = p_cov_bot.add_run("裝幀規範：米蘭暖琥珀出版級標準 ｜ 適用體系：TOGAF 10 ADM (32 Views) / ISO 42001 / ISO 27001 / SAP Clean Core")
    r_bot.font.name = "Arial"
    r_bot.font.size = Pt(8.5)
    r_bot.font.color.rgb = RGB_MUTED

    doc.add_page_break()

    print("Building Page 2: Executive Letter & Bento Metrics...")
    # =========================================================================
    # PAGE 2: 執行摘要與致光寶面試官的一封信 (Executive Letter to Panel)
    # =========================================================================
    add_header_banner(doc, 2, "執行摘要與致光寶面試審查團的一封信", "EXECUTIVE LETTER", "直球回應第一關（CIO、技術顧問、人資長）與第二關（董事長）之核心關切")

    add_callout(doc, 
        "「見招拆招，只能解決眼前這一關。真正的問題，往往藏在問題的背後。」—— 光寶科技資訊長 李逢堉\n"
        "光寶正在打一場硬仗：將全球 86 家公司、112 座工廠的 ERP 升級至 SAP S/4HANA，並於 2027 年 1 月 4 日同步切換。然而，S/4HANA 只是數位骨幹；真正能為光寶帶來看得見的經濟效益、增加製造與供應鏈彈性的，是骨幹之上能主動預測、主動建議的 AI 決策大腦。本人以戰時管理者的責任感，隨時準備與團隊並肩作戰。",
        title="戰略破題：深挖問題背後的結構性根因"
    )

    p_p2_1 = doc.add_paragraph()
    p_p2_1.paragraph_format.space_before = Pt(4)
    p_p2_1.paragraph_format.space_after = Pt(4)
    r_p2_1 = p_p2_1.add_run(
        "尊敬的董事長、李逢堉資訊長、技術顧問與人資長：\n"
        "當前企業導入 AI 最常見的陷阱，是陷入「零散 POC 自嗨」：各部門各自找工具寫提示詞，產出一堆無法沉澱為資產的玩具，既無法與核心交易系統閉環，又大幅拉高資安外洩與算力浪費風險。\n"
        "光寶需要的是一位 Forward-Deployed AI Architect 兼具 C-Level 治理格局的領航者：\n"
        "1. 懂製造與骨幹：深知 SAP ECC 至 S/4HANA 升級的敏感神經，恪守 Clean Core 原則，以 Kafka CDC 串流解耦，絕不干擾核心停機窗口；\n"
        "2. 懂平台與重用：能將零碎的模型調用收斂為單一企業級模型網關（HowardRoute），降低 20~40% Token 成本，讓 AI 成為即插即用的水庫；\n"
        "3. 懂組織與人性：在傳統製造文化中化解技術老將的防衛心理，以露骨商業算盤帶動業務同仁轉型為 AI 原生 PO。"
    )
    r_p2_1.font.name = "STHeiti Light"
    r_p2_1.font.size = Pt(9.5)
    r_p2_1.font.color.rgb = RGB_DARK

    # Insert Bento Diagram
    img_bento_path = os.path.join(IMG_DIR, 'diagram_bento.png')
    if os.path.exists(img_bento_path):
        p_img = doc.add_paragraph()
        p_img.paragraph_format.space_before = Pt(6)
        p_img.paragraph_format.space_after = Pt(4)
        doc.add_picture(img_bento_path, width=Inches(7.2))

    doc.add_page_break()

    print("Building Page 3: LITE-ON Strategic Context...")
    # =========================================================================
    # PAGE 3: 光寶科技現況脈絡解構：全球製造與 S/4HANA 轉型大局
    # =========================================================================
    add_header_banner(doc, 3, "光寶科技現況脈絡解構：全球製造與 S/4HANA 轉型大局", "STRATEGIC CONTEXT", "86 間子公司、112 座製造工廠、20+ 跨國據點之複雜度剖析")

    add_callout(doc,
        "光寶產品線橫跨雲端伺服器電源、網路通訊、消費電子、車用電子到智慧城市。資訊系統不是輔助工具，而是支撐千億營收的骨幹。\n"
        "2026 年 3 月啟動的 S/4HANA 專案包含 16 項新功能導入與 27 項管理流程優化，時程壓縮至 10 個月，停機 72 小時上線。此役只許成功，不容差錯。",
        title="商周實地調研：光寶規模與關鍵時程"
    )

    tbl_p3 = doc.add_table(rows=4, cols=3)
    tbl_p3.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p3.autofit = False
    tbl_p3.columns[0].width = Inches(1.8)
    tbl_p3.columns[1].width = Inches(2.7)
    tbl_p3.columns[2].width = Inches(2.7)

    headers_p3 = ["維度 / 節點", "光寶科技真實痛點與現況", "Howard 互補架構之解法與落地路徑"]
    for i, h in enumerate(headers_p3):
        c = tbl_p3.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=80, bottom=80, left=100, right=100)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY

    rows_p3 = [
        ("S/4HANA 升級大戰\n(2027/01/04 切換)", "核心系統骨幹牽一髮動全身，全球 86 家公司同時切換，停機時間僅 72 小時，任何客製化 AI 均嚴禁直接修改 ERP 核心。", "恪守 SAP Clean Core 原則。將 AI 邏輯完全移至外掛微服務層，透過 Debezium CDC 異動捕捉技術入湖，對 ERP 資料庫零負載。"),
        ("跨事業部數據對齊\n與沖銷邏輯", "過去合併報表每逢月結，BW 抽取數據需人工反覆核對，耗費會計團隊大量精力於沖銷對帳。", "借鏡 IBM 成功重塑數據映射之經驗，進一步建立跨 BU 主數據 (MDM) 血緣追蹤，為 AI 提供即時乾淨且具備審計軌跡之高質量數據。"),
        ("下一個里程碑\n「讓 ERP 更 AI」", "李逢堉資訊長明言：線的另一邊是製造端主動判斷。MES 與 ERP 需緊密結合，在替代料、齊套料與工單排程全自動化。", "導入製造預測大腦 HowardPro 與雙環 Data Bus，建立替代料自動驗證演算法，使產線具備自動排產與動態避險之自我感知能力。")
    ]

    for r_idx, r_data in enumerate(rows_p3, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p3.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=80, bottom=80, left=100, right=100)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8.5)
            r.font.color.rgb = RGB_DARK

    p_p3_bot = doc.add_paragraph()
    p_p3_bot.paragraph_format.space_before = Pt(8)
    p_p3_bot.paragraph_format.space_after = Pt(0)
    r_p3_b = p_p3_bot.add_run("核心戰略洞察：光寶需要的不是「再多買一套工具」，而是「把既有 PLM、SAP、MES 串成具備智慧推論閉環的自適應系統」。")
    r_p3_b.font.name = "STHeiti Medium"
    r_p3_b.font.size = Pt(9.5)
    r_p3_b.font.color.rgb = RGB_PRIMARY

    doc.add_page_break()

    print("Building Page 4: Core Positioning & Paradigm Shift...")
    # =========================================================================
    # PAGE 4: 職位定位與總體策略願景：從零散應用到企業級可重複平台
    # =========================================================================
    add_header_banner(doc, 4, "職位定位與總體策略願景：從零散應用到企業級可重複平台", "CORE POSITIONING", "把 AI 從單一應用推進到產品，再到可重複使用的平台，帶來經濟效益")

    p_p4_lead = doc.add_paragraph()
    p_p4_lead.paragraph_format.space_before = Pt(0)
    p_p4_lead.paragraph_format.space_after = Pt(4)
    r_p4_l = p_p4_lead.add_run(
        "光寶科技對「IT AI 平台負責人」的定位非常精確：負責光寶整體 AI 策略與執行。把 AI 從單一應用推進到產品，再到可重複使用的平台，並為公司帶來看得見的經濟效益。\n"
        "這代表此職位不是研究員，也不是純演算法工程師，而是「AI 產品線總架構師兼事業夥伴（Business Co-Creator）」。"
    )
    r_p4_l.font.name = "STHeiti Light"
    r_p4_l.font.size = Pt(9.5)
    r_p4_l.font.color.rgb = RGB_DARK

    # Insert Platform Topology Diagram
    img_plat_path = os.path.join(IMG_DIR, 'diagram_platform.png')
    if os.path.exists(img_plat_path):
        p_img = doc.add_paragraph()
        p_img.paragraph_format.space_before = Pt(4)
        p_img.paragraph_format.space_after = Pt(4)
        doc.add_picture(img_plat_path, width=Inches(7.2))

    tbl_p4 = doc.add_table(rows=4, cols=3)
    tbl_p4.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p4.autofit = False
    tbl_p4.columns[0].width = Inches(1.8)
    tbl_p4.columns[1].width = Inches(2.7)
    tbl_p4.columns[2].width = Inches(2.7)

    headers_p4 = ["演進階段", "傳統做法之困境與瓶頸", "Howard 企業級平台化落地實踐"]
    for i, h in enumerate(headers_p4):
        c = tbl_p4.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=70, bottom=70, left=90, right=90)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY

    rows_p4 = [
        ("階段一：單一零散應用\n(Ad-hoc Apps)", "各單位私自採購 API，各寫 Python 腳本；程式碼無人維護，資料散落各處，機密外洩風險極高。", "集中納管於 HowardRoute API 網關，統一驗證與授權，即時清點影子 API，確保合規稽核。"),
        ("階段二：封裝資料產品\n(Data Products)", "重複開發相似模型，業務單位提需求動輒等待半年，上線後成效難以衡量。", "將常用功能封裝為「微服務資料產品」（如：財務傳票 OCR、規格書問答 Agent、製程異常診斷服務），即開即用。"),
        ("階段三：可重複平台\n(Reusable Platform)", "運算資源與 Token 成本失控，各事業部互搶 GPU 算力，無標準化維運與監控。", "導入 Smart Routing 與自動降本演算法，為光寶 86 家公司建立計費與效益分攤模型，直觀呈現 ROI。")
    ]

    for r_idx, r_data in enumerate(rows_p4, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p4.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=70, bottom=70, left=90, right=90)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8)
            r.font.color.rgb = RGB_DARK

    doc.add_page_break()

    print("Building Page 5: Scope 1 - Prioritization & TOGAF BDAT...")
    # =========================================================================
    # PAGE 5: 工作內容 1：定義優先導入領域，規劃企業級 AI 平台藍圖
    # =========================================================================
    add_header_banner(doc, 5, "工作內容 1：定義優先領域，規劃企業級 AI 平台藍圖", "WORK SCOPE 1", "與高階主管定義優先導入 AI 領域，規劃 AI 平台藍圖 ｜ 對齊 HowardLiao/RSI ＆ 8436")

    add_callout(doc,
        "在信源全球 (RSI) 2027 策略藍圖專案中，本人向 CEO 暨經管會呈報 18 頁策略簡報，界定五大支柱與 AI Use Case & ROI 模型；在大江生醫 (8436) 專案中，繪製 TOGAF ADM 32 全架構視圖，將企業戰略無縫解構為技術拓撲。",
        title="GitHub 實績背書：HowardLiao/RSI ＆ HowardLiao/8436"
    )

    p_p5_body = doc.add_paragraph()
    p_p5_body.paragraph_format.space_before = Pt(4)
    p_p5_body.paragraph_format.space_after = Pt(4)
    r_p5_b = p_p5_body.add_run(
        "導入 AI 不能由技術人員閉門造車，必須由上而下與高階主管對齊戰略優先級。本人將在到任 60 天內，採用成熟的 TOGAF 企業架構四階矩陣 (BDAT) 為光寶建立藍圖："
    )
    r_p5_b.font.name = "STHeiti Light"
    r_p5_b.font.size = Pt(9.5)
    r_p5_b.font.color.rgb = RGB_DARK

    tbl_p5 = doc.add_table(rows=5, cols=3)
    tbl_p5.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p5.autofit = False
    tbl_p5.columns[0].width = Inches(1.5)
    tbl_p5.columns[1].width = Inches(3.0)
    tbl_p5.columns[2].width = Inches(2.7)

    headers_p5 = ["BDAT 架構層級", "光寶次世代 AI 平台對位組件", "高階主管對齊與治理目標"]
    for i, h in enumerate(headers_p5):
        c = tbl_p5.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=70, bottom=70, left=90, right=90)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY

    bdat_rows = [
        ("B 業務架構\n(Business)", "全球 86 家子公司營運流向、112 座製造工廠生管排程、採購詢價比價、研發規格驗證。", "對齊 CEO/COO 經營目標，確保 AI 專案直接回饋 EBITDA、降低缺料停線風險。"),
        ("D 數據架構\n(Data)", "雙環 Data Bus (Kafka + EMQX)、SAP S/4HANA CDC 即時異動流、主數據血緣 (DataHub)。", "打破工廠與總部數據孤島，落實 ALCOA+ 數據完整性與跨國數據主權合規。"),
        ("A 應用架構\n(Application)", "多模型網關 HowardRoute、任務編排 HowardAGent、製造大腦 HowardPro、APISIX 影子防護。", "建立標準 API 服務目錄，提供各 BU 即插即用的微服務產品，杜絕重複造輪子。"),
        ("T 技術架構\n(Technology)", "混合多雲 GPU 算力調度、Air-Gapped 工廠邊緣節點、不可竄改備份與災害復原體系。", "落實 Zero Outage 99.99% 可用性 SLA，實現毫秒級容災切換與極致成本控制。")
    ]

    for r_idx, r_data in enumerate(bdat_rows, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p5.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=70, bottom=70, left=90, right=90)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8)
            r.font.color.rgb = RGB_DARK

    add_callout(doc,
        "為求深度挖掘「問題背後的問題」，將沿用信源全球 (RSI) 成熟的訪談題庫：\n"
        "• 針對 COO (生產副總)：深入探討工單排程瓶頸、機台嫁動率 (OEE) 虛報盲點與產線缺料實況；\n"
        "• 針對 CFO (財務長)：審查各事業部 Token 投資回報率、呆料認列與跨國沖銷作業時間；\n"
        "• 針對海外各廠總廠長：盤點現場網路連線穩定度、在地語言工單轉換障礙與資深師傅經驗傳承瓶頸。",
        title="跨 C-Level 與總廠長之結構化訪談清冊"
    )

    doc.add_page_break()

    print("Building Page 6: Scope 2 - Reusable Data Products & Gateway...")
    # =========================================================================
    # PAGE 6: 工作內容 2：零散應用做成可重複使用的資料產品與平台
    # =========================================================================
    add_header_banner(doc, 6, "工作內容 2：零散應用產品化與可重複數據中樞", "WORK SCOPE 2", "把零散應用做成可重複使用的資料產品與平台 ｜ 對齊 HowardLiao/8436")

    add_callout(doc,
        "在大江生醫 (8436) 實戰中，本人主導建立企業級多模型網關 HowardRoute 與任務編排中樞 HowardAGent：\n"
        "1. 單一相容 OpenAI 端點，納管 250+ 開源與商用模型，具備 0% 額外加價 (Markup)；\n"
        "2. Smart Routing 演算法依據 Prompt 難度動態派發小型快速模型或旗艦推理模型，省 20~40% Token 成本；\n"
        "3. 毫秒級自動容錯轉移 (Failover)，確保業務連續性不受單一公有雲模型服務商中斷影響。",
        title="平台核心實踐：HowardRoute 模型網關"
    )

    p_p6_body = doc.add_paragraph()
    p_p6_body.paragraph_format.space_before = Pt(4)
    p_p6_body.paragraph_format.space_after = Pt(4)
    r_p6_b = p_p6_body.add_run(
        "為徹底解決光寶各部門「自建零碎工具、維運成本高昂、無法重複利用」的痛點，本人規劃三大共用資料產品標準庫："
    )
    r_p6_b.font.name = "STHeiti Light"
    r_p6_b.font.size = Pt(9.5)
    r_p6_b.font.color.rgb = RGB_DARK

    tbl_p6 = doc.add_table(rows=4, cols=3)
    tbl_p6.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p6.autofit = False
    tbl_p6.columns[0].width = Inches(2.0)
    tbl_p6.columns[1].width = Inches(2.6)
    tbl_p6.columns[2].width = Inches(2.6)

    headers_p6 = ["標準資料產品名稱", "技術組件與封裝能力", "光寶業務場景重複使用效益"]
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
        ("通用多模態憑證辨識\n(Document OCR Product)", "自研排版還原演算法 + 多模態視覺模型微調，支援發票、海關報單、送貨簽收單自動結構化。", "財務部傳票核銷工時減少 75%，各工廠進料驗收單一鍵登錄 SAP，杜絕人為謄打失誤。"),
        ("企業級 Agentic RAG\n(Knowledge Hub Product)", "整合光寶產品規格手冊、ISO 制度規章、專利清冊；強制來源標註 (Citations)，準確率 95%。", "業務部詢價規格比對速度提升 2 倍，全球技術客服初次諮詢解決率提高 40%，杜絕模型幻覺。"),
        ("工業虛擬量測大腦\n(Industrial AI Product)", "AutoML 特徵工程 + 邊緣即時推理容器，支援 Air-Gapped 隔離部署與 Domain Twin 數位代理。", "112 座工廠 SMT/AOI 產線通用，無須為每條產線從頭訓練模型，大幅降低模型客製成本。")
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

    add_callout(doc,
        "在 API 治理層級，全面導入 Apache APISIX 與 Keycloak：\n"
        "• 影子 API 自動清點：防止開發人員私下建立未受控的 AI 端點；\n"
        "• AI 阻斷 BOLA 越權攻擊：在微服務入口即時防禦惡意參數篡改；\n"
        "• 計費與調用度量：精確記錄每位使用者、每個 BU 的 Token 消耗，達成看得見的財務透明治理。",
        title="資安與 API 平台防護網"
    )

    doc.add_page_break()

    print("Building Page 7: Scope 3 - PLM, SAP, MES AI Stack (Part 1)...")
    # =========================================================================
    # PAGE 7: 工作內容 3 (上)：建立和 SAP、PLM、MES 互補的 AI Stack
    # =========================================================================
    add_header_banner(doc, 7, "工作內容 3 (上)：建立和 SAP、PLM、MES 互補的 AI Stack", "WORK SCOPE 3", "把 PLM、SAP、MES 串成一條數據流 ｜ 對齊 HowardLiao/4163 實戰經驗")

    add_callout(doc,
        "在鐿鈦科技 (4163) 專案中，本人提出「把 PLM、SAP、MES 串成一條數據流」的四大核心方案：\n"
        "1. 核心原則：盡量使用 SAP 標準功能，減少客製化技術債；先串資料，再談 AI；\n"
        "2. 少一次人工轉檔：逐一改為系統加密 API 介接，免除重複謄打；\n"
        "3. 料號與 BOM 一致：PLM 設計變更自動同步 SAP 與 MES，杜絕用錯版本；\n"
        "4. 庫存與良率即時化：多廠區採用同一套數據度量即時呈現戰情室。",
        title="實戰經驗映照：4163 系統整合精要"
    )

    p_p7_body = doc.add_paragraph()
    p_p7_body.paragraph_format.space_before = Pt(4)
    p_p7_body.paragraph_format.space_after = Pt(4)
    r_p7_b = p_p7_body.add_run(
        "光寶當前正全速推動 SAP S/4HANA 升級，此時推動 AI 最忌諱的就是直接修改 ERP 核心邏輯（Modifications）。\n"
        "本人深知大型製造業骨幹的脆弱性，主張建立「與 S/4HANA 互補、而非干擾」的 AI Stack："
    )
    r_p7_b.font.name = "STHeiti Light"
    r_p7_b.font.size = Pt(9.5)
    r_p7_b.font.color.rgb = RGB_DARK

    tbl_p7 = doc.add_table(rows=4, cols=3)
    tbl_p7.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p7.autofit = False
    tbl_p7.columns[0].width = Inches(1.8)
    tbl_p7.columns[1].width = Inches(2.7)
    tbl_p7.columns[2].width = Inches(2.7)

    headers_p7 = ["核心系統節點", "系統定位與傳統介接痛點", "AI Stack 互補增強模式"]
    for i, h in enumerate(headers_p7):
        c = tbl_p7.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=70, bottom=70, left=90, right=90)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY

    p7_rows = [
        ("PLM 產品生命週期\n(設計 / 規格 / ECN)", "工程變更 (ECN) 頻繁，新零件與規格手冊大多為非結構化 PDF，人工輸入 ERP 料號耗時且容易錯漏。", "建立 PLM 規格智能解析 Agent，工程變更發布時自動抽取規格特徵，結構化寫入物料主數據，自動通知 MES 更新工藝路線。"),
        ("SAP S/4HANA\n(訂單 / 物料 / 財務)", "86 間公司核心交易骨幹，升級期不容許效能損耗與架構雜訊，複雜業務邏輯牽一髮動全身。", "恪守 SAP Clean Core 原則。透過標準 OData / REST API 與 Debezium CDC 異動監控，在 ERP 外部建立高效能運算快取。"),
        ("MES 製造執行系統\n(現場工單 / 良率)", "112 座工廠設備協議各異（Modbus、OPC-UA、SECS/GEM），產線資料量大且零碎，難以即時反映至採購排程。", "在工廠端部署 EMQX MQTT 物聯網邊緣總線，將機台良率、加工時間即時清洗聚合，回填至 MES 工單，驅動 AI 動態排產。")
    ]

    for r_idx, r_data in enumerate(p7_rows, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p7.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=70, bottom=70, left=90, right=90)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8)
            r.font.color.rgb = RGB_DARK

    p_p7_bot = doc.add_paragraph()
    p_p7_bot.paragraph_format.space_before = Pt(8)
    p_p7_bot.paragraph_format.space_after = Pt(0)
    r_p7_bt = p_p7_bot.add_run("架構承諾：與 IBM 顧問團隊同向發力，保證 AI 平台的掛載 100% 不干擾 2027/01/04 全球 S/4HANA 的上線切換。")
    r_p7_bt.font.name = "STHeiti Medium"
    r_p7_bt.font.size = Pt(9.5)
    r_p7_bt.font.color.rgb = RGB_PRIMARY

    doc.add_page_break()

    print("Building Page 8: Scope 3 - Dual-Ring Data Bus & Shop-Floor AI...")
    # =========================================================================
    # PAGE 8: 工作內容 3 (下)：雙環 Data Bus 與製造端痛點攻堅
    # =========================================================================
    add_header_banner(doc, 8, "工作內容 3 (下)：雙環 Data Bus 與製造端痛點攻堅", "WORK SCOPE 3", "直擊光寶李逢堉資訊長痛點：替代料選用、齊套料規劃、工單排程全自動化")

    # Insert ERP-MES AI Stack Diagram
    img_erp_path = os.path.join(IMG_DIR, 'diagram_erp_mes.png')
    if os.path.exists(img_erp_path):
        p_img = doc.add_paragraph()
        p_img.paragraph_format.space_before = Pt(0)
        p_img.paragraph_format.space_after = Pt(4)
        doc.add_picture(img_erp_path, width=Inches(7.2))

    tbl_p8 = doc.add_table(rows=4, cols=3)
    tbl_p8.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p8.autofit = False
    tbl_p8.columns[0].width = Inches(1.8)
    tbl_p8.columns[1].width = Inches(2.7)
    tbl_p8.columns[2].width = Inches(2.7)

    headers_p8 = ["製造端關鍵痛點", "現行作業瓶頸 (問題背後的問題)", "AI 決策大腦全自動化閉環解法"]
    for i, h in enumerate(headers_p8):
        c = tbl_p8.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=65, bottom=65, left=90, right=90)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY

    p8_rows = [
        ("替代料選用\n(Part Substitution)", "供應鏈料況波動或原廠停產時，工程師需人工翻閱 PLM 規格書比對電性與封裝，核可週期長，常導致產線停擺。", "建立「零件規格知識圖譜 + LLM 推理」，當缺料警報觸發時，系統在數秒內精確推薦符合規範之替代料並標註驗證依據。"),
        ("齊套料動態規劃\n(Kit Readiness AI)", "傳統工單排程僅看 ERP 帳面庫存，忽略產線在製品、檢驗中料件與跨廠在途運輸，經常開工後才發現欠料。", "雙環 Data Bus 即時監控 SAP 物料異動與 MES 現場領料，動態演算每張工單的「齊套置信度」，未達門檻不予派工，消除產線半套呆滯。"),
        ("工單智慧排程\n(Dynamic Dispatching)", "生管人員仰賴個人經驗與 Excel 排產，面對插單、設備故障或急件時無法全域最佳化，機台換模時間過長。", "以強化學習 + 運籌演算法 (OR) 打造動態排產引擎，平衡機台利用率、換模損失與訂單交付期，工單調整即時推播至 HMI。")
    ]

    for r_idx, r_data in enumerate(p8_rows, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p8.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=65, bottom=65, left=90, right=90)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8)
            r.font.color.rgb = RGB_DARK

    add_callout(doc,
        "雙環 Data Bus 核心工程價值：\n"
        "• IT 骨幹總線：Apache Kafka 處理跨國 86 家子公司的高吞吐業務事件；\n"
        "• SAP CDC 引擎：Debezium 即時監聽 S/4HANA 資料庫日誌，零延遲同步異動且不造成任何查詢壓力；\n"
        "• OT 邊緣物聯網：EMQX Broker 支援各工廠斷網續傳與本地緩衝，確保工廠斷網時產線仍能持續作業。",
        title="數據總線高可用韌性設計"
    )

    doc.add_page_break()

    print("Building Page 9: Scope 4 - Talent Pipeline & War-Time Leadership...")
    # =========================================================================
    # PAGE 9: 工作內容 4 (上)：組建 AI 組織梯隊與化解開國老臣山頭防衛
    # =========================================================================
    add_header_banner(doc, 9, "工作內容 4 (上)：組建 AI 組織梯隊與化解山頭防衛", "WORK SCOPE 4", "組建 AI 組織與人才梯隊，帶領技術主管與工程師 ｜ 對齊 HowardLiao/journey")

    add_callout(doc,
        "在《組織從零到一的降維突圍實戰報告》（HowardLiao/journey）中，本人深刻復盤在非成熟治理土壤中，面對「老闆隕石開發、中間傳話失真、開國老臣山頭防衛、基層迷茫」的破局實踐。\n"
        "任何大型製造集團推動技術升級，最大的阻力從來不是演算法，而是組織既得利益者的深層防衛心靈。唯有具備戰時管理手腕，才能成就團隊。",
        title="實戰復盤：組織變革的核心自白"
    )

    p_p9_body = doc.add_paragraph()
    p_p9_body.paragraph_format.space_before = Pt(4)
    p_p9_body.paragraph_format.space_after = Pt(4)
    r_p9_b = p_p9_body.add_run(
        "光寶在台北、新北、中科、高雄與全球各地擁有眾多資深 IT 與工程團隊。在推動 AI 平台化時，開國元老與資深主管必然面臨三種深層防衛："
    )
    r_p9_b.font.name = "STHeiti Light"
    r_p9_b.font.size = Pt(9.5)
    r_p9_b.font.color.rgb = RGB_DARK

    tbl_p9 = doc.add_table(rows=4, cols=3)
    tbl_p9.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p9.autofit = False
    tbl_p9.columns[0].width = Inches(1.8)
    tbl_p9.columns[1].width = Inches(2.7)
    tbl_p9.columns[2].width = Inches(2.7)

    headers_p9 = ["深層心理防禦機制", "資深同仁之真實顧慮與防禦表現", "Howard 實戰破冰與引導機制 (ORID)"]
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
        ("地位防禦\n(Status Defense)", "擔心新 AI 平台架構否定其過去十餘年建立的系統與成就，認為外部技術威脅其技術話語權。", "運用「承認能力、同意問題、建立公平規則」原則。公開肯定歷史架構對千億營收之貢獻，邀請資深主管擔任平台標準審查委員。"),
        ("利益防禦\n(Interest Defense)", "憂慮自動化取代既有人力維護職缺，或新考核指標對資深同仁不利，暗中拖延配合進度。", "透過標準職務說明書 (JD) 與雙軌職涯規劃，讓資深同仁從重複維護的泥潭中解脫，轉型為業務架構顧問與領域專家。"),
        ("關係防禦\n(Relationship Defense)", "小團體林立、資訊壟斷、跨部門禁止直接交流，習慣向上管理而非橫向協同。", "導入「如果一年後團隊更差是因為什麼」逆向提問工作坊，運用 ORID 焦點討論法凝聚痛點共識，拆解部門壁壘。")
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

    add_callout(doc,
        "戰略絕緣層（Decoupling & Buffer）手腕：\n"
        "當高層有急躁或不切實際的即興需求時，身為 AI 平台負責人必須成為團隊的防彈衣與避震器。自己主動承受管理壓力，專注於骨架搭建與體系健全，讓基層工程師在安全的沙盒中專心攻堅，功成不必在我。",
        title="高階領導心法：保護團隊的戰時絕緣層"
    )

    doc.add_page_break()

    print("Building Page 10: Scope 4 - 9 Engineering Ladders & 9-Box Matrix...")
    # =========================================================================
    # PAGE 10: 工作內容 4 (下)：9 大工程技術發展階梯與人才九宮格
    # =========================================================================
    add_header_banner(doc, 10, "工作內容 4 (下)：9 大工程技術發展階梯與人才九宮格", "WORK SCOPE 4", "打破單點壟斷、授權潛力新星、建立量化工程人才梯隊 ｜ 對齊 HowardLiao/journey")

    # Insert Journey Diagram
    img_jrny_path = os.path.join(IMG_DIR, 'diagram_journey.png')
    if os.path.exists(img_jrny_path):
        p_img = doc.add_paragraph()
        p_img.paragraph_format.space_before = Pt(0)
        p_img.paragraph_format.space_after = Pt(4)
        doc.add_picture(img_jrny_path, width=Inches(7.2))

    tbl_p10 = doc.add_table(rows=4, cols=3)
    tbl_p10.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p10.autofit = False
    tbl_p10.columns[0].width = Inches(2.0)
    tbl_p10.columns[1].width = Inches(2.6)
    tbl_p10.columns[2].width = Inches(2.6)

    headers_p10 = ["工程梯隊發展機制", "具體引導工具與評估模型", "光寶 AI 研發團隊落地指標"]
    for i, h in enumerate(headers_p10):
        c = tbl_p10.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=65, bottom=65, left=90, right=90)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY

    p10_rows = [
        ("9 大技術發展路線\n(Tracks A ~ I)", "涵蓋 A-語言深度、B-分散式高並發、C-資料工程、D-機器學習、E-MLOps/DevOps、F-資訊安全、G-架構設計、H-商業轉譯、I-工程領導。", "每位工程師均有專屬技術坐標與雙季成長路線，杜絕「唯年資論」與盲目內卷，專業職與管理職雙軌並行。"),
        ("前端與應用九宮格\n(Talent 9-Box Matrix)", "以「交付品質」與「技術領導潛力」為雙軸，抽卡牌破冰＋優勢卡對齊，定位出潛力星同仁。", "突破傳統組長單點壟斷，直接授權潛力星工程師主責中大型 AI Feature 上線，賦能基層扛起責任。"),
        ("現代 CISO/CIO/AI 編制\n(HowardLiao/6446 規範)", "規劃 9~14 人核心平台編制：架構師 2 名、Data/MLOps 4 名、後端/API 4 名、業務 PO 4 名。", "確立清晰的 RACI 權責矩陣與可量化 KPI（平台可用性 99.99%、API 延遲 <200ms、Token 成本降低率）。")
    ]

    for r_idx, r_data in enumerate(p10_rows, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p10.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=65, bottom=65, left=90, right=90)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8)
            r.font.color.rgb = RGB_DARK

    add_callout(doc,
        "人才梯隊之承諾：\n"
        "到任 90 天內，完成光寶現有 AI 與資料工程同仁的 1-on-1 深度晤談，產出個人優勢地圖與 9 大路線定位，為光寶留住核心研發骨幹，打造一支具備戰時作戰能力的特種部隊。",
        title="人才賦能之具體成果預期"
    )

    doc.add_page_break()

    print("Building Page 11: Scope 5 - Business-Led Platform & PO Academy...")
    # =========================================================================
    # PAGE 11: 工作內容 5 (上)：業務主導平台與內部 PO 梯隊培育
    # =========================================================================
    add_header_banner(doc, 11, "工作內容 5 (上)：業務主導平台與內部 PO 梯隊培育", "WORK SCOPE 5", "推動業務主導的平台團隊與企業內部 PO 培養，帶動 AI 原生的工作方式 ｜ 對齊 journey")

    add_callout(doc,
        "在 journey 專案中，企劃營運組面臨「成熟產品無事做、新專案天天救火、老闆眼中能力不到位」的惡性循環。\n"
        "本人透過「三好一支援」工作坊全盤梳理需求，並建立 5 大構面「指標字典」，以「0.1% DAU 對賭打平團隊成本」的商業算盤，引導企劃人員具備商業與技術雙重視角，成功轉型為合格的產品負責人 (PO)。",
        title="實務經驗印證：從需求傳話筒到業務 PO"
    )

    p_p11_body = doc.add_paragraph()
    p_p11_body.paragraph_format.space_before = Pt(4)
    p_p11_body.paragraph_format.space_after = Pt(4)
    r_p11_b = p_p11_body.add_run(
        "光寶推動 AI 轉型，絕不能由資訊部在象牙塔裡強推。唯有業務單位主管與生管同仁深刻感受到「AI 能幫我扛 KPI、能讓我準時下班」，轉型才會成功。\n"
        "本人將在光寶推動「企業內部 PO 培訓營」，建立四大核心賦能模組："
    )
    r_p11_b.font.name = "STHeiti Light"
    r_p11_b.font.size = Pt(9.5)
    r_p11_b.font.color.rgb = RGB_DARK

    tbl_p11 = doc.add_table(rows=5, cols=3)
    tbl_p11.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p11.autofit = False
    tbl_p11.columns[0].width = Inches(1.8)
    tbl_p11.columns[1].width = Inches(2.7)
    tbl_p11.columns[2].width = Inches(2.7)

    headers_p11 = ["PO 核心修煉模組", "培養方法與賦能工具", "光寶內部落地交付成效"]
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
        ("商業算盤思維\n(Business Math)", "訓練 PO 拒絕「我覺得這很酷」的模糊需求，強制計算 ROI（EBITDA 提升、工時節省、不良品降損）。", "提報 AI 提案前必須先附帶商業假設與效益模型，杜絕無效益之自嗨型 PoC 專案。"),
        ("5 大構面指標字典\n(Metrics Dictionary)", "建立企劃、營運、行銷、介接、專案等 5 大構面標準度量，統一業務與技術的溝通語言。", "消除跨部門溝通雞同鴨講，使製造現場與資訊團隊以同一套數據度量衡量專案進度。"),
        ("雙軌 MVP 沙盒快跑\n(Dual-Track Sandbox)", "將大專案拆解為 2 週一個迭代的最小可行性產品 (MVP)，設立安全試錯沙盒。", "以快速上線驗證業務反饋，避免耗時一年開發出不符合工廠現場需求的巨大系統。"),
        ("週三分段例會機制\n(Structured Cadence)", "建立「單週需求會議、雙週競品與業務分析、三週核心功能審查、月度數據覆盤」之節奏。", "終結無效冗長會議，讓決策在明確的軌道上高效運轉，確保業務主導權。")
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

    p_p11_bot = doc.add_paragraph()
    p_p11_bot.paragraph_format.space_before = Pt(8)
    p_p11_bot.paragraph_format.space_after = Pt(0)
    r_p11_bt = p_p11_bot.add_run("文化變革成果：把「要我用 AI」轉變為「我要用 AI 解決我的痛點」，讓業務單位成為平台真正的產品經理。")
    r_p11_bt.font.name = "STHeiti Medium"
    r_p11_bt.font.size = Pt(9.5)
    r_p11_bt.font.color.rgb = RGB_PRIMARY

    doc.add_page_break()

    print("Building Page 12: Scope 5 - Departmental AI Rollout...")
    # =========================================================================
    # PAGE 12: 工作內容 5 (下)：Departmental AI 跨部門普及落地法
    # =========================================================================
    add_header_banner(doc, 12, "工作內容 5 (下)：Departmental AI 跨部門普及落地法", "WORK SCOPE 5", "主管先學、資訊部先試、有成效再擴散 ｜ 對齊 HowardLiao/4163 Scheme 3")

    add_callout(doc,
        "在鐿鈦科技 (4163) 規劃中，本人提出極具可操作性的 Departmental AI 四階推動原則：\n"
        "依 ISO 42001 訂立安全規範 -> 主管先學理解邊界 -> 資訊部先試建立樣板 -> 產生可量化成效後再全面擴散。\n"
        "各部門題目會在到任前 60 天深度訪談後確立，兼顧各事業群高階主管真實痛點。",
        title="落地推動法門：穩紮穩打的擴散模型"
    )

    p_p12_body = doc.add_paragraph()
    p_p12_body.paragraph_format.space_before = Pt(4)
    p_p12_body.paragraph_format.space_after = Pt(4)
    r_p12_b = p_p12_body.add_run(
        "為光寶科技四大核心事業單位與職能部門量身打造的專屬落地場景清冊："
    )
    r_p12_b.font.name = "STHeiti Light"
    r_p12_b.font.size = Pt(9.5)
    r_p12_b.font.color.rgb = RGB_DARK

    tbl_p12 = doc.add_table(rows=5, cols=3)
    tbl_p12.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p12.autofit = False
    tbl_p12.columns[0].width = Inches(1.8)
    tbl_p12.columns[1].width = Inches(2.7)
    tbl_p12.columns[2].width = Inches(2.7)

    headers_p12 = ["光寶事業 / 職能部門", "專屬 AI 應用題目與試點場景", "量化效益與驗收成果指標"]
    for i, h in enumerate(headers_p12):
        c = tbl_p12.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=70, bottom=70, left=90, right=90)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY

    p12_rows = [
        ("生產製造單位\n(Manufacturing & OT)", "製程參數知識庫問答、資深師傅除錯經驗數位化、SMT 產線換線輔助。", "設備換模與調機時間縮短 25%，新進技術人員培訓週期從 3 個月降至 3 週。"),
        ("品保與品檢單位\n(QA & QC Units)", "AOI 外觀檢驗影像輔助判讀、跨國客訴資料結構化分類與根本原因 (RCA) 歸因分析。", "品檢誤判率降低 30%，客訴根本原因分析時間從 3 天縮短為 2 小時。"),
        ("全球業務與供應鏈\n(Sales & Supply Chain)", "國際客戶規格書 (Spec) 智能比對、原料歷史價格波動預警、原廠替代料庫存自動推薦。", "詢價與報價處理效率提升 50%，採購呆滯料發生率降低 20%。"),
        ("行政與資訊部門\n(Admin, Legal & IT)", "跨國合約法規條款智能審查、內部 IT Helpdesk 工單自動分類與一線自動排障。", "合約初審時間節省 60%，一線 Helpdesk 常見問題自動解決率達 45%。")
    ]

    for r_idx, r_data in enumerate(p12_rows, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p12.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=70, bottom=70, left=90, right=90)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8)
            r.font.color.rgb = RGB_DARK

    add_callout(doc,
        "光寶推動 AI 守則：\n"
        "1. 嚴禁為了做 AI 而做 AI：無明確量化指標之題目一律駁回；\n"
        "2. 嚴守敏感資料邊界：所有涉及機密設計圖面與顧客專利之數據，一律跑在私有化或 Air-Gapped 隔離模型上；\n"
        "3. 崇尚小步快跑：2 週看原型、4 週測實效、8 週算損益。",
        title="Departmental AI 推動三大鐵律"
    )

    doc.add_page_break()

    print("Building Page 13: Scope 6 - C-Level Reporting & Value Realization...")
    # =========================================================================
    # PAGE 13: 工作內容 6：定期向董事會、CEO 與事業單位主管報告成效
    # =========================================================================
    add_header_banner(doc, 13, "工作內容 6：向高階主管定期報告成效與投資回報", "WORK SCOPE 6", "定期向高階主管與事業單位主管報告成效 ｜ 對齊 HowardLiao/RSI ＆ 4163")

    add_callout(doc,
        "在信源全球 (RSI) 專案中，本人建立 CEO Balanced Scorecard、Run/Grow/Transform 預算表與一頁式決策審核表；在鐿鈦 (4163) 建立「四大立竿見影 Quick Win 指南」，首波 1 週內交出量化成果報告，建立跨部門信心。",
        title="高階治理實績：用 C-Level 懂的語言溝通"
    )

    p_p13_body = doc.add_paragraph()
    p_p13_body.paragraph_format.space_before = Pt(4)
    p_p13_body.paragraph_format.space_after = Pt(4)
    r_p13_b = p_p13_body.add_run(
        "高階主管的時間極其寶貴，最忌諱聽技術人員長篇大論演算法參數。\n"
        "本人為光寶董事會、李逢堉資訊長與事業部主管設計三層級透明報告架構："
    )
    r_p13_b.font.name = "STHeiti Light"
    r_p13_b.font.size = Pt(9.5)
    r_p13_b.font.color.rgb = RGB_DARK

    tbl_p13 = doc.add_table(rows=4, cols=3)
    tbl_p13.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p13.autofit = False
    tbl_p13.columns[0].width = Inches(1.8)
    tbl_p13.columns[1].width = Inches(2.7)
    tbl_p13.columns[2].width = Inches(2.7)

    headers_p13 = ["報告層級與週期", "核心呈報內容與關鍵視圖", "決策價值與管理輸出"]
    for i, h in enumerate(headers_p13):
        c = tbl_p13.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=70, bottom=70, left=90, right=90)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY

    p13_rows = [
        ("月度戰情報告\n(Monthly Ops Review)", "向李逢堉資訊長呈報各 BU Token 成本效益排行榜、API 響應延遲與 Failover 統計、產線異常警報解決率。", "即時優化運算資源配置，抓出算力異常消耗之部門，即時調整 Smart Routing 分流規則。"),
        ("季度經管會審查\n(Quarterly BOD/BU)", "向董事長與事業部總經理呈報 S/4HANA 整合進度、替代料庫存去化金額、工單準時交付率提升指標。", "以財務 EBITDA 衝擊與 ROI 說話，客觀評估各事業部 AI 投資回報率，動態調整下季預算。"),
        ("年度 IT 投資總盤點\n(Annual Capital Plan)", "Run / Grow / Transform 三向預算結構分析、雲端與硬體 TCO 總成本對照、技術債清理清冊。", "確保每一分 IT 資本支出 (CAPEX) 與營運費用 (OPEX) 均精確契合光寶中長期策略願景。")
    ]

    for r_idx, r_data in enumerate(p13_rows, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p13.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=70, bottom=70, left=90, right=90)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8)
            r.font.color.rgb = RGB_DARK

    add_callout(doc,
        "四大立竿見影 Quick Win 指南（到任 1 週內見量化成果）：\n"
        "• 場景 1：財務傳票與採購單 OCR 自動對齊 S/4HANA，憑證處理工時直接降低 75%；\n"
        "• 場景 2：光寶智慧規章與技術手冊 KM 助理，首次諮詢解決率提高 40%，100% 來源引用；\n"
        "• 場景 3：採購原物料報價異常自動標註與智慧比價雙重審批；\n"
        "• 場景 4：IT Helpdesk 一線常見問題自動導航與知識推薦，解放技術工程師時間。",
        title="Quick Wins：建立組織信心的第一步"
    )

    doc.add_page_break()

    print("Building Page 14: Cybersecurity & Compliance Safeguards...")
    # =========================================================================
    # PAGE 14: 資安底線與 AI 合規治理：ISO 42001 ＆ ISO 27001
    # =========================================================================
    add_header_banner(doc, 14, "資安底線與 AI 合規治理：ISO 42001 ＆ ISO 27001", "CYBER & GOVERNANCE", "資安是系統整合與 AI 的底線 ｜ 對齊 HowardLiao/6446 ＆ Howard_CISO")

    add_callout(doc,
        "系統串得越多、AI 用得越廣，資料外流、勒索病毒與模型被投毒的風險就越高。\n"
        "本人具備 ISO/IEC 27001 主導稽核員 (Lead Auditor) 國際資格，深入實踐 ISO/IEC 42001 人工智慧管理系統標準與金管會 GenAI 核心指引，堅持資安絕非業務絆腳石，而是企業出海擴張的最高防禦網。",
        title="資安合規權威背書：CISO 格局的守門員"
    )

    p_p14_body = doc.add_paragraph()
    p_p14_body.paragraph_format.space_before = Pt(4)
    p_p14_body.paragraph_format.space_after = Pt(4)
    r_p14_b = p_p14_body.add_run(
        "光寶服務全球一線雲端大廠與車用頂級客戶，對商業秘密與智財保護有著極高要求。本人規劃四大不可逾越之合規防線："
    )
    r_p14_b.font.name = "STHeiti Light"
    r_p14_b.font.size = Pt(9.5)
    r_p14_b.font.color.rgb = RGB_DARK

    tbl_p14 = doc.add_table(rows=5, cols=3)
    tbl_p14.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p14.autofit = False
    tbl_p14.columns[0].width = Inches(1.8)
    tbl_p14.columns[1].width = Inches(2.7)
    tbl_p14.columns[2].width = Inches(2.7)

    headers_p14 = ["資安合規防禦層", "潛在威脅與法遵要求", "光寶次世代落地工程對策"]
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
        ("工廠網絡分段隔離\n(OT Air-Gapping)", "勒索軟體透過辦公網絡橫向感染製造現場，造成 112 座工廠停工災難。", "實施 Purdue 模型實體與邏輯分段。機台 HMI 與生產資料庫置於受保護隔離區，AI 邊緣推理節點單向資料傳輸。"),
        ("核心圖面與專利防護\n(IP Loss Prevention)", "員工將未發布之電源機構設計圖或客戶規格丟入公有雲大模型，導致營業秘密外洩。", "部署本地私有化 LLM 與資料防外洩 (DLP) 網關，敏感欄位自動遮蔽，核心圖面絕對不出廠。"),
        ("不可竄改安全備份\n(Immutable Backup)", "勒索病毒加密主機與線上備份檔，導致企業無法復原生產資料。", "落實 3-2-1-1-0 備份架構，配置離線與不可竄改 (WORM) 存儲，每季強制實施非計畫停機復原演練。"),
        ("AI 倫理與可解釋性\n(Explainability & Audit)", "AI 替代料推薦或排程演算法產生偏差，現場人員盲目信任導致重大批量退貨。", "遵循 ISO 42001 標準，AI 決策必須具備特徵權重解釋與人類在環 (Human-in-the-Loop) 二次審批機制。")
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

    p_p14_bot = doc.add_paragraph()
    p_p14_bot.paragraph_format.space_before = Pt(8)
    p_p14_bot.paragraph_format.space_after = Pt(0)
    r_p14_bt = p_p14_bot.add_run("資安承諾：以 ISO 27001 主導稽核員標準把關，確保光寶 AI 平台在享受技術紅利時，資安風險始終為零。")
    r_p14_bt.font.name = "STHeiti Medium"
    r_p14_bt.font.size = Pt(9.5)
    r_p14_bt.font.color.rgb = RGB_PRIMARY

    doc.add_page_break()

    print("Building Page 15: Qualifications & Competencies Audit...")
    # =========================================================================
    # PAGE 15: 光寶科技面試要求自我審查核定總表
    # =========================================================================
    add_header_banner(doc, 15, "光寶科技面試要求自我審查核定總表", "QUALIFICATIONS AUDIT", "官方職缺所有必要條件與加分條件，逐條匹配並附客觀可查證出處")

    p_p15_body = doc.add_paragraph()
    p_p15_body.paragraph_format.space_before = Pt(0)
    p_p15_body.paragraph_format.space_after = Pt(4)
    r_p15_b = p_p15_body.add_run(
        "對齊 Notion 職缺頁面《(NEW!) IT AI 平台負責人》之所有技術職能、管理職能與任職門檻："
    )
    r_p15_b.font.name = "STHeiti Light"
    r_p15_b.font.size = Pt(9.5)
    r_p15_b.font.color.rgb = RGB_DARK

    tbl_p15 = doc.add_table(rows=8, cols=4)
    tbl_p15.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p15.autofit = False
    tbl_p15.columns[0].width = Inches(1.3)
    tbl_p15.columns[1].width = Inches(1.8)
    tbl_p15.columns[2].width = Inches(2.9)
    tbl_p15.columns[3].width = Inches(1.2)

    headers_p15 = ["條件類別", "光寶官方條件", "Howard Liao Ph.D. 具體驗證依據", "核定結果"]
    for i, h in enumerate(headers_p15):
        c = tbl_p15.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=60, bottom=60, left=80, right=80)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY

    p15_rows = [
        ("必要條件 1", "學歷、產業背景不限", "資訊管理博士 (Ph.D.) ＆ 國立中興大學 資訊科學碩士。具備電腦科學與企業管理雙重底蘊。", "100% 符合"),
        ("必要條件 2", "10 年以上帶領 AI／資料團隊經驗", "27+ 年 IT & 工程歷練、20+ 年 C-Level 管理經驗，經歷軟體、跨國製造與雲端多次典範轉移。", "遠超 10 年"),
        ("必要條件 3", "主導 AI 平台或產品上線並交出可量化成果", "4 大 C-Level 商業衝擊量化成果：$10M+ 資本治理、100% Zero Outage、-30% TCO、+100% 部署速度。", "量化查核通過"),
        ("加分條件 1", "從零建立 AI／資料平台與團隊經驗", "《組織從零到一降維突圍實戰報告》（journey）：完整記錄突破老臣防衛、組建 35+ 人平台梯隊之實戰。", "實戰驗證具備"),
        ("加分條件 2", "具備與 C Level 或 高階主管溝通能力", "長期向董事會、CEO、審計委員會、COO 呈報策略與投資規劃，擅長翻譯演算法為 EBITDA 商業價值。", "完全具備"),
        ("加分條件 3", "具備 CIO 或 IT 部門主管經驗", "上市櫃數位娛樂集團 (6542.TWO) CIO/CISO/CDAIO、鴻海中央資訊技術處長（企業架構與數位轉型）。", "完整高管履歷"),
        ("加分條件 4", "國內大型企業數位轉型專案推動經驗", "泓晏科技（跨國電子製造）、信源全球（跨國成衣製造）、鐿鈦科技（精密醫材）、大江生醫（生醫製造）。", "跨產業實績")
    ]

    for r_idx, r_data in enumerate(p15_rows, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p15.cell(r_idx, c_idx)
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

    add_callout(doc,
        "面試流程第一關與第二關承諾：\n"
        "• 第一關（CIO 李逢堉、技術顧問、人資長）：現場可就 PLM-SAP-MES 串流技術細節、Debezium CDC 拓撲、Kafka 吞吐量與組織化解防衛心理進行深層技術與管理答辯；\n"
        "• 第二關（董事長）：現場可就企業資本回報率 (ROI)、全球布局風險控制與千億製造網絡競爭優勢進行宏觀商業戰略對焦。",
        title="對位面試關卡之自我期許"
    )

    doc.add_page_break()

    print("Building Page 16: Howard Liao Ph.D. Profile & Track Record...")
    # =========================================================================
    # PAGE 16: 個人履歷與學術底蘊 (Howard Liao Ph.D.)
    # =========================================================================
    add_header_banner(doc, 16, "個人個人簡歷與學術底蘊 (Howard Liao Ph.D.)", "CANDIDATE PROFILE", "資訊管理博士 ｜ 國立中興大學 資訊科學碩士 ｜ 27+ 年工程與管理淬鍊")

    # Table: Portrait + Key Profile
    tbl_prof = doc.add_table(rows=1, cols=2)
    tbl_prof.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_prof.autofit = False
    tbl_prof.columns[0].width = Inches(2.2)
    tbl_prof.columns[1].width = Inches(5.0)

    c_img = tbl_prof.cell(0, 0)
    c_txt = tbl_prof.cell(0, 1)
    set_cell_background(c_img, HEX_HEADER_BG)
    set_cell_background(c_txt, HEX_SURFACE)
    set_cell_margins(c_img, top=100, bottom=100, left=100, right=100)
    set_cell_margins(c_txt, top=100, bottom=100, left=120, right=100)

    # Insert Portrait
    portrait_path = os.path.join(ASSETS_DIR, 'howard_portrait.jpg')
    if os.path.exists(portrait_path):
        p_port = c_img.paragraphs[0]
        p_port.alignment = WD_ALIGN_PARAGRAPH.CENTER
        c_img.paragraphs[0].paragraph_format.space_before = Pt(0)
        c_img.paragraphs[0].paragraph_format.space_after = Pt(4)
        run_img = p_port.add_run()
        run_img.add_picture(portrait_path, width=Inches(1.8))
        
        p_lbl = c_img.add_paragraph()
        p_lbl.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_lbl.paragraph_format.space_before = Pt(2)
        p_lbl.paragraph_format.space_after = Pt(0)
        r_lbl = p_lbl.add_run("Howard Liao Ph.D.\n廖倫豪 博士")
        r_lbl.font.name = "STHeiti Medium"
        r_lbl.font.size = Pt(8.5)
        r_lbl.font.bold = True
        r_lbl.font.color.rgb = RGB_DARK

    p_txt = c_txt.paragraphs[0]
    p_txt.paragraph_format.space_before = Pt(0)
    p_txt.paragraph_format.space_after = Pt(2)
    r_pt = p_txt.add_run("【核心學歷與國際認證】\n")
    r_pt.font.name = "STHeiti Medium"
    r_pt.font.size = Pt(9.5)
    r_pt.font.bold = True
    r_pt.font.color.rgb = RGB_PRIMARY

    r_pb = p_txt.add_run(
        "• 資訊管理博士 (Ph.D. in Information Management)\n"
        "• 國立中興大學 資訊科學碩士 (National Chung Hsing Univ. · M.S. in CS)\n"
        "• 出生年份：民國 62 年次 (1973 年生)\n"
        "• 國際證照：ISO/IEC 27001 Lead Auditor 主導稽核員\n"
        "• 治理標準：ISO/IEC 42001 人工智慧管理系統 ＆ PMP 專案管理師規範\n"
        "• 聯絡方式：Email: liao.howard@gmail.com  ｜  LINE ID: howardliao\n"
        "• 線上作品集：https://howardliao.github.io/portfolio/"
    )
    r_pb.font.name = "STHeiti Light"
    r_pb.font.size = Pt(8.5)
    r_pb.font.color.rgb = RGB_DARK

    p_spacer_16 = doc.add_paragraph()
    p_spacer_16.paragraph_format.space_before = Pt(4)
    p_spacer_16.paragraph_format.space_after = Pt(4)

    tbl_roles = doc.add_table(rows=5, cols=3)
    tbl_roles.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_roles.autofit = False
    tbl_roles.columns[0].width = Inches(1.8)
    tbl_roles.columns[1].width = Inches(2.2)
    tbl_roles.columns[2].width = Inches(3.2)

    headers_roles = ["服務企業 / 集團", "擔任職銜", "核心職能與歷史治理戰功"]
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
        ("鴻海科技集團\n(Foxconn)", "中央資訊 技術處長", "主責大型企業架構決策、SWOT 差距分析、商業戰略轉譯與集團數位轉型推動。奠定超大型製造網絡與跨國供應鏈頂層設計能力。"),
        ("上市櫃數位娛樂集團\n(6542.TWO)", "資訊長 CIO / CISO / CDAIO", "掌管集團技術戰略、跨國多雲架構、高併發交易防護與 ISO 27001 資安認證；創下 100% Zero Outage 紀錄，降低 30% 基礎設施持有成本。"),
        ("盛欣網絡科技\n(Shenxin Network)", "技術副總\nVP of Technology", "主導研發團隊敏捷轉型，從零建立 Agentic AI 落地體系、建立產品 PO 制度、導入內控交易循環與 ISO 42001 人工智慧治理體系。"),
        ("製造與生醫產業顧問\n(RSI / 4163 / 8436)", "企業資訊架構執行負責人\nLead Architect & C-Level Advisor", "主導信源全球 (RSI) 2027 IT 策略藍圖、鐿鈦科技 (4163) PLM/SAP/MES 整合藍圖、大江生醫 (8436) 企業資訊策略與 32 全架構視圖設計。")
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

    print("Building Page 17: Case Studies...")
    # =========================================================================
    # PAGE 17: 代表性專案深度復盤：跨國電子製造與精密製造實績
    # =========================================================================
    add_header_banner(doc, 17, "代表性專案深度復盤：跨國電子製造與精密製造實績", "CASE STUDIES", "跨國電子製造（泓晏）、高可用零停機（隆中 6542）與全架構貫通（8436 / 4163）")

    cases = [
        ("案例一：泓晏科技 —— 跨國電子製造數據整合實務（對齊光寶 EMS 與電源工廠場景）",
         "【專案背景】泓晏科技為跨國電子零組件製造商，產線面臨 SMT 拋料率偏高、跨廠備料資訊斷鏈、以及人工抄表謄打導致數據延遲 48 小時的挑戰。\n"
         "【架構對策】在工廠端部署邊緣閘道器直接採集貼片機與 AOI 檢驗機數據，建立近即時 (Near-Real-Time) 品質預警模型；在總部端打通 ERP 與生產排程，消除人工作業斷點。\n"
         "【量化成果】拋料異常通報時間從 24 小時縮短至 5 分鐘，跨廠庫存周轉率提高 18%，為光寶 112 座工廠數據互通提供了成熟的落地範本。"),
        
        ("案例二：隆中網絡 (6542.TWO) —— 100% Zero Outage 韌性治理與 -30% TCO",
         "【專案背景】上市櫃高併發線上娛樂與數位平台，每秒承受數萬筆併發交易，任何非計畫性停機均直接導致鉅額營收損失與監管懲處。\n"
         "【架構對策】導入多雲主動容災 (Multi-Cloud Active-Active)、不可竄改防勒索備份演練與自動化流量切換，並實施 FinOps 雲端運算資源優化，去除冗餘架構雜訊。\n"
         "【量化成果】任期內創下連續多年 100% Zero Outage 營運紀錄，通過 ISO 27001 實質認證，並使集團雲端基礎設施 TCO 總成本降低 30%。"),
         
        ("案例三：大江生醫 (8436) ＆ 鐿鈦科技 (4163) —— TOGAF 32 全架構與 PLM-SAP-MES 數據流",
         "【專案背景】生醫研發製造與精密醫材領域對數據完整性 (ALCOA+) 與法規追溯 (FDA 21 CFR Part 11) 有著全球最嚴苛的要求。\n"
         "【架構對策】以 TOGAF ADM 框架規劃 32 全架構視圖，設計 Kafka + Debezium CDC 雙環數據總線，使研發設計變更自動同步現場工單，杜絕用錯料號風險。\n"
         "【量化成果】研發至量產交付週期縮短 35%，全廠達成 100% 數位化批次生產記錄 (eBPR)，稽核追溯工時減少 80%。")
    ]

    for title, desc in cases:
        add_callout(doc, desc, title=title)

    doc.add_page_break()

    print("Building Page 18: 180-Day Onboarding Roadmap...")
    # =========================================================================
    # PAGE 18: 到任光寶 180 天落地行動計畫：對齊 2027/01/04 S/4HANA 切換
    # =========================================================================
    add_header_banner(doc, 18, "到任光寶 180 天落地行動計畫：對齊 2027/01/04 S/4HANA 切換", "ONBOARDING ROADMAP", "倒排工期、步步為營，在不干擾 ERP 核心升級的前提下穩健推進 AI Stack")

    # Insert Roadmap Diagram
    img_rd_path = os.path.join(IMG_DIR, 'diagram_roadmap.png')
    if os.path.exists(img_rd_path):
        p_img = doc.add_paragraph()
        p_img.paragraph_format.space_before = Pt(0)
        p_img.paragraph_format.space_after = Pt(4)
        doc.add_picture(img_rd_path, width=Inches(7.2))

    tbl_p18 = doc.add_table(rows=5, cols=3)
    tbl_p18.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p18.autofit = False
    tbl_p18.columns[0].width = Inches(1.5)
    tbl_p18.columns[1].width = Inches(2.8)
    tbl_p18.columns[2].width = Inches(2.9)

    headers_p18 = ["時間里程碑", "階段目標與主要推進工作", "關鍵交付物 (Deliverables)"]
    for i, h in enumerate(headers_p18):
        c = tbl_p18.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=65, bottom=65, left=90, right=90)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY

    p18_rows = [
        ("第 1 ~ 30 天\n(Listen & Audit)", "• 拜訪資訊長李逢堉、IBM 專案主管、重點事業群總經理與海外示範廠長；\n• 與 15 位核心 IT 與資料工程師 1-on-1；\n• 盤查 S/4HANA 升級介接端點與 112 座工廠 MES/PLM 孤島現況。", "交付 1：《光寶科技 AI 現況盤點與痛點診斷報告》\n交付 2：《資深同仁優勢地圖與 9 大路線初評表》"),
        ("第 31 ~ 60 天\n(Blueprint & PO)", "• 發布光寶次世代 AI 平台拓撲藍圖 (TOGAF BDAT)；\n• 選定首波立竿見影場景（替代料推薦、齊套料預警）；\n• 成立第一期「平台試驗沙盒組」，招募首批業務 PO 同仁。", "交付 3：《光寶 AI 平台架構藍圖與技術規範》\n交付 4：《首波 PoC 規格書與業務 ROI 測算表》"),
        ("第 61 ~ 90 天\n(Pilot & Bus)", "• 部署雙環 Data Bus (Kafka + Debezium CDC + EMQX MQTT)；\n• 於海外示範廠完成 MES 與 AI 模型即時推理串接；\n• 首波 PoC 上線，驗證替代料推薦準確度與生管工時節省。", "交付 5：《示範廠 AI 推理上線實測報告》\n交付 6：《首波 1 週可量化成效報告（財務憑證 OCR 工時 -75%）》"),
        ("第 91 ~ 180 天\n(Scale & Cutover)", "• 對齊 2027/01/04 全球 S/4HANA 上線，正式掛載 AI 網關中樞；\n• 啟動製造執行系統 (MES) 工單全自動智慧派工閉環；\n• 建立全集團 AI Token 計費分攤與持續訓練機制。", "交付 7：《光寶可重複使用 AI 平台投產白皮書》\n交付 8：《2027 年度 AI 投資回報與持續優化計畫》")
    ]

    for r_idx, r_data in enumerate(p18_rows, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p18.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=65, bottom=65, left=90, right=90)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8)
            r.font.color.rgb = RGB_DARK

    doc.add_page_break()

    print("Building Page 19: Enterprise Risk Register & Mitigation...")
    # =========================================================================
    # PAGE 19: 關鍵風險登錄表與雙軌避震對策 (Enterprise Risk Register)
    # =========================================================================
    add_header_banner(doc, 19, "關鍵風險登錄表與雙軌避震對策", "RISK REGISTER", "針對光寶 S/4HANA 升級與 AI 導入可能遭遇之 5 大風險提供結構化解法")

    # Insert Risk Diagram
    img_rk_path = os.path.join(IMG_DIR, 'diagram_risk.png')
    if os.path.exists(img_rk_path):
        p_img = doc.add_paragraph()
        p_img.paragraph_format.space_before = Pt(0)
        p_img.paragraph_format.space_after = Pt(4)
        doc.add_picture(img_rk_path, width=Inches(7.2))

    tbl_p19 = doc.add_table(rows=6, cols=4)
    tbl_p19.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p19.autofit = False
    tbl_p19.columns[0].width = Inches(1.3)
    tbl_p19.columns[1].width = Inches(1.8)
    tbl_p19.columns[2].width = Inches(2.6)
    tbl_p19.columns[3].width = Inches(1.5)

    headers_p19 = ["風險識別編號", "風險情境與潛在衝擊", "雙軌緩解對策與工程控制", "責任人 / 監控"]
    for i, h in enumerate(headers_p19):
        c = tbl_p19.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=65, bottom=65, left=80, right=80)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY

    p19_rows = [
        ("RISK 01\n(S/4HANA 延誤)", "ERP 升級進度緊張，若 AI 整合牽涉核心資料庫修改，可能影響 2027/01/04 切換窗口。", "恪守 SAP Clean Core 原則。將 AI 運算完全外掛於微服務層，以 Kafka CDC 非同步抽取，零衝擊核心。", "AI 平台負責人\nS/4HANA PMO"),
        ("RISK 02\n(組織山頭防禦)", "資深開國同仁擔心地位受損，暗中消極抵抗，導致新平台無人調用。", "實施「戰略絕緣層」與 ORID 工作坊，確立「承認能力、同意問題、建立公平規則」，授權潛力星。", "AI 平台負責人\nHR 部門主管"),
        ("RISK 03\n(模型幻覺錯料)", "LLM 推薦非合格之替代料，導致工程事故或大批量退貨賠償。", "強式 Agentic RAG 整合 PLM 參數庫，實施規格二次強校驗，強制附帶引用來源，保留專家最終審核權。", "AI 演算法主管\nPLM 負責人"),
        ("RISK 04\n(工廠網路中斷)", "海外工廠（如越南、泰國）聯外網絡不穩定，雲端 AI 斷線造成產線停擺。", "落實 Purdue 模型 Air-Gapped 實體分段，邊緣節點具備離線推理能耐與本地緩衝降級模式。", "OT 網路主管\n各廠總廠長"),
        ("RISK 05\n(Token 成本失控)", "各單位任意呼叫旗艦大模型，導致雲端算力與 API 授權費用幾何級數暴增。", "HowardRoute 實施 Smart Routing 自動降本分流演算法，嚴格設定各事業部每月調用配額與超額警報。", "FinOps 架構師\n財務審計專員")
    ]

    for r_idx, r_data in enumerate(p19_rows, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p19.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=65, bottom=65, left=80, right=80)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8)
            r.font.color.rgb = RGB_DARK

    doc.add_page_break()

    print("Building Page 20: Conclusion & Digital Artifacts Index...")
    # =========================================================================
    # PAGE 20: 結語與數位資源全景索引 (Conclusion & Digital Artifacts)
    # =========================================================================
    add_header_banner(doc, 20, "結語與數位資源全景索引", "CONCLUSION & INDEX", "戰時領導力、功成不必在我、全力輔佐光寶千億製造網絡")

    add_callout(doc,
        "「在非成熟治理土壤中，當老闆深陷焦慮、中間層退化為傳話筒、開國老臣山頭盤據時，唯一的生還之道：硬核商業對賭、極簡防護工具、與戰略絕緣層。自己專注於骨架搭建，成就團隊，功成不必在我。」—— Howard Liao Ph.D.\n"
        "光寶科技正邁向綠色資料中心、永續運輸與高效能基礎設施的全球領導者。本人帶著 27+ 年工程熱忱與 20+ 年 C-Level 實戰歷練，隨時準備就位，全力輔佐董事長、李逢堉資訊長與全體光寶同仁！",
        title="候選人誓言：戰時管理者的格局與擔當"
    )

    p_p20_body = doc.add_paragraph()
    p_p20_body.paragraph_format.space_before = Pt(4)
    p_p20_body.paragraph_format.space_after = Pt(2)
    r_p20_b = p_p20_body.add_run("【HowardLiao GitHub 全景數位資產與專案門戶索引】")
    r_p20_b.font.name = "STHeiti Medium"
    r_p20_b.font.size = Pt(9.5)
    r_p20_b.font.bold = True
    r_p20_b.font.color.rgb = RGB_PRIMARY

    tbl_p20 = doc.add_table(rows=8, cols=3)
    tbl_p20.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p20.autofit = False
    tbl_p20.columns[0].width = Inches(2.2)
    tbl_p20.columns[1].width = Inches(2.4)
    tbl_p20.columns[2].width = Inches(2.6)

    headers_p20 = ["專案倉庫 (Repository)", "核心架構資產與文檔內容", "線上審閱門戶 (Live Portal)"]
    for i, h in enumerate(headers_p20):
        c = tbl_p20.cell(0, i)
        set_cell_background(c, HEX_HEADER_BG)
        set_cell_margins(c, top=55, bottom=55, left=80, right=80)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "STHeiti Medium"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGB_PRIMARY

    p20_rows = [
        ("HowardLiao/2301\n(光寶科技專案)", "本報告全量工程原始碼、RWD/PWA 線上高管門戶、架構圖資。", "https://howardliao.github.io/2301/"),
        ("HowardLiao/8436\n(大江生醫架構)", "HowardRoute 模型網關、HowardAGent、TOGAF 32 全架構圖資。", "https://howardliao.github.io/8436/"),
        ("HowardLiao/4163\n(鐿鈦科技整合)", "把 PLM、SAP、MES 串成一條數據流；Departmental AI 方案。", "https://howardliao.github.io/4163/"),
        ("HowardLiao/RSI\n(信源全球 2027)", "2027 IT 策略白皮書、18 頁 CEO 簡報、AI Use Case & ROI 矩陣。", "https://howardliao.github.io/RSI/"),
        ("HowardLiao/journey\n(組織突圍報告)", "組織從零到一降維突圍、ORID 焦點法化解老臣防衛、9 大技術階梯。", "https://howardliao.github.io/journey/"),
        ("HowardLiao/6446\n(藥華醫藥治理)", "ISO 42001 人工智慧治理體系、CIO/CTO/CISO 權責章程與 KPI。", "https://howardliao.github.io/6446/"),
        ("HowardLiao/portfolio\n(高管主作品集)", "Howard Liao Ph.D. 全球數位作品集，4 大 C-Level 商業衝擊量化指標。", "https://howardliao.github.io/portfolio/")
    ]

    for r_idx, r_data in enumerate(p20_rows, start=1):
        for c_idx, val in enumerate(r_data):
            c = tbl_p20.cell(r_idx, c_idx)
            set_cell_background(c, HEX_SURFACE if r_idx % 2 == 1 else "#FFFFFF")
            set_cell_margins(c, top=55, bottom=55, left=80, right=80)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "STHeiti Light"
            r.font.size = Pt(8)
            r.font.color.rgb = RGB_DARK

    p_sign = doc.add_paragraph()
    p_sign.paragraph_format.space_before = Pt(12)
    p_sign.paragraph_format.space_after = Pt(0)
    r_s = p_sign.add_run("呈報人簽署： Howard Liao Ph.D. (廖倫豪 博士) ｜ 日期：2026 年 11 月 05 日 ｜ 地點：台北市內湖區光寶科技總部面試呈報")
    r_s.font.name = "STHeiti Medium"
    r_s.font.size = Pt(8.5)
    r_s.font.bold = True
    r_s.font.color.rgb = RGB_PRIMARY

    # Save document
    doc.save(OUTPUT_DOCX)
    print(f"Successfully generated 20-page dossier at: {OUTPUT_DOCX}")

if __name__ == '__main__':
    build_dossier()
