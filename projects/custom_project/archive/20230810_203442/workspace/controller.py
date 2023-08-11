class Controller:
    def process_data(self, data):
        # For simplicity, let's assume the processing involves filtering out data items where value is None
        return [item for item in data if item['value'] is not None]
