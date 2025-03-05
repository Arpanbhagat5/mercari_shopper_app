import json
import re

import requests

from internal.prompts.recommendation_prompt import RECOMMENDATION_PROMPT
from internal.prompts.parameter_extraction_prompt import PARAM_EXTRACTION_PROMPT
from internal.parameter_matching.parameter_matcher import parameter_matcher
from internal.utils.constants import (
    ENG_TO_JPN_CATEGORY_MAP,
    ITEM_CONDITION_ID_TO_NAME_MAP,
)


def extract_search_parameters_with_llm_ollama(user_request_text, mercari_items=None):
    """
    Extracts Mercari Japan search parameters from user request text using a local Ollama LLM (Llama3.2).
    Uses parameter_matcher to validate and match extracted category names to category IDs.

    Args:
        user_request_text: The user's natural language request (string).
        mercari_items: (Optional) List of Mercari items (search results). If provided, the function will generate recommendations instead of just extracting parameters.

    Returns:
        A dictionary containing the extracted search parameters and top 3 item recommendations (if available).
        Returns None if an error occurs during the process.
    """

    if mercari_items:
        top_mercari_items = mercari_items
        search_results_formatted = "\n\n**Mercari Search Results (Top Items for recommendation generation):**\n"

        for item in top_mercari_items:
            condition_name = ITEM_CONDITION_ID_TO_NAME_MAP.get(
                item.item_condition_id, "Condition Unknown"
            )
            search_results_formatted += f"- Item Name: {item.name}, Price: ¥{item.price}, Condition: {condition_name}, Item ID: {item.id_}\n"
        formatted_prompt = RECOMMENDATION_PROMPT.format(
            search_results_placeholder=search_results_formatted,
        )
        print(search_results_formatted)
    else:
        formatted_prompt = PARAM_EXTRACTION_PROMPT.format(
            user_request=user_request_text
        )

    ollama_api_url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3.2",
        "prompt": formatted_prompt,
        "max_tokens": 750,
        "temperature": 0.5,
        "stop_sequence": "\n\n",
    }

    try:
        response = requests.post(ollama_api_url, json=data, stream=True)
        response.raise_for_status()

        json_text_builder = []
        for line in response.iter_lines():
            if line:
                try:
                    json_line = json.loads(line)
                    if "response" in json_line:
                        json_text_builder.append(json_line["response"])
                except json.JSONDecodeError:
                    print(f"Warning: Could not decode JSON line: {line}")

        json_text = "".join(json_text_builder).strip()

        try:
            extracted_params_json = json.loads(json_text)

            # --- Category Name Matching and ID Conversion ---
            if "categories" in extracted_params_json:
                extracted_category_names = extracted_params_json["categories"]
                matched_category_ids = parameter_matcher.match_category_names_to_ids(
                    extracted_category_names
                )  # Use parameter_matcher
                if matched_category_ids:
                    extracted_params_json["categories"] = (
                        matched_category_ids  # Replace category names with IDs
                    )
                else:
                    extracted_params_json["categories"] = None
                    print(
                        "Warning: No valid category IDs found for extracted category names."
                    )

            return json.dumps(extracted_params_json)

        except json.JSONDecodeError as json_err:
            print(f"Error: JSON Decode Error in llm_parameter_extraction: {json_err}")
            return None

    except requests.exceptions.RequestException as req_err:
        print(f"Request error in llm_parameter_extraction: {req_err}")
        return None
    except Exception as e:
        print(f"Unexpected error in llm_parameter_extraction: {e}")
        return None
