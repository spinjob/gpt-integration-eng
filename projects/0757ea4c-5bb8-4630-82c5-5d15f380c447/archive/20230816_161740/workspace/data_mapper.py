import formulas

class DataMapper:
    def map(self, source_data, mapping_json):
        target_data = {}
        for key, mapping in mapping_json.items():
            value = self.get_value(source_data, mapping['input'])
            for formula in mapping['input'].get('formulas', []):
                value = getattr(formulas, formula['formula'])(value, **formula['inputs'])
            self.set_value(target_data, mapping['output'], value)
        return target_data

    def get_value(self, data, input):
        keys = input['sourcePath'].split('.')
        for key in keys:
            data = data[key]
        return data

    def set_value(self, data, output, value):
        keys = output['targetPath'].split('.')
        for key in keys[:-1]:
            data = data.setdefault(key, {})
        data[keys[-1]] = value
