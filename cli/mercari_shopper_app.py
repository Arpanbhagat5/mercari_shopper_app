import json
import os
import sys

from internal.api_client.mercari_api_client import simulate_mercari_search
from internal.llm.llm_parameter_extraction import (
    extract_search_parameters_with_llm_ollama,
)
from internal.utils.constants import ITEM_COUNT_FOR_RECOMMENDATION


def get_user_search_request():
    """Prompts the user for a search request or 'exit'."""
    return input(
        "\nEnter your Mercari Japan search request (or type 'exit' to quit):\n"
    )


def display_user_request(user_request):
    """Prints the user's search request to the console."""
    print(f'\n--- User Request: "{user_request}" ---')


def handle_parameter_extraction(user_request):
    """Extracts search parameters using LLM. Handles JSON parsing errors."""
    extracted_params_json = extract_search_parameters_with_llm_ollama(user_request)
    if not extracted_params_json:
        print("Parameter extraction failed.")
        return None

    try:
        extracted_params = json.loads(extracted_params_json)
        print(json.dumps(extracted_params, indent=2))  # Print formatted JSON
        return extracted_params
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None


def handle_mercari_search_simulation(extracted_params):
    """Simulates Mercari search using extracted parameters."""
    print("Simulating Mercari search...")
    mercari_search_result = simulate_mercari_search(extracted_params)
    if not mercari_search_result:
        print("\n--- Mercari Simulation Status: Failure ---")
        print("Search failed, but parameter extraction was successful.")
        return None
    return mercari_search_result


def handle_recommendation_generation(user_request, mercari_search_result):
    """Generates item recommendations using LLM and search results."""
    if not mercari_search_result or not mercari_search_result.items:
        return None  # No recommendations if no search results

    items_for_recommendation = (
        mercari_search_result.items[:ITEM_COUNT_FOR_RECOMMENDATION]
        if len(mercari_search_result.items) > ITEM_COUNT_FOR_RECOMMENDATION
        else mercari_search_result.items
    )
    recommendation_params_json = extract_search_parameters_with_llm_ollama(
        user_request, items_for_recommendation
    )
    if not recommendation_params_json:
        return None

    try:
        recommendation_params = json.loads(recommendation_params_json)
        return recommendation_params
    except json.JSONDecodeError as e:
        print(f"Error parsing Recommendation JSON: {e}")
        return None


def display_recommendations(recommendation_params):
    """Prints formatted LLM-generated recommendations to the console."""
    if not recommendation_params or "recommendations" not in recommendation_params:
        print("No recommendations to display.")
        return

    print("\n--- LLM Generated Recommendations: ---")
    if recommendation_params["recommendations"]:
        for i, recommendation in enumerate(recommendation_params["recommendations"]):
            item_url = f"https://jp.mercari.com/item/{recommendation['item_id']}"
            print(f"{i+1}. **{recommendation['item_name']}**")
            print(
                f"   Price: ¥{recommendation['item_price']:,} (Condition: {recommendation['item_condition']})"
            )
            print(f"   Reason: {recommendation['reason']}")
            print(f"   [View on Mercari]({item_url})\n")
    else:
        print("No recommendations found in LLM response.")


def display_mercari_simulation_status(mercari_search_result):
    """Prints the Mercari simulation status and item count."""
    if mercari_search_result and mercari_search_result.items:
        print("\n--- Mercari Simulation Status: Success ---")
        print(f"Found {len(mercari_search_result.items)} items.")
    elif mercari_search_result:
        print("\n--- Mercari Simulation Status: Success but No Items Found ---")
    else:
        print("\n--- Mercari Simulation Status: Failure ---")


if __name__ == "__main__":
    print("Welcome to Mercari Shopper!")
    while True:
        user_request = get_user_search_request()
        if user_request.lower() == "exit":
            print("Exiting Mercari Shopper...")
            break

        display_user_request(user_request)

        extracted_params = handle_parameter_extraction(user_request)
        if not extracted_params:
            continue  # Skip to next iteration if parameter extraction failed

        mercari_search_result = handle_mercari_search_simulation(extracted_params)

        recommendation_params = handle_recommendation_generation(
            user_request, mercari_search_result
        )
        display_recommendations(recommendation_params)
        display_mercari_simulation_status(mercari_search_result)
