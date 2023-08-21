class DataMapper:
    def __init__(self, mapping):
        self.mapping = mapping

    def map(self, data):
        mapped_data = {}
        for key, value in self.mapping.items():
            mapped_data[key] = data.get(value)
        return mapped_data
