def apply_formula(formula, input_data):
    if formula['name'] == 'If, then':
        return if_then(formula['inputs']['ifThen'][0], input_data)
    elif formula['name'] == 'Substring':
        return substring(formula['inputs']['substring'], input_data)
    elif formula['name'] == 'Prepend':
        return prepend(formula['inputs']['prepend'], input_data)
    elif formula['name'] == 'Division':
        return division(formula['inputs']['division'], input_data)

def if_then(formula, input_data):
    if input_data == formula['if']['value']:
        return formula['then']['value']
    else:
        return formula['else']['value']

def substring(formula, input_data):
    return input_data[formula['startingIndex']:formula['endingIndex']]

def prepend(formula, input_data):
    return formula['prepend'] + input_data

def division(formula, input_data):
    return input_data / formula['division']
