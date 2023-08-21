def if_then(value):
    # Implement the "If, then" formula
    if value['if']:
        return value['then']
    else:
        return value['else']

def substring(value):
    # Implement the "Substring" formula
    return value['value'][value['startingIndex']:value['endingIndex']]

def prepend(value):
    # Implement the "Prepend" formula
    return value['prepend'] + value['value']

formulas = {
    'ifthen': if_then,
    'substring': substring,
    'prepend': prepend
}
