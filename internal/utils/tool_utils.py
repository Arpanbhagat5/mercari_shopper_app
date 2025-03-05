from internal.parameter_matching.facets_config import (
    config,
)  # Import the config instance


def map_category_names_to_ids(category_names, facets_config=config):
    """
    Maps a list of category names to a list of Mercari category IDs using FacetsConfig.

    For each category name provided, it attempts to find a matching ID from the
    category data loaded by FacetsConfig.  Category names not found in the
    configuration are ignored, and a warning is printed for each unfound name.

    Args:
        category_names: A list of category names (strings).
        facets_config: An instance of FacetsConfig (defaults to the global 'config').

    Returns:
        A list of category IDs (strings) corresponding to the successfully
        matched category names.  Category names that could not be matched are skipped.
        Returns an empty list if no category names in the input list are matched.
    """
    category_ids = []
    category_name_to_id_map = facets_config.category_name_to_id_map

    for name in category_names:
        category_id = category_name_to_id_map.get(name)  # Use .get() for safe lookup
        if category_id:
            category_ids.append(category_id)
        else:
            print(
                f"Warning: Category name '{name}' not found in configured categories and will be ignored."
            )
            # Now, just ignore and continue to the next category

    return category_ids  # Return IDs of successfully matched categories


if __name__ == "__main__":
    # Example usage and testing
    test_category_names = [
        "レディース",
        "メンズ",
        "家電・スマホ・カメラ",
        "ファッション",
        "NonExistentCategory",
    ]

    matched_ids = map_category_names_to_ids(test_category_names)

    print("Category Names:", test_category_names)
    print("Matched Category IDs (relaxed matching):", matched_ids)
