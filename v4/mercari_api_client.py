import asyncio
from mercapi import Mercapi


def simulate_mercari_search(search_params):
    """Simulates a Mercari search and returns raw search results.
    Now handles category IDs directly.
    """

    mercari_params = {}
    mercari_params["query"] = search_params.get("query", "")
    mercari_params["price_min"] = search_params.get("price_min")
    mercari_params["price_max"] = search_params.get("price_max")

    category_ids = search_params.get("categories", [])
    mercari_params["categories"] = category_ids

    mercari_params["brands"] = search_params.get("brands", [])
    mercari_params["item_conditions"] = search_params.get("item_conditions", [])
    mercari_params["shipping_payer"] = search_params.get("shipping_payer", [])

    try:
        m = Mercapi()
        results = asyncio.run(
            m.search(
                query=mercari_params["query"],
                price_min=mercari_params["price_min"],
                price_max=mercari_params["price_max"],
                categories=mercari_params["categories"],
                # TODO Handle with same logic as categories
                # brands=mercari_params["brands"], # Facet params commented out for now
                # item_conditions=mercari_params["item_conditions"],
                # shipping_payer=mercari_params["shipping_payer"],
            )
        )
        return results

    except Exception as e:
        print(f"\n--- Error during mercapi search in mercari_api_client: {e} ---")
        return None
