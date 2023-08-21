class DataMapper:
    def __init__(self):
        pass

    def map_data(self, mapping_instructions, data):
        mapped_data = {}
        for key, value in mapping_instructions.items():
            mapped_data[key] = data.get(value)
        return mapped_data
