import json

# item count for recommendations
N = 20

# --- Item Condition ID to Name Mapping ---
item_condition_id_to_name = {
    1: "New, unused",  # "新品、未使用"
    2: "Like new",  # "未使用に近い"
    3: "Used - Excellent",  # "目立った傷や汚れなし"
    4: "Used - Good",  # "やや傷や汚れあり"
    5: "Used - Fair",  # "傷や汚れあり"
    6: "Used - Poor",  # "全体的に状態が悪い"
}


english_to_japanese_categories = {
    "fashion": "ファッション",
    "electronics": "家電",
    "gadgets": "ガジェット",
    "home & living": "家具・インテリア",
    "beauty & health": "美容・健康",
    "electronics & gadgets": "家電・スマホ・カメラ",
    "home & living": "インテリア・住まい・小物",
    "hobbies & collectibles": "おもちゃ・ホビー・グッズ",
    "cosmetics & beauty": "コスメ・香水・美容",
    "sports & outdoors": "スポーツ・レジャー",
    "handmade": "ハンドメイド",
    "books, music & games": "本・音楽・ゲーム",
    "food, sweets & drinks": "食品/飲料/酒",
    "baby & kids": "ベビー・キッズ",
    "tickets & coupons": "チケット",
    "other": "その他",
    "manga": "漫画",
    "anime": "アニメグッズ",
    "toys": "おもちゃ",
    "games": "ゲーム",
}


def get_category_ids_from_names(category_names):
    """
    Maps a list of category names to a list of Mercari category IDs using categories.json.

    Args:
        category_names: A list of category names (strings).

    Returns:
        A list of category IDs (integers) corresponding to the given names.
        Returns an empty list if any category name is not found.
    """
    category_ids = []
    category_name_to_id_map = {}  # Create a map for faster lookup

    try:
        with open("facets/categories.json", "r", encoding="utf-8") as f:
            categories_data = json.load(f)
            if categories_data and "data" in categories_data:
                # Process categories and build the map
                def process_category_list(category_list):
                    for category_item in category_list:
                        category_name_to_id_map[category_item["name"]] = category_item[
                            "id"
                        ]
                        if "child" in category_item:
                            process_category_list(
                                category_item["child"]
                            )  # Recursive call for children

                process_category_list(
                    categories_data["data"]
                )  # Start processing from the root

            else:
                print(
                    "Warning: 'categories.json' does not have expected 'data' structure in tool_utils."
                )
                return []  # Return empty list if data is not in expected format

    except FileNotFoundError:
        print(
            "Error: 'categories.json' file not found in tool_utils. Make sure it's in the same directory as the script."
        )
        return []  # Return empty list if file not found
    except json.JSONDecodeError:
        print(
            "Error: Could not decode 'categories.json' in tool_utils.  File might be corrupted."
        )
        return []  # Return empty list if JSON is invalid

    for name in category_names:
        if name in category_name_to_id_map:
            category_ids.append(category_name_to_id_map[name])
        else:
            print(
                f"Warning: Category name '{name}' not found in 'categories.json' in tool_utils."
            )
            return (
                []
            )  # If any category is not found, return empty list (for now, to be strict)
            # You could modify this to return IDs for found categories and skip unfound ones if needed.

    return category_ids
