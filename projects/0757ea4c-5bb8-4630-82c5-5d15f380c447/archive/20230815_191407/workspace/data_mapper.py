import json

class DataMapper:
    def map(self, source_data, mapping_file):
        with open(mapping_file) as f:
            mapping = json.load(f)
        target_data = {}
        for key, value in mapping.items():
            target_data[key] = source_data[value['sourcePath']]
        return target_data
