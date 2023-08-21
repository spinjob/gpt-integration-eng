class Formula:
    def __init__(self, formula):
        self.formula = formula

    def execute(self, value):
        if self.formula['name'] == 'If, then':
            condition = self.formula['inputs']['ifThen'][0]
            if value == condition['if']['value']:
                return condition['then']['value']
            else:
                return condition['else']['value']
        elif self.formula['name'] == 'Substring':
            return value[int(self.formula['inputs']['substring']['startingIndex']):int(self.formula['inputs']['substring']['endingIndex'])]
        elif self.formula['name'] == 'Prepend':
            return self.formula['inputs']['prepend'] + value
        elif self.formula['name'] == 'Division':
            return value / int(self.formula['inputs']['division'])
