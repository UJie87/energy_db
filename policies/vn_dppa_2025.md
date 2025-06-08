---
country: VN
policy_id: 57/2025/ND-CP
topic: DPPA
full_name: Direct Power Purchase Agreement
effective_year: 2025
status: active
policy_type: renewable energy procurement
legal_level: Decrees of the Government
source:
  - https://vanban.chinhphu.vn/?pageid=27160&docid=213012
---
### Summary
On the mechanism for direct electricity purchase and sale between renewable energy generators (RE GENCO) and large electricity consumers

| mechanism                    | parties                                   | contract type                                                                                                                       |
| ---------------------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| DPPA via private power lines | RE GENCO, Large electricity consumer      | DPPA (RE GENCO- consumer )                                                                                                          |
| DPPA via the National gird   | RE GENCO, Large electricity consumer, EVN | - VWEM PPA (EVN- RE GENCO)<br>- PPA (EVN-consumer)<br>- Forward Contract, CfD (RE GENCO- consumer)<br>*all contracts are necessary* |

<!--SUMMARY SPLIT-->

<!--CARD: via_private_power_lines-->
#### DPPA via Private Power Lines
##### applicable participants

- RE GENCO: 電力法第4條第14款規定的再生能源發電單位
- Large electricity consumer: 工貿部部長規定具有大容量和高消耗量的用電戶
##### application process

**Licensing --> Agreement --> Report**

Step 1. Licensing
RE GENCO should conduct procedures on planning, investment, construction, power operation licenses for projects, works and grids to sell electricity directly to Consumers.

Step 2. Agreement
RE GENCO and the Consumer should negotiate the DPPA privately; both the contracted volume and price are open to negotiation, as there's no price ceiling.

Step 3. Report
Within 10 days of signing the DPPA, the consumer must prepare a written report that includes:
- Information related to the DPPA
- The contracted volume
- The agreed DPPA price
This report must be submitted to the local Provincial People’s Committee and copied to the local EVN Power Company (PC) and the System and Market Operator (SMO) operating in the area.
##### contract
Only one contract need to sign under this mechanism.
##### price structure


<!--CARD: via_national_grid-->
買家可以透過兩種方式直接採購再生能源電：
1. 透過獨立電網與RE GENCO(renewable energy generation corporate) 簽約
2. 透過國家電網與EVN簽約

<!--CARD: detailed_comparison-->
fruiwofijtgrfjwri

<!--CARD: opinion-->

目前有疑慮的部分主要有兩大點：
- 沒有提到再生能源憑證在DPPA會怎麼發放，這很重要，這會關乎EVN 是怎麼進行再生能源電力結算的
- EVN的履約保證僅有收錄在附錄二說會有履約保證，但沒有詳細條款是EVN 會怎麼樣履約

<!--CARD: casestudy-->

(await for market update)

<!--CARD: policy_structure_n_outline-->

#### 第一章：總則

- 用電戶可以透過兩種方式直接購買再生能源:
	1. 透過獨立電網進行直接購電的參與對象包括：
	    - 再生能源發電單位：擁有根據電力法第4條第14款規定的再生能源發電單位
	    - 大型用電戶：根據「工貿部部長規定，具有大容量和高消耗量的客戶」
	2. 透過國家電網進行直接購電的參與對象包括
	    - 再生能源發電單位：總發電容量需超過10MW以上的再生能源發電廠，且併入國家電廠直接參與競爭性批發電力市場
	    - 大型用電戶：必須是以生產、經營、服務為目的的使用電力。用電電壓等級必須在22kV以上

| 機制           | 可參與再生能源發電單位定義                          | 可參與大型用電戶定義                            |
| ------------ | -------------------------------------- | ------------------------------------- |
| 透過獨立電網進行直接購電 | 電力法第4條第14款規定的再生能源發電單位                  | 工貿部部長規定具有大容量和高消耗量的用電戶                 |
| 透過國家電網進行直接購電 | - 總發電容量超過10MW<br>- 併入國家電廠直接參與競爭性批發電力市場 | - 以生產、經營、服務為目的使用電力<br>- 用電電壓等級在22kV以上 |


