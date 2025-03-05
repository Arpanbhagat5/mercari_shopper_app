# Mercari Japan Shopper

## Description

Command-line application for searching Mercari Japan using natural language.

**Key Features:**

*   Natural Language Search (English/Japanese)
*   Parameter Extraction via Local LLM (Ollama/Llama3.2)
*   Real Mercari Japan API Interaction (via [`mercapi API`](https://github.com/take-kun/mercapi))
*   Item Recommendations (LLM-generated)
*   Bilingual (English/Japanese queries)

**Limitations (Important):**  **Real API interaction is experimental and potentially unreliable. Expect "No Items Found" or limited results.** See "Limitations" section for details.

## Project Structure

The project consists of the following Python files:
```
mercari_shopper_app/
├── mercari_shopper_app.py      # Main script (CLI)
├── mercapi_api_client.py      # Mercari API interaction (mercapi-api.py)
├── llm_parameter_extraction.py # LLM parameter extraction & recommendations
├── parameter_matcher.py       # Category ID matching
├── prompts.py                 # LLM prompts
├── categories.json            # Mercari category data
├── requirements.txt           # Dependencies
└── README.md                  # Documentation
```

## Setup Instructions

1.  **Prerequisites:**
    *   **Ollama:** [ollama.com](https://ollama.com/) - Install & run server. Verify: `ollama list` in terminal.
    *   **Ollama Model:** `llama3.2` - Pull model: `ollama pull llama3.2` in terminal.
    *   **Python:** Python 3.x installed.

2.  **Clone/Download Project:** Get all Python files, `categories.json`, `requirements.txt`.
    ```
    git clone git@github.com:Arpanbhagat5/g-m-s.git
    ```

3.  **Virtual Environment (Recommended):**
    *   Navigate to project dir: `cd v4`
    *   Create: `python3 -m venv venv`
    *   Activate: `source venv/bin/activate` (macOS/Linux) or `venv\Scripts\activate` (Windows)

4.  **Install Dependencies:**
    *   Activated venv: `pip install -r requirements.txt`

5.  **Run Application:**
    *   Terminal, project dir: `python mercari_shopper_app.py`

## Usage Instructions

1.  Run `mercari_shopper_app.py`.
2.  Enter search request when prompted (or `exit`). Examples:
    *   `cheap manga`
    *   `vintage watch under 5000 yen`
    *   `nintendo switch new`
    *   `kids swimsuit`
3.  Application output: Extracted parameters, Mercari search results (if any), LLM recommendations.
4.  Repeat or type `exit`.

## Usage Example
**User Request:** `格安のNintendo switch light 本体のみ (cheap switch light console only)`

**Expected Output (Example - actual output may vary):**
```
Enter your Mercari Japan search request (or type 'exit' to quit):
Nintendo switch 本体のみ

--- User Request: "Nintendo switch 本体のみ" ---
{
  "query": "Nintendo switch \u672c\u4f53\u306e\u307f",
  "price_min": null,
  "price_max": null,
  "categories": [],
  "brands": [
    ""
  ],
  "item_conditions": [],
  "shipping_payer": [],
  "sort_by": "",
  "sort_order": ""
}
Simulating Mercari search...
Generating item recommendations...


**Mercari Search Results (Top Items for recommendation generation):**
- Item Name: マイクラソフト　本体のみ, Price: ¥2980, Condition: Used - Excellent, Item ID: m54885282081
- Item Name: Nintendo Switch Lite ターコイズ 本体のみ, Price: ¥9999, Condition: Used - Poor, Item ID: m90044012651
- Item Name: 【美品】新型Switch本体　ニンテンドースイッチ本体　新型モデル本体　新型本体, Price: ¥19800, Condition: Like new, Item ID: m54904812676
- Item Name: Nintendo Switch スイッチ 本体のみ 新モデル, Price: ¥14500, Condition: Used - Fair, Item ID: m66742308875
- Item Name: ドラゴンクエストIII そして伝説へ… SWITCH ロトの剣付き, Price: ¥7200, Condition: Used - Excellent, Item ID: m56905921984
- Item Name: 任天堂switch　有機EL　スプラトゥーン　本体のみ, Price: ¥20500, Condition: Used - Good, Item ID: m14621327063
- Item Name: 25022704 ドリームスイッチ セット, Price: ¥5200, Condition: Used - Good, Item ID: m51676206359
- Item Name: ドリームスイッチ　本体、台座、リモコン、外箱のみ, Price: ¥2000, Condition: Used - Excellent, Item ID: m34429120842
- Item Name: 未対策機　Nintendo Switch 本体のみ, Price: ¥15000, Condition: Used - Fair, Item ID: m50612800291
- Item Name: スイッチ 本体のみ, Price: ¥13000, Condition: Used - Fair, Item ID: m20638420716
- Item Name: Nintendo Switch リングフィット アドベンチャー　③, Price: ¥3600, Condition: Used - Fair, Item ID: m48838519968
- Item Name: 【訳有り】Nintendo Switch スイッチ 本体のみ 液晶のみ, Price: ¥11800, Condition: Used - Excellent, Item ID: m26972907984
- Item Name: 純正プロコン(本体のみ), Price: ¥3400, Condition: Used - Excellent, Item ID: m53330610605
- Item Name: PDP afterglow wireless 最終値下げ, Price: ¥2888, Condition: Used - Good, Item ID: m43258369887
- Item Name: Nintendo Switch 本体のみ　動作正常　2018年　旧型, Price: ¥13880, Condition: Used - Excellent, Item ID: m69754982915
- Item Name: 美品　NintendoSwitch　ニンテンドースイッチ本体　有機ELモデル, Price: ¥20900, Condition: Used - Excellent, Item ID: m13904992131
- Item Name: Nintendo Switch 2017年, Price: ¥12000, Condition: Used - Good, Item ID: m84686097666
- Item Name: バッテリー強化型　ニンテンドースイッチ本体　NintendoSwitch, Price: ¥15500, Condition: Used - Fair, Item ID: m93869353493
- Item Name: Nintendo Switch Lite コーラル　本体のみ, Price: ¥14500, Condition: Used - Good, Item ID: m20314680970
- Item Name: 【本体のみ】ドリテックステンレス電気ケトル, Price: ¥2480, Condition: Used - Excellent, Item ID: m70126701143


--- LLM Generated Recommendations: ---
1. **Nintendo Switch Lite コーラル 本体のみ**
   Price: ¥14,500 (Condition: Used - Good)
   Reason: Relevance to the user's main query: Nintendo Switch console, high price point due to rarity
   [View on Mercari](https://jp.mercari.com/item/m20314680970)

2. **ドリームスイッチ 本体、台座、リモコン、外箱のみ**
   Price: ¥2,000 (Condition: Used - Excellent)
   Reason: Relevance to the user's main query: Nintendo Switch console, relatively low price point, high condition
   [View on Mercari](https://jp.mercari.com/item/m34429120842)

3. **美品　NintendoSwitch　ニンテンドースイッチ本体　有機ELモデル**
   Price: ¥20,900 (Condition: Used - Excellent)
   Reason: Relevance to the user's main query: Nintendo Switch console, high quality and condition
   [View on Mercari](https://jp.mercari.com/item/m13904992131)


--- Mercari Simulation Status: Success ---
Found 120 items.

```

## Design Choices

*   **Local LLM (Ollama/Llama3.2):**
    *   Cost-effective, private, offline capable.
    *   Sufficient for parameter extraction & recommendations.
    *   Ollama simplifies setup & experimentation.
    *   (minus) Not as capable as paid ones like Claude or OpenAI models

*   **`mercapi-api.py` Library:**
    *   **Real Mercari API Interaction:** Designed for real API, simplifies integration.
    *   Abstracts API complexity, structured data handling.
    *   Promotes maintainability, aims for UI result consistency.

*   **JSON for LLM Communication:** Structured, reliable data exchange.
*   **Facet-Based Parameter Matching:** Robust facet handling. Eg. `categories.json`.
*   **Bilingual:** English/Japanese queries supported.

## Limitations

*   **Real Mercari API - Unreliable Interaction:** **Expect issues.**
    *   **"No Items Found"/Limited Results:** Frequent, even for valid queries. API behavior, inventory limitations.
    *   **API Instability/Errors:** External API prone to downtime, changes, rate limits. `mercapi API` library stability not guaranteed.
    *   **Potential Auth Requirements:** API may need authentication not fully implemented.

*   **Recommendation:** API interaction is fragile. "No Items Found" may be normal API response. Try broader queries.
*   **Dependency on User Prompts:** Vague prompts may yield vague/no results (like Mercari UI).
*   **Price Range Queries in Query String:**  May not be fully supported by Mercari API. Use general keywords + price parameters.
*   **Category Matching:** Imperfect matching, limited/outdated `categories.json`.
*   **Brand/Condition/Shipping Facets:** Extracted but not fully used in API or recommendations.

## Potential Improvements

*   **Improve Mercari API Reliability:**
    *   Robust error handling, logging, retries.
    *   Investigate API authentication needs.
    *   Verify parameter mapping, API compatibility.
    *   Explore full `mercapi API` features for better results.

*   **Expand Facet Handling:** Implement Brand/Condition/Shipping facets in API calls & recommendations.
*   **Fuzzy Category Matching:** Handle category name variations.
*   **Enhanced Recommendations:** Consider item popularity, ratings (if API provides), visual similarity, advanced NLP.
*   **User Interface:** Web UI or desktop GUI.
*   **Advanced Price Understanding:** Handle complex price queries ("cheapest", "mid-range").
*   **Interactive Prompts:** Clarifying questions for vague user requests.
