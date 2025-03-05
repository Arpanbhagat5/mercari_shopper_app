import json
import os
import sys

from internal.api_client.mercari_api_client import simulate_mercari_search
from internal.llm.llm_parameter_extraction import (
    extract_search_parameters_with_llm_ollama,
)
from internal.utils.constants import ITEM_COUNT_FOR_RECOMMENDATION

if __name__ == "__main__":
    print("Welcome to Mercari Shopper!")
    while True:  # Start an infinite loop for continuous interaction
        user_request = input(
            "\nEnter your Mercari Japan search request (or type 'exit' to quit):\n"
        )
        if user_request.lower() == "exit":  # Allow user to exit
            print("Exiting Mercari Shopper...")
            break

        print(f'\n--- User Request: "{user_request}" ---')  # Echo user request
        # --- PART 1: Parameter Extraction ---
        extracted_params_json = extract_search_parameters_with_llm_ollama(user_request)
        if extracted_params_json:
            # print("--DEBUG--Extracted Parameters (JSON):")
            # print(extracted_params_json)  # Print JSON string
            try:
                extracted_params = json.loads(extracted_params_json)
                # print("--DEBUG--Parsed Parameters (Dictionary):")
                print(json.dumps(extracted_params, indent=2))

                # --- PART 2: Simulate Mercari Search (using PART 1 parameters) ---
                print("Simulating Mercari search...")  # Added interactive text
                mercari_search_result = simulate_mercari_search(extracted_params)
                if mercari_search_result is not None:  # Success

                    # --- PART 3: Generate Recommendations using LLM (with search results) ---
                    # Pass only top items for recommendation
                    print("Generating item recommendations...")
                    items_for_recommendation = (
                        mercari_search_result.items[:ITEM_COUNT_FOR_RECOMMENDATION]
                        # mercari_search_result.items # Use all items
                        if mercari_search_result.items
                        and len(mercari_search_result.items)
                        > ITEM_COUNT_FOR_RECOMMENDATION
                        else []  # Use all items if less than ITEM_COUNT_FOR_RECOMMENDATION
                    )
                    recommendation_params_json = (
                        extract_search_parameters_with_llm_ollama(
                            user_request,
                            items_for_recommendation,
                        )
                    )
                    if recommendation_params_json:
                        # print("\n--DEBUG-- Recommendation Parameters (JSON): ---")
                        # print(recommendation_params_json)
                        try:
                            recommendation_params = json.loads(
                                recommendation_params_json
                            )
                            if "recommendations" in recommendation_params:
                                print("\n--- LLM Generated Recommendations: ---")
                                if recommendation_params["recommendations"]:
                                    for i, recommendation in enumerate(
                                        recommendation_params["recommendations"]
                                    ):
                                        item_url = f"https://jp.mercari.com/item/{recommendation['item_id']}"
                                        print(
                                            f"{i+1}. **{recommendation['item_name']}**"
                                        )
                                        print(
                                            f"   Price: ¥{recommendation['item_price']:,} (Condition: {recommendation['item_condition']})"
                                        )
                                        print(f"   Reason: {recommendation['reason']}")
                                        print(f"   [View on Mercari]({item_url})\n")
                                else:
                                    print("No recommendations found in LLM response.")
                            else:
                                print("Warning: 'recommendations' key not found.")

                        except json.JSONDecodeError as e:
                            print(f"Error parsing Recommendation JSON: {e}")

                    if mercari_search_result.items:  # Check if items exist
                        print("\n--- Mercari Simulation Status: Success ---")
                        print(f"Found {len(mercari_search_result.items)} items.")
                    else:
                        print(
                            "\n--- Mercari Simulation Status: Success but No Items Found ---"
                        )
                else:
                    print("\n--- Mercari Simulation Status: Failure ---")  # Failure
                    print("Search failed, but param extraction was successful.")

            except json.JSONDecodeError as e:
                print(f"Error parsing JSON: {e}")

        else:
            print("Parameter extraction failed.")
