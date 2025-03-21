from internal.parameter_matching.facets_config import config
from internal.utils.constants import ENG_TO_JPN_CATEGORY_MAP


class ParameterMatcher:
    def __init__(self, config=config):
        self.config = config

    def match_category_names_to_ids(self, extracted_category_names):
        """
        Matches extracted category names (English or Japanese) to Mercari category IDs using facets_config.
        Attempts to translate English category names to Japanese before matching.
        Returns IDs for successfully matched categories, ignores unmatched ones. (Relaxed Matching)

        Args:
            extracted_category_names: A list of category names (strings) extracted by the LLM.

        Returns:
            A list of Mercari category IDs (integers) corresponding to the valid matched category names.
            Returns a list of IDs for categories that *were* successfully matched (can be empty if no matches).
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
                    f"Warning: Extracted category name '{extracted_name}' (or its English version) does not perfectly match valid Mercari categories and will be ignored."
                )
                # Now, just ignore and continue to the next category, instead of returning empty list

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
