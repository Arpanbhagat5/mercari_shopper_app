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
    # NOTE: This is a partial mapping for demonstration purposes.
    # The actual mapping should include all relevant categories.
    # Not all the categories listed here are mapped as used by mercari actually
    "fashion": "ファッション/小物",
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
    "baby & kids": "キッズ/ベビー",
    "kids": "キッズ/ベビー",
    "baby": "キッズ/ベビー",
    "tickets & coupons": "チケット",
    "other": "その他",
    "manga": "漫画",
    "anime": "アニメグッズ",
    "toys": "おもちゃ",
    "games": "ゲーム",
}
