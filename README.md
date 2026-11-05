# 光寶科技 (2301.TW) 全球 AI 策略、資料產品與製造中樞演進藍圖
## LITE-ON Global Enterprise AI Strategy, Data Products & Smart Manufacturing Hub

> **報告人**：**Howard Liao Ph.D. (廖倫豪 博士)**  
> **職位定位**：全球 AI 策略與平台演進總監 / VP of AI 候選人 ｜ Forward-Deployed AI Architect & Player-Coach C-Level  
> **呈報對象**：光寶科技 執行長 ｜ 資訊長 李逢堉 ｜ 事業單位主管 ｜ 董事會經管會  
> **線上即時高管門戶 (Live Online Portal)**：[https://howardliao.github.io/2301/](https://howardliao.github.io/2301/)  
> **適用標準與框架**：TOGAF 10 ADM (32 Views) / ISO/IEC 42001 (AI Governance) / ISO/IEC 27001:2022 / SAP S/4HANA Clean Core / FDA ALCOA+

---

## 📌 執行摘要：深挖「問題背後的問題」
依據《商業周刊》最新深訪與光寶科技官方科技藍圖，光寶正處於數位轉型最關鍵的骨幹交接期：
1. **全球製造與組織規模**：旗下 86 間子公司、112 座製造工廠、分佈全球 20 幾個跨國據點。
2. **骨幹核心升級大戰**：資訊長李逢堉率領團隊將全球 ERP 從 SAP ECC 全面升級至 S/4HANA（含 16 項新功能與 27 項流程優化），目標 **2027 年 1 月 4 日同步切換**，停機時間嚴格控制於 72 小時以內。
3. **下一個里程碑「讓 ERP 更 AI」**：S/4HANA 上線只是開端，下一階段核心是**「能預測、能建議、在製造端主動判斷的系統」**，關鍵痛點在於 **MES 與 ERP 緊密串聯、替代料選用、齊套料規劃、工單智慧排程**；管理心法則是**「深挖問題背後的問題」**。

本專案將 Howard Liao Ph.D. 歷經 27+ 年工程與 20+ 年 C-Level 治理所沉澱之技術資產，全面映射至光寶科技之戰略需求。

---

## 🏛️ 核心架構矩陣：光寶互補式 AI Stack (Complementary to SAP & MES)

```
[業務與決策端]   SAP S/4HANA (86 間子公司財務/採購/供應鏈) ── MES 工單現場 (112 座工廠)
                                    ▲                               ▲
                                    │ (REST / gRPC / 双向回填)      │ (MQTT / OPC-UA)
                                    ▼                               ▼
[AI 決策大腦]     HowardRoute 模型網關 (250+ 模型, Smart Routing, 0% Markup, 省 20~40% Token)
                  HowardAGent 任務編排中樞 (Agentic RAG 95% 準確率, 傳票 OCR, 規格問答)
                  HowardPro 工業預測調機大腦 (AutoML 參數推薦, 替代料比對, 齊套料預警)
                                    ▲
                                    │ (毫秒級特徵提取)
[雙環 Data Bus]   IT 骨幹串流：Apache Kafka
                  SAP 即時異動捕捉：Debezium (SAP CDC, 零 DB 查詢負載)
                  OT 邊緣物聯網：EMQX MQTT Broker
                                    ▲
[OT 現場隔離]     SMT 產線 ｜ AOI 檢測 ｜ CNC 加工 ｜ RFID 追溯 (Air-Gapped 工廠網路分段)
```

---

## 📊 光寶科技技術與管理職能 ＆ GitHub 實體工程逐條對照

| 光寶科技職能要求 | 核心實踐與解決方案 | GitHub 關聯倉庫與線上手冊 |
| :--- | :--- | :--- |
| **【定位】把 AI 從單一應用推進到產品與平台，帶來看得見的經濟效益** | • **HowardRoute**：多模型調度與網關，250+ 款模型集中管控，動態分流節省 20~40% Token 營運成本。<br>• **HowardAGent**：企業級 Agentic RAG（95% 準確率）、多模態 OCR。<br>• **HowardPro**：工業級 AutoML 虛擬量測與參數推薦。 | • [`HowardLiao/8436`](https://github.com/HowardLiao/8436)<br>• [8436 Live 戰情](https://howardliao.github.io/8436/) |
| **【工作 1】定義優先導入 AI 領域，規劃 AI 平台藍圖** | • **信源全球 (RSI) 2027 策略藍圖**：撰寫 18 頁 CEO 簡報與五大策略支柱，包含 AI Use Case & ROI 治理矩陣。<br>• **32 全架構視圖**：涵蓋 ADM Phase A~H 業務、數據、應用與技術架構。<br>• **跨 C-Level 訪談題庫**：深入訪談 COO、CFO、海外總廠長 30+ 題。 | • [`HowardLiao/RSI`](https://github.com/HowardLiao/RSI)<br>• [RSI Live 白皮書](https://howardliao.github.io/RSI/) |
| **【工作 2】零散應用做成可重複使用的資料產品與平台** | • 微服務化資料產品，以 Apache APISIX + Keycloak 統一阻斷影子 API 與越權攻擊。<br>• 建立集中式模型調度與 Token 成本度量分攤機制。<br>• 災備與 Agentic 自動化工作流。 | • [`HowardLiao/8436`](https://github.com/HowardLiao/8436)<br>• [`HowardLiao/Hermes-Backup`](https://github.com/HowardLiao/Hermes-Backup) |
| **【工作 3】建立和 SAP、PLM、MES 互補的 AI stack** | • **把 PLM、SAP、MES 串成一條數據流（4163 Scheme 1）**：PLM 設計變更（ECN）自動同步 SAP 與 MES，杜絕人工轉檔與用錯 BOM。<br>• **雙環 Data Bus**：Kafka + Debezium SAP CDC + EMQX OT MQTT。<br>• **直擊光寶製造痛點**：替代料智慧推薦、齊套料動態規劃、工單智慧排程。<br>• **跨國電子製造實績**：泓晏科技跨國電子製造數據整合。 | • [`HowardLiao/4163`](https://github.com/HowardLiao/4163)<br>• [4163 Live 專區](https://howardliao.github.io/4163/) |
| **【工作 4】組建 AI 組織與人才梯隊，帶領技術主管與工程師** | • **《組織從零到一降維突圍實戰報告》（journey）**：運用 ORID 焦點討論法化解 16~18 年開國老臣山頭防衛。<br>• **9 大技術發展路線（A~I）** 與人才九宮格，打破單點壟斷，授權潛力工程師扛起核心 Feature KPI。<br>• 設計 9~14 人 CISO/CIO/AI 編制與量化 KPI。 | • [`HowardLiao/journey`](https://github.com/HowardLiao/journey)<br>• [journey Live 門戶](https://howardliao.github.io/journey/)<br>• [`HowardLiao/6446`](https://github.com/HowardLiao/6446) |
| **【工作 5】推動業務主導的平台團隊與企業內部 PO 培養，帶動 AI 原生工作方式** | • **「三好一支援」工作坊**：全盤梳理業務真實需求。<br>• **5 大構面「指標字典」**：以「0.1% DAU 對賭打平團隊成本」訓練內部 PO 商業算盤思維。<br>• **Departmental AI 普及模式**：主管先學、資訊部先試、擴散四部（生產、品保、業務、管理）。 | • [`HowardLiao/journey`](https://github.com/HowardLiao/journey)<br>• [`HowardLiao/4163`](https://github.com/HowardLiao/4163) |
| **【工作 6】定期向高階主管與事業單位主管報告成效** | • **CEO Balanced Scorecard**：Run/Grow/Transform 三向預算情境分析與季度平準化路線圖。<br>• **四大立竿見影 Quick Win 指南**：1 週內交出量化成果報告（財務憑證 OCR 工時 -75%、智慧問答初次解決率 +40%）。 | • [`HowardLiao/RSI`](https://github.com/HowardLiao/RSI)<br>• [`HowardLiao/4163`](https://github.com/HowardLiao/4163) |

---

## 📈 條件審查核定（必要條件 ＆ 加分條件）

* **必要條件 1：學歷、產業背景不限** -> **100% 符合**：資訊管理博士 (Ph.D.) ＆ 國立中興大學 資訊科學碩士。
* **必要條件 2：10 年以上帶領 AI／資料團隊經驗** -> **遠超要求**：27+ 年 IT & 工程歷練，20+ 年高階主管（CIO / CISO / CDAIO / VP of Tech）。
* **必要條件 3：主導 AI 平台或產品上線並交出可量化成果** -> **量化查核通過**：4 大 C-Level 商業衝擊量化成果（**$10M+** 資本治理、**100% Zero Outage**、**-30% TCO**、**+100% 部署速度**）。
* **加分條件 1：從零建立 AI／資料平台與團隊經驗** -> **實戰具備**：`journey` 詳實記錄從 0 構建 35+ 人平台團隊、化解老臣防衛、落地閉環之全歷程。
* **加分條件 2：具備與 C Level 或 高階主管溝通能力** -> **完全具備**：長期呈報董事會、執行長、經管會與海外廠長，將演算法轉譯為 EBITDA 與 ROI。
* **加分條件 3：具備 CIO 或 IT 部門主管經驗** -> **完整資歷**：上市櫃娛樂科技集團 (6542.TWO) CIO/CISO/CDAIO、鴻海中央資訊技術處長（企業架構決策、SWOT差距分析、商業戰略轉譯、數位轉型計畫）。
* **加分條件 4：國內大型企業數位轉型專案推動經驗** -> **跨產業實證**：泓晏科技（跨國電子製造）、信源全球（跨國高階成衣製造）、鐿鈦科技（精密醫材製造）、大江生醫（生醫研發製造）。

---

## ⏱️ 到任光寶 180 天落地行動計畫（對齊 2027/01/04 S/4HANA 切換）

* **30 Days（傾聽訪談與深度盤點）**：訪談李逢堉資訊長、事業部主管與海外工廠廠長；盤點 S/4HANA 介接點與 112 座工廠 MES/PLM 數據現況。
* **60 Days（藍圖確定與試點挑選）**：發布光寶次世代 AI 平台拓撲藍圖；選定首波替代料智慧推薦與齊套料預警場景；啟動內部業務 PO 培訓營。
* **90 Days（示範廠貫通與 POC 驗收）**：部署雙環 Data Bus（Kafka + Debezium CDC + EMQX MQTT）；示範廠 MES 即時推理上線；繳出首批 1 週量化效益成果。
* **180 Days（S/4HANA 閉環與規模複製）**：對齊 2027/01/04 全球 S/4HANA 切換，AI 網關正式掛載，工單全自動智慧派工閉環投產。

---

## 📞 聯絡與對接方式
* **Author Attribution**：Howard Liao Ph.D. (廖倫豪 博士)
* **Email**：[liao.howard@gmail.com](mailto:liao.howard@gmail.com)
* **LINE ID**：`howardliao`
* **GitHub Profile**：[https://github.com/HowardLiao](https://github.com/HowardLiao)
* **Executive Portfolio**：[https://howardliao.github.io/portfolio/](https://howardliao.github.io/portfolio/)
