class DataMapper:
    def map_data(self, data, mapping):
        # Map the data according to the mapping and return the result
        result = {}
        for key, value in mapping.items():
            result[key] = data.get(value)
        return result
