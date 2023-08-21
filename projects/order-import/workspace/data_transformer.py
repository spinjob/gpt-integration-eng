class DataTransformer:
    def transform(self, data):
        transformed_data = {}
        for category_id, category in data['categories'].items():
            transformed_data['categories.' + category_id] = category
        for modifier_group_id, modifier_group in data['modifierGroups'].items():
            transformed_data['modifierGroups.' + modifier_group_id] = modifier_group
        return transformed_data
