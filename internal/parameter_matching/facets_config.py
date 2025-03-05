import json
import os
from typing import Dict, List, Optional


class FacetsConfig:
    """
    Loads and provides access to category data from a JSON file.
    """

    def __init__(self, categories_file_path: str) -> None:
        """
        Initializes FacetsConfig with the path to the categories JSON file.

        Args:
            categories_file_path: Path to the categories JSON file.
        """
        self.categories_file: str = categories_file_path
        self.category_name_to_id_map: Dict[str, str] = self._load_category_data()

    def _load_category_data(self) -> Dict[str, str]:
        """
        Loads category data from the specified JSON file and creates a name-to-id map.

        Returns:
            A dictionary mapping category names to category IDs.
        """
        category_name_to_id_map: Dict[str, str] = {}
        try:
            with open(self.categories_file, "r", encoding="utf-8") as f:
                categories_data = json.load(f)
                if categories_data and "data" in categories_data:

                    def process_category_list(category_list):
                        for category_item in category_list:
                            category_name_to_id_map[category_item["name"]] = (
                                category_item["id"]
                            )
                            if "child" in category_item:
                                process_category_list(category_item["child"])

                    process_category_list(categories_data["data"])
                else:
                    print(
                        f"Warning: '{self.categories_file}' does not have expected 'data' structure."
                    )
        except FileNotFoundError:
            print(f"Error: '{self.categories_file}' file not found.")
        except json.JSONDecodeError:
            print(
                f"Error: Could not decode '{self.categories_file}'. File might be corrupted."
            )
        return category_name_to_id_map

    def get_valid_category_names(self) -> List[str]:
        """
        Returns a list of valid category names loaded from the configuration.
        """
        return list(self.category_name_to_id_map.keys())

    def get_category_id_by_name(self, category_name: str) -> Optional[str]:
        """
        Returns the category ID for a given category name.

        Args:
            category_name: The name of the category to look up.

        Returns:
            The category ID if found, otherwise None.
        """
        return self.category_name_to_id_map.get(category_name)


# Initialize FacetsConfig -  NOW with the file path argument!
default_categories_file_path = os.path.join(
    os.path.dirname(__file__), "..", "facets", "categories.json"  # Corrected path!
)
config = FacetsConfig(default_categories_file_path)

if __name__ == "__main__":
    # Example usage and testing
    example_config = FacetsConfig(
        default_categories_file_path
    )  # Use the same path here too

    print(
        "Valid Category Names (first 10):",
        list(example_config.get_valid_category_names())[:10],
    )
    print(
        "\nCategory ID for 'レディース':",
        example_config.get_category_id_by_name("レディース"),
    )
    print(
        "Category ID for 'NonExistentCategory':",
        example_config.get_category_id_by_name("NonExistentCategory"),
    )
