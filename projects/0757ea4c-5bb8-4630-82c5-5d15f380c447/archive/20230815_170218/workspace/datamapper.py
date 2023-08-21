from formula import Formula

class DataMapper:
    def __init__(self, data_mapping):
        self.data_mapping = data_mapping

    def map(self, input_data):
        output_data = {}
        for key, mapping in self.data_mapping.items():
            value = input_data
            for part in mapping['input']['path'].split('.'):
                value = value[part]
            for formula in mapping['input'].get('formulas', []):
                value = Formula(formula).execute(value)
            output_data[key] = value
        return output_data
