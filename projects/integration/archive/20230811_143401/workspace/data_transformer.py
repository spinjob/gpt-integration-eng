class DataTransformer:
    def transform(self, data):
        transformed_data = {
            'categories': data['categories'],
            'modifierGroups': data['modifierGroups']
        }
        return transformed_data
