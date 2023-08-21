def ifthen(input_value, condition, then_value, else_value):
    return then_value if input_value == condition else else_value

def substring(input_value, starting_index, ending_index):
    return input_value[starting_index:ending_index]

def prepend(input_value, prepend_value):
    return prepend_value + input_value

def division(input_value, divisor):
    return input_value / divisor
