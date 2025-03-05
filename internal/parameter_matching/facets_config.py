import json
import os


class FacetsConfig:
    categories_file_path = os.path.join(
        os.path.dirname(__file__), "facets", "categories.json"
    )

    def __init__(self, categories_file=categories_file_path):
        self.categories_file = categories_file
        self.category_name_to_id_map = self._load_category_data()

    def _load_category_data(self):
        """Loads category data from categories.json and creates a name-to-id map."""
        category_name_to_id_map = {}
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

    def get_valid_category_names(self):
        """Returns a list of valid category names."""
        return list(self.category_name_to_id_map.keys())

    def get_category_id_by_name(self, category_name):
        """Returns the category ID for a given category name, or None if not found."""
        return self.category_name_to_id_map.get(category_name)


# Initialize FacetsConfig - This will load category data when the module is imported
facets_config = FacetsConfig()

if __name__ == "__main__":
    # Example usage and testing
    config = FacetsConfig()
    print(
        "Valid Category Names (first 10):", list(config.get_valid_category_names())[:10]
    )
    print(
        "\nCategory ID for 'レディース':", config.get_category_id_by_name("レディース")
    )
    print(
        "Category ID for 'NonExistentCategory':",
        config.get_category_id_by_name("NonExistentCategory"),
    )
