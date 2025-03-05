from internal.parameter_matching.facets_config import config
from internal.utils.constants import ENG_TO_JPN_CATEGORY_MAP


class ParameterMatcher:
    """
    Matches extracted parameter names (like category names) to their corresponding IDs
    using configuration data (e.g., from FacetsConfig) and translation maps.
    """

    def __init__(self, config=config):
        """
        Initializes ParameterMatcher with a FacetsConfig instance.

        Args:
            config: A FacetsConfig instance providing access to facet data (e.g., categories).
                    Defaults to the globally initialized 'config' from facets_config.py.
        """
        self.config = config

    def match_category_names_to_ids(self, extracted_category_names):
        """
        Matches extracted category names (English or Japanese) to Mercari category IDs.

        Attempts to translate English category names to Japanese before matching.
        Returns IDs for successfully matched categories, ignoring unmatched ones (relaxed matching).

        Warning: Category name matching is case-sensitive against Japanese category names
        from the configuration. English to Japanese translation is case-insensitive for lookup.

        Args:
            extracted_category_names: A list of category names (strings) extracted by the LLM.

        Returns:
            A list of Mercari category IDs (strings) corresponding to the valid matched category names.
            Returns an empty list if no categories are successfully matched.
        """
        matched_category_ids = []
        category_name_to_id_map = self.config.category_name_to_id_map

        for extracted_name in extracted_category_names:
            japanese_name = ""
            category_name = (
                extracted_name  # Default to extracted name if no match found
            )
            lower_category_name = category_name.lower()
            if lower_category_name in ENG_TO_JPN_CATEGORY_MAP:
                japanese_name = ENG_TO_JPN_CATEGORY_MAP[
                    lower_category_name
                ]  # Translate English to Japanese

            if japanese_name in category_name_to_id_map:
                matched_category_ids.append(category_name_to_id_map[japanese_name])
            else:
                print(
                    f"Warning: Extracted category name '{extracted_name}' (Japanese: '{japanese_name if japanese_name else 'N/A' }') does not perfectly match valid Mercari categories and will be ignored."
                )
                # Ignore and continue to the next category, instead of returning empty list

        return matched_category_ids  # Return IDs of successfully matched categories, even if some were not matched


# Initialize ParameterMatcher
parameter_matcher = ParameterMatcher()

if __name__ == "__main__":
    # Example usage and testing
    matcher = ParameterMatcher()

    # Test cases - now including English category names that SHOULD be translated and matched
    test_category_names = [
        "レディース",
        "メンズ",
        "家電・スマホ・カメラ",
        "ファッション",
        "NonExistentCategory",
        "electronics & gadgets",
        "Fashion",
    ]

    matched_ids = matcher.match_category_names_to_ids(test_category_names)

    print("Extracted Category Names:", test_category_names)
    print(
        "Matched Category IDs (relaxed matching):", matched_ids
    )  # Indicate relaxed matching in output
