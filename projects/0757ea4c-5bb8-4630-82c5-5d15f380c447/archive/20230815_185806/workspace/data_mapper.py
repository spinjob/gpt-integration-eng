import json
from formulas import apply_formula

class DataMapper:
    def map_trigger_data(self, data):
        with open('trigger_data_mapping.json') as f:
            mapping = json.load(f)
        return self._map_data(data, mapping)

    def _map_data(self, data, mapping):
        mapped_data = {}
        for key, value in mapping.items():
            input_data = data[value['input']['sourcePath']]
            if 'formulas' in value['input']:
                for formula in value['input']['formulas']:
                    input_data = apply_formula(formula, input_data)
            mapped_data[value['output']['path']] = input_data
        return mapped_data
