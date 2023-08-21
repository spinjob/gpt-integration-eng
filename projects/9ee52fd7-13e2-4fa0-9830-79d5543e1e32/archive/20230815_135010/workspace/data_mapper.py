import json

class DataMapper:
    def map_data(self, data):
        # Load the mapping JSON
        with open('mapping.json') as f:
            mapping = json.load(f)

        # Map the data according to the mapping JSON
        mapped_data = {}
        for key, value in mapping.items():
            mapped_data[key] = data[value['sourcePath']]

        return mapped_data
