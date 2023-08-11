import pandas as pd

class DataProcessor:
    def process_data(self, data):
        df = pd.DataFrame(data)
        processed_data = df.describe()
        return processed_data
