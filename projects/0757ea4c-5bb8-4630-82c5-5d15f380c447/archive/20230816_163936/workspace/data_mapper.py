import formulas

class DataMapper:
    def map_data(self, source_data, mapping):
        target_data = {}
        for key, value in mapping.items():
            input_data = self._get_data(source_data, value['input'])
            for formula in value['input'].get('formulas', []):
                input_data = getattr(formulas, formula['name'])(input_data, **formula['inputs'])
            self._set_data(target_data, value['output'], input_data)
        return target_data

    def _get_data(self, data, path_info):
        data = data[path_info['in']]
        for key in path_info['path'].split('.'):
            data = data[key]
        return data

    def _set_data(self, data, path_info, value):
        keys = path_info['path'].split('.')
        for key in keys[:-1]:
            if key not in data:
                data[key] = {}
            data = data[key]
        data[keys[-1]] = value
