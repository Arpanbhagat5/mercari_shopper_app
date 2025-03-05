# Mercari Japan Shopper

## Description

This is a command-line application that helps users search for items on Mercari Japan (a popular online marketplace in Japan) using natural language requests.

The application uses a local Large Language Model (LLM) via Ollama to understand user requests, extract relevant search parameters, simulate a Mercari search, and then generate item recommendations based on the search results.

## Project Structure

The project consists of the following Python files:

*   **`mercari_shopper_app.py`**:
    *   This is the main application script.
    *   It handles user interaction (prompting for search requests, displaying output).
    *   Orchestrates the overall workflow: parameter extraction, search simulation, and recommendation generation.

*   **`mercari_api_client.py`**:
    *   Contains the `simulate_mercari_search` function.
    *   Simulates interaction with the Mercari API (currently does not use the real API).
    *   Takes search parameters as input and returns simulated search results.

*   **`llm_parameter_extraction.py`**:
    *   Contains the `extract_search_parameters_with_llm_ollama` function.
    *   Uses Ollama and a Large Language Model (LLM) to extract search parameters from user requests.
    *   Processes user input using NLP techniques to identify query, price range, categories, etc.

*   **`tool_utils.py`**:
    *   Contains utility functions and data mappings.
    *   Currently includes:
        *   `english_to_japanese_categories`: A dictionary for translating English category names to Japanese.
        *   `item_condition_id_to_name`: A dictionary mapping item condition IDs to names.

*   **`facets_config.py`**:
    *   Manages facet configuration data loaded from JSON files.
    *   Currently loads and provides access to category data from `categories.json`.
    *   Provides functions to get valid category names and map names to IDs.

*   **`parameter_matcher.py`**:
    *   Contains the `ParameterMatcher` class and related functions.
    *   Responsible for validating and matching extracted parameter names (e.g., category names) against valid values from `facets_config.py`.
    *   Translates English category names to Japanese for matching.

*   **`prompts.py`**:
    *   Stores the prompt templates used for interacting with the LLM (Ollama).
    *   Includes `PARAM_EXTRACTION_PROMPT` for parameter extraction and `RECOMMENDATION_PROMPT` for recommendation generation.

*   **`categories.json`**:
    *   JSON file containing Mercari category data.
    *   Used by `facets_config.py` to load valid category names and IDs.
*   **`requirements.txt`**:
    *   Lists the Python dependencies for this project.
    *   Used to install required libraries using `pip`.
## Setup Instructions