- 交易週期為30分鐘，是電力的交易、量測和結算基礎時間單位


#### 第二章：透過獨立電網進行直接購電

- 說明透過獨電網進行直接購電的基本原則，強調發電單位和的大型用電戶透過雙方同意的獨立線路進行電力交易。價格和電量由雙方協商確定，不受最高價格框架限制（第六條）

- 規定再生能源發電單位和大型用電戶具有電網建設與運行、電力供應和使用安全等責任

- 由再生能源發電單位投資，為大型用電戶安裝屋頂太陽能電力系統所產生的餘電不得超過實際發電的20%，多餘電力的買賣價格可由雙方協商，但不得超過與該類別發電價格框架中規定的最高價格


#### 第三章：透過國家電網進行直接購電

透過國家電網進行直接購電，共有三份合約會參與在該市場機制中：

- 再生能源發電單位在即時市場上銷售電力(RE GENCO -- EVN)
    - 生產的全部電量都需要在**競爭性批發電力市場的即時市場**上銷售
    - 在即時市場的電力銷售價格是根據工貿部關於競爭性批發電力市場運營的規定確定的「即時市場價格」
    - EVN（或被授權的單位）會根據即時市場的支付結算規則，向再生能源發電單位支付其在即時市場上銷售到電量收益
    - 支付金額是根據每個結算週期測量到的用電量 $Q_mq(i)$ 乘以該週期的即時市場價格$FMP(i)$ 來計算總和 。計算公式為：$$R_g = Σ(Q_mq(i) * FMP(i))$$
- 大型用電戶從 EVN 購買電力(EVN -- Power Offtaker)
    - 購電協議內容
    - 大型用電客戶向 EVN/電力公司支付的總電費 $CKH$ 是根據以下公式計算的 : $$ CKH = CBN + CDPPA + CCL + CBL $$
        - $CBN$ 再生能源電能費用：大型用電戶中，再生能源匹配且使用（匹配依據：用電量與再生能源發電單位即時市場銷售電量一致）後，依據即時市場價格進行再生能源價格的支付，計算公式為: $$CBN = Σ (QKHhc(i) * CFMP(i) * Kpp)$$
            - $QKHhc(i)$：大型用電客戶在結算週期 $i$ 的再生能源用電量 。
            - $CFMP(i)$：越南電力集團/電力公司在結算週期  $i$  從即時市場購買電力的價格
            - $Kpp$：電網耗損係數
        - $CDPPA$ 使用電網的費用：使用國家電網進行電力傳輸和相關服務的成本。$$CDPPA = Σ (QKHhc(i) * CDPPAav)$$
            - $QKHhc(i)$：大型用電客戶在結算週期 $i$ 的再生能源用電量 。
            - $CDPPAav$：大型用電客戶在當年 $N$ 使用電力系統服務的平均費用率。這個費用率涵蓋了輸電、配電、系統運行、市場運行、調度、行政管理等成本，並根據工貿部規定，參考 EVN 在前一年 $N-2$ 的相關總成本和利潤進行計算和公佈
        - $CCL$ 年度差額平衡費用：分擔電力系統在不同類型發電和市場機制下的成本平衡。其詳細計算非常複雜，規定在法規的附件 IV (Phụ lục IV) 中。它包括了多個組成部分，涵蓋了不同類型發電（如 BOT 電廠、常規市場參與者、支援電力市場的發電廠等）的購電價格差異、系統輔助服務費用、線路損耗相關的費用、以及其他未能分配或報銷的差額等。
        - $CBL$ 按零售電價購買電力的費用：沒有匹配到再生能源，使用傳統電力的費用。超出與再生能源單位匹配量的部分，將按照標準的零售電價支付給 EVN/電力公司。計算公式為 $$CBL = Σ ((QKH(i) - QKHhc(i)) * PBL(i))$$
            - $QKH(i)$：大型用電客戶在結算週期 i 的實際用電量
            - $QKHhc(i)$：如上所述大型用電客戶在結算週期 $i$ 的再生能源用電量。因此，$QKH(i) - QKHhc(i)$ 代表客戶在該週期內的實際用電量中超過與再生能源發電單位匹配並調整後的電量的那一部分
            - $PBL(i)$：工貿部規定的在結算週期 $i$ 的零售電價
