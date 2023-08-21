class DataMapping:
    def __init__(self, mapping_json):
        self.mapping_json = mapping_json

    def map_data(self, source_data):
        mapped_data = {}
        for key, mapping in self.mapping_json.items():
            source_value = self.get_value_from_path(source_data, mapping['input']['path'])
            if 'formulas' in mapping['input']:
                for formula in mapping['input']['formulas']:
                    source_value = self.apply_formula(source_value, formula)
            self.set_value_in_path(mapped_data, mapping['output']['path'], source_value)
        return mapped_data

    def get_value_from_path(self, data, path):
        parts = path.split('.')
        for part in parts:
            data = data[part]
        return data

    def set_value_in_path(self, data, path, value):
        parts = path.split('.')
        for part in parts[:-1]:
            data = data.setdefault(part, {})
        data[parts[-1]] = value

    def apply_formula(self, value, formula):
        if formula['formula'] == 'ifthen':
            condition = formula['inputs']['ifThen'][0]['if']
            if value == condition['value']:
                return formula['inputs']['ifThen'][0]['then']['value']
            else:
                return formula['inputs']['ifThen'][0]['else']['value']
        elif formula['formula'] == 'substring':
            return value[formula['inputs']['substring']['startingIndex']:formula['inputs']['substring']['endingIndex']]
        elif formula['formula'] == 'prepend':
            return formula['inputs']['prepend'] + value
        elif formula['formula'] == 'division':
            return value / formula['inputs']['division']
        else:
            return value
