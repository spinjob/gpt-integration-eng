import pandas as pd

class DataProcessor:
    def process_data(self, data):
        df = pd.DataFrame(data)
        processed_data = df.describe()  # Perform some basic statistical analysis
        return processed_data.to_dict()
