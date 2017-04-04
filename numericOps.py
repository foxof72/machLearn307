import math

def avg(attr):
    summation = 0
    for vals in attr:
        summation = vals + summation
    return summation / len(attr)


def sigma(attr, mean):
    variance = sum([pow(val - mean, 2) for val in attr]) / float(len(attr) - 1)
    return math.sprt(variance)


def pdf(x, mean, stdev):
    exponent = math.exp(-(math.pow(x - mean, 2) / (2 * math.pow(stdev, 2))))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent