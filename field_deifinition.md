# Field Definitions

本文件說明資料庫中各csv檔各欄位定義、格式與應用說明，供未來新增資料時參考與維持一致性。

## Vietnam
### Table: vn_policy_summary.csv

所有法規的note都會編寫在notion

| 欄位名稱 | 說明 | 格式/單位 | 範例 | 備註 |
|---------------|-------------------|----------|-----|-----|
|`policy_id`| 每一條政策的唯一識別碼 | string | VN_PDP8_2023 | 國家（兩字縮寫）_政策主軸_年份 |
| `policy_name `| 法規或政策的正式名稱 | string | PDP8 revised | 加入年份來區分版本 |
| `country` | 法規所屬國家 | string | Vietnam, Taiwan | 使用英文標準拼寫 |
| `release_year` | 政策發佈年份 | YYYY | 2023 | 如果不確定先以最早公開版本為準 |
| `effective_year` | 正式生效或執行年份 | YYYY | 2030 | 若是草案只會有release year，這邊可以略過|
| `policy_type` | 法規功能類別，根據其目的與性質分類 | enum (string) | Market-Defining, Mechanism-Launching | 詳見類別定義下方 |
| `legal_level` | 法規層級（如計劃、命令、草案、立法等）| string | National Plan, Ministerial Circular | 根據當地法律體制標示，越南法律體制請見下方 ｜
| `market_mechanism` |  採購機制類型 | string | Feed-in Tariff, Auction, PPA | 僅有採購相關政策需填寫，可留空 |
| `status` | 政策目前狀態 | enum | active, obsolete, draft | 可以擴充為suspended 等 |
| `related_parent_id` | 上層法規的ID(若本法為某政策的子法) | string/ null | VN_FIT_2017 | 若無則可空白 |
| `pursuant_to` | 本政策依據的所有法律條文 | 法規ID | VN_FIT_2017 | 若有多個條文，可用英文逗號分開 |
| `replaces_id` | 被此政策取代的舊政策ID(如果有) | string/ null | VN_FIT_2017 | 若無則可空白 |
| `is_amendment_of` | 是否為某法規的修正版本，指向原法 | string/ null | VN_FIT_2017 | 若無則可空白 |
| `re_target` | 政策中提及的再生能源目標 | text/ list (string) | 2030 RE30%, 2045 RE40% | 可留空，年份不限 |
| `brief_description` | 一句話摘要政策重點 | text | DPPA正式運行文件 | 簡單扼要就好 |
| `source`| 政策原文 | path | OneDrive/energydb/... | 無 |
| `last_reviewed` | 最近一次手動確認此法規狀態的日期 | YYYY-MM-DD | 2023-02-21 | 手動填入，表明最後一次查閱這條政策的時間點 ｜

#### `policy_type`分類定義

| 類別名稱 | 說明與範例 |
|---------|-----------|
| Market-Defining | 設定市場結構、角色與權責，如PDP8、台灣電業法 |
| Mechanism-Launching | 推出具體市場機制，像是FIT、標案規則 |
| Target-Setting | 訂定國家總目標，像是2050國家減碳目標 |
| Supportive | 配套支持政策，像是賦稅優惠、用地指引 |
| Procedural | 作業細則、程序性法規，像是契約流程公告 |

#### `legal_level` 越南分類定義
根據越南的 Law on Promulgation of Legal Documents 第四條規定

| legla level (high to low） | description |
|----------------------------|--------------|
| Constitution (Hiến pháp)   | The supreme law of Vietnam, enacted by the National Assembly. All other legal documents must conform to the Constitution |
| Codes, Laws, and Resolutions of the National Assembly (Bộ luật, Luật, Nghị quyết của Quốc hội) | Comprehensive legal documents governing various sectors, such as the Civil Code (Bộ luật Dân sự), Penal Code (Bộ luật Hình sự), and specific laws like the Law on Enterprises (Luật Doanh nghiệp). Resolutions address specific issues or policies |
| Ordinances and Resolutions of the Standing Committee of the National Assembly (Pháp lệnh, Nghị quyết của Ủy ban Thường vụ Quốc hội) | Legal instruments issued when the National Assembly is not in session, covering areas not yet legislated or requiring urgent regulation |
| Orders and Decisions of the President (Lệnh, Quyết định của Chủ tịch nước) | Legal documents issued by the President, including orders to promulgate laws and decisions on specific matters within presidential authority |
| Decrees of the Government (Nghị định của Chính phủ) | Detailed regulations guiding the implementation of laws, issued by the Government |
| Decisions of the Prime Minister (Quyết định của Thủ tướng Chính phủ) | Directives issued by the Prime Minister to manage and administer state affairs |
| Resolutions of the Council of Justices of the Supreme People's Court (Nghị quyết của Hội đồng Thẩm phán Tòa án nhân dân tối cao) | Interpretative documents guiding the uniform application of laws across the judiciary |
| Circulars of the Chief Justice of the Supreme People's Court and the Prosecutor General of the Supreme People's Procuracy (Thông tư của Chánh án Tòa án nhân dân tối cao, Viện trưởng Viện kiểm sát nhân dân tối cao) | Guidelines issued to ensure consistent legal interpretation and enforcement within their respective systems |
| Circulars of Ministers and Heads of Ministerial-Level Agencies (Thông tư của Bộ trưởng, Thủ trưởng cơ quan ngang bộ) | Detailed instructions and regulations within specific sectors, issued to implement laws and decrees |
| Decisions of the State Auditor General (Quyết định của Tổng Kiểm toán Nhà nước) | Regulations and directives pertaining to state audit activities.|
| Resolutions of People's Councils at Provincial Level (Nghị quyết của Hội đồng nhân dân cấp tỉnh) | Local legislative documents addressing regional governance and policies |
| Decisions of People's Committees at Provincial Level (Quyết định của Ủy ban nhân dân cấp tỉnh) | Administrative decisions implementing laws and policies within the province |
| Resolutions of People's Councils at District Level (Nghị quyết của Hội đồng nhân dân cấp huyện) | Local legislative documents for district-level governance |
| Decisions of People's Committees at District Level (Quyết định của Ủy ban nhân dân cấp huyện) | Administrative decisions at the district level |
| Legal Documents of Local Administrations in Special Administrative-Economic Units (Văn bản quy phạm pháp luật của chính quyền địa phương ở đơn vị hành chính - kinh tế đặc biệt) |Regulations specific to special zones with unique administrative and economic arrangements |



## Taiwan
### Table: tw_capacit