- 大型用電戶透過期貨合約向發電單位購買電力 (RE GENCO -- Power Offtaker)
    - 電力期貨合約內容（附錄三）
    - 規定客戶需依據期貨合約價格向發電單位支付費用的計算方式
    - 這個機制與前一個機制並行，客戶需要同時從EVN（即時市場）和從再生能源發電單位（期貨合約）進行支付計算
    - 這個期貨合約的作用類似CfD機制。合約中會約定一個承諾價格和一個承諾電量，根據期貨合約的規定，大型用電戶（或零售單位）與再生能源發電單位之間會進行**差價結算**支付（或收取）的金額計算方式是基於期貨合約的承諾價格和即時市場價格之間的差額，乘以期貨合約中承諾的電量。$$Rc = Σ (PCk(i) - FMP(i)) * Qck(i)$$
        - $Rc$: 在該結算週期內，根據期貨合約應支付或收取的總金額
        - $PCk(i)$: 在交易週期 i 期貨合約中承諾的價格
        - $FMP(i)$: 在交易週期 i 即時市場上的價格
        - $Qck(i)$: 在交易週期 i 期貨合約中承諾的電量
        
    - 如果期貨承諾價格 $PCk$ 高於即時市場價格 $FMP$，則大型用電戶需要向再生能源發電單位支付差額；反之亦然

#### 第四章：申請流程與文件

- 透過獨立電網進行直接購電的流程與文件
    - 流程：再生能源發電單位執行獨立電網與發電相關設施的營建活動 —> 兩方簽訂電力採購協議 —> 用電戶（或授權的零售單位）在開始透過獨立電網進行直接購電活動時，應將一份通知報告 (báo cáo)發送給所在地的省級工貿廳或直轄市人民委員會
    - 需提交的文件（需在簽訂購電協議後10天內提交）
        - 購電協議相關資訊
        - 約定的購電量
        - 電價
- 透過國家電網進行直接購電的流程與文件
    - 如果大型用電戶和EVN （或經授權、分級的單位）進行電力採購需要與EVN 簽訂PPA，並且與可再生能源發電單位簽署forward PPA
    - 流程：大型用電戶（或零售單位）向EVN電力公司提交參與該機制的申請文件 —> EVN 收到申請文件後的5個工作天內，進行文件檢查，並回函確認或要求補件 —> 確認文件有效後5個工作天內，EVN 應書面回覆大型用電戶，確認參與資格、預計簽訂協議的時間以及預計開始執行的日期 —> 工貿部/ERAV 會在競爭性批發電力市場資訊系統上公布參與客戶名單 —> 大型用戶與EVN 簽訂PPA —> EVN 通知工貿部/ERAV 已簽訂PPA —> 客戶根據簽訂內容開始購電
    - 申請文件應包括（第26條第2款規定）
        - 參與直接購電的申請書
        - 大型用電戶與EVN 之間關於簽訂PPA的原則性協商或協商文件（第15條有規定詳細資訊）
        - 大型用電戶目前機器設備、容量、營運狀況以及現有（如有）PPA 的報告
        - 大型用電戶資訊（用電地點、目的、電壓等級、契約容量…)
- 說明可以申請暫停、終止或恢復參與的規定和程序
- 詳細規定參與者需要提交的各類報告，附件有提供模板

#### 第五章：施行條款

- 實施責任
- 過渡條款
- 這份法規取代 80/2024/ND-CP

#### 附錄

- 附錄一：即時市場電力購電協議內容
- 附錄二：大型用電戶或區域／集群授權電力零售單位與總電力公司（或電力公司）之間的購電協議內容
- 附錄三：電力期貨合約的主要內容
- 附錄四：年度差價補償付款費用
- 附錄五：報告表格範例


