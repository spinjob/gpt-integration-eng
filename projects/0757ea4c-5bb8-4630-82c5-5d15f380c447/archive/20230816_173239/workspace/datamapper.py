class DataMapper:
    def map_data(self, data, mapping):
        mapped_data = {}
        for key, value in mapping.items():
            mapped_data[key] = data.get(value)
        return mapped_data
