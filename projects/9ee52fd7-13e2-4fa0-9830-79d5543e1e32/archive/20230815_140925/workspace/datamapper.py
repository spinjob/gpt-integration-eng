class DataMapper:
    def __init__(self, mapping_json):
        self.mapping_json = mapping_json

    def map_data(self, data, source):
        mapped_data = {}
        for key, value in self.mapping_json.items():
            if value['input']['in'] == source:
                mapped_data[value['output']['outputPath']] = data[value['input']['sourcePath']]
        return mapped_data
