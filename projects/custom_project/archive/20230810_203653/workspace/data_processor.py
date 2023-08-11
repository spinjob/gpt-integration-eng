from dataclasses import dataclass

@dataclass
class Data:
    id: int
    value: str

def process_data(raw_data):
    processed_data = [Data(id=item['id'], value=item['value']) for item in raw_data]
    return processed_data
