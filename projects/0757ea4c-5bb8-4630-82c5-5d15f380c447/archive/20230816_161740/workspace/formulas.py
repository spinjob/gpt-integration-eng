def ifthen(value, ifThen):
    for condition in ifThen:
        if condition['if']['condition'] == 'equals' and value == condition['if']['value']:
            return condition['then']['value']
        else:
            return condition['else']['value']

def substring(value, startingIndex, endingIndex):
    return value[startingIndex:endingIndex]

def prepend(value, prepend):
    return prepend + value

def division(value, division):
    return value / division
