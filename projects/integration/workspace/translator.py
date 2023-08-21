class Translator:
    def translate(self, data):
        # Translate the data according to the mapping table
        translated_data = {
            'categories': {categoryId: data['categories'][categoryId] for categoryId in data['categories']},
            'modifierGroups': {modifierGroupId: data['modifierGroups'][modifierGroupId] for modifierGroupId in data['modifierGroups']}
        }

        # Return the translated data
        return translated_data