1.  **Prerequisites:**
    *   **Ollama:** You need to install and run Ollama on your system. Ollama is a tool that allows you to run large language models locally.
        *   **Download Ollama:** Go to the [Ollama website](https://ollama.com/) and download the installer for your operating system (macOS, Linux, or Windows).
        *   **Install Ollama:** Run the installer you downloaded and follow the on-screen instructions.
        *   **Run Ollama Server:** After installation, you need to ensure the Ollama server is running in the background.
            *   **On macOS:** Ollama should start automatically after installation. You should see the Ollama icon in your menu bar.
            *   **On Windows:** Ollama should also start automatically. Check your system tray for the Ollama icon.
            *   **On Linux:** You might need to start the Ollama server manually after installation. Refer to the [Ollama documentation](https://ollama.com/docs/linux) for specific instructions for your Linux distribution.  Typically, you might run `ollama serve` in a terminal, or use systemd if provided in the installation instructions.
        *   **Verify Ollama is Running:** To check if Ollama is running, open your terminal and try to run the command `ollama list`. If Ollama is running correctly, this command should list the models you have available (you might not have any models yet, which is fine at this stage). If it's not running, you'll likely see an error message like "Error: could not connect to Ollama server".

    *   **Ollama Model:**  Make sure you have the `llama3.2` model (or a compatible model) available in Ollama. You can pull it by running: `ollama pull llama3.2` in your terminal.
    *   **Python:** Python 3.x must be installed on your system.

2.  **Clone or Download the Project:**  Make sure you have all the Python files (`mercari_shopper_app.py`, `mercari_api_client.py`, `llm_parameter_extraction.py`, `tool_utils.py`, `facets_config.py`, `parameter_matcher.py`, `prompts.py`) in the same directory.

3.  **Set up a Virtual Environment (Recommended):**
    *   Navigate to the project directory in your terminal.
    *   Create a virtual environment:
        ```bash
        python3 -m venv venv
        ```
    *   Activate the virtual environment:
        *   On macOS/Linux:
            ```bash
            source venv/bin/activate
            ```
        *   On Windows:
            ```bash
            venv\Scripts\activate
            ```
4.  **Install Dependencies:**
    *   With the virtual environment activated, install the required Python libraries using pip:
        ```bash
        pip install -r requirements.txt
        ```

5.  **Run the Application:** Open your terminal, navigate to the project directory, and run the main script:

    ```bash
    python mercari_shopper_app.py
    ```


## Dependencies

*   Python standard libraries: `json`, `os`, `requests`, `asyncio`, `re`
*   [Mercari API Client Library](https://github.com/take-kun/mercapi): `mercapi` (Note: currently, the code uses a simulated search, but this would be a dependency if you integrate with the real Mercari API).
*   Ollama (<https://ollama.com/>) and a compatible LLM model (like `llama3.2`).

## Usage Instructions
1.  **Enter Search Requests:** The application will prompt you to enter your Mercari Japan search request. Type your request in natural language (English or Japanese) and press Enter.

2.  **Exit:** To exit the application, type `exit` when prompted for a search request.


**User Request:** `格安のNintendo switch light 本体のみ (cheap switch light console only)`

**Expected Output (Example - actual output may vary):**
```
Enter your Mercari Japan search request (or type 'exit' to quit):
Nintendo switch 本体のみ

--- User Request: "Nintendo switch 本体のみ" ---
Warning: Extracted category name '' (or its English version) does not perfectly match valid Mercari categories and will be ignored.
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

*   **Local LLM (Ollama and Llama3.2):**  The application uses a local LLM via Ollama for parameter extraction and recommendation generation. This choice prioritizes user privacy and offline functionality, as the LLM runs locally without relying on external API services. Llama3.2 is chosen as a capable and readily available model in Ollama.
*   **JSON-based Communication with LLM:**  Strict JSON format is enforced for communication with the LLM (both in prompts and expected responses). This ensures structured and reliable data exchange, making it easier to parse and process the LLM's output in Python.
*   **Facet-Based Parameter Matching:**  To improve the accuracy and robustness of parameter extraction, especially for categories, the application employs a facet-based matching mechanism. It loads valid category data from `categories.json` and uses the `parameter_matcher.py` module to validate and map extracted category names to category IDs. This approach is more scalable and maintainable than relying solely on prompt engineering for parameter validation.
*   **Simulated Mercari Search:**  For this version, a simulated Mercari search is implemented using a pre-defined dataset. This allows for development and testing without requiring access to the real Mercari API and avoids potential rate limits or API key management.  The `mercari-api.py` library is included as a potential dependency for future real API integration.
*   **Bilingual Capability:** The prompts and parameter matching logic are designed to handle both English and Japanese user requests, leveraging a simple English-to-Japanese category name mapping for basic translation of category parameters.

## Potential Improvements

*   **Real Mercari API Integration:**  The most significant improvement would be to integrate with the actual Mercari API to fetch live, up-to-date item listings instead of relying on simulated data. This would make the application much more practical and useful.
*   **Expand Facet Handling:** Implement full facet handling for brands, item conditions, shipping payer, and potentially other facets available in the Mercari API. This would involve creating similar facet configuration files and matcher modules for these parameters.
*   **Fuzzy Matching for Categories:**  Improve category matching to handle slight variations or misspellings in user-provided category names using fuzzy matching techniques.
*   **Enhanced Recommendation Logic:**  Refine the item recommendation logic to consider more factors beyond just keyword matching and price.  This could include incorporating item popularity, user ratings (if available), visual similarity, or more sophisticated NLP techniques to understand user intent.
*   **User Interface:** Develop a user-friendly interface (e.g., a web interface or a desktop GUI) to make the application more accessible and easier to use than a command-line interface.
*   **Advanced Price Range Understanding:**  While price range extraction is implemented, further improve the LLM's ability to understand and handle more complex and nuanced price-related queries (e.g., "cheapest gaming laptop", "mid-range camera").
*   **Error Handling and Robustness:**  Enhance error handling throughout the application to gracefully manage API errors, LLM failures, and unexpected user input. Add more input validation and logging.
*   **Support for More Languages:** Extend the bilingual capability to support more languages beyond English and Japanese.

## Limitations

*   **Price Range Queries in Query String:**  Mercari Japan's search functionality (and this simulated search) may not fully support price range specifications (like "under 4000 jpy", "over 25000 yen") directly within the text query itself. While the application *extracts* price ranges from such queries, the actual search filtering might primarily rely on the separate `price_min` and `price_max` parameters. For best results with price filtering, use general item keywords in your query and rely on the extracted price range being applied as a filter.
*   **Category Matching:** Category matching relies on a pre-defined `categories.json` file and English-to-Japanese category name mappings.  Imperfect matches or categories not present in the data may be ignored.
*   **Brand, Condition, Shipping Payer Facets:**  Currently, the application extracts parameters for brands, item conditions, and shipping payer, but these facets are not yet fully implemented in the simulated Mercari search or recommendation generation. Future versions could expand on these facets.
*   **Simulated Search:** This application uses a *simulated* Mercari search. It does not interact with the real Mercari API to fetch live, up-to-date item listings. The search results and recommendations are based on a pre-defined set of example items. To use live Mercari data, integration with the actual Mercari API would be required.
*   **Ollama and Model Dependency:** The application depends on Ollama being installed and running locally, and the `llama3.2` model (or a compatible model) being available. Performance and accuracy may vary depending on the specific LLM model used.
