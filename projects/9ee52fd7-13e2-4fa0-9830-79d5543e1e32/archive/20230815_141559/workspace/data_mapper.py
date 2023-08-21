class DataMapper:
    def map_data(self, data, mapping):
        # Map data according to provided JSON
        output = {}
        for key, value in mapping.items():
            output[key] = data[value['input']['sourcePath']]
        return output
