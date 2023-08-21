def ifthen(input_data, ifThen):
    for condition in ifThen:
        if input_data == condition['if']['value']:
            return condition['then']['value']
    return condition['else']['value']

def substring(input_data, startingIndex, endingIndex):
    return input_data[startingIndex:endingIndex]

def prepend(input_data, prepend):
    return prepend + input_data

def division(input_data, division):
    return input_data / division
