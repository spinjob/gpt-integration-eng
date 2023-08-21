class DataMapper:
    def map_data(self, source_data, mapping_json):
        # Initialize the target data
        target_data = {}

        # Iterate over the mapping JSON
        for key, value in mapping_json.items():
            # Extract the source and target paths
            source_path = value["input"]["path"]
            target_path = value["output"]["path"]

            # Replace the placeholders in the paths
            source_path = source_path.replace("{{categoryId}}", "test-category-id")
            target_path = target_path.replace("{{categoryId}}", "test-category-id")

            # Map the data
            target_data[target_path] = source_data[source_path]

        return target_data
