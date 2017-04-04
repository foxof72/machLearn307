import math
from nominalOps import classifer


def avg(attr):
    summation = 0
    for vals in attr:
        summation = vals + summation
    return summation / len(attr)


def sigma(attr, mean):
    variance = sum([pow(val - mean, 2) for val in attr]) / float(len(attr) - 1)
    return math.sqrt(variance)


def pdf(x, mean, stdev):
    exponent = math.exp(-(math.pow(x - mean, 2) / (2 * math.pow(stdev, 2))))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent


def numeric_value(attributeToUse, list_of_numerics, input_x):
    list_yes, list_no, list_tot = classifer(list_of_numerics)
    attr = list_yes[attributeToUse]
    mean_yes = avg(attr)
    stdev_yes = sigma(attr, mean_yes)
    yesPDF = pdf(input_x, mean_yes, stdev_yes)
    attr = list_no[attributeToUse]
    mean_no = avg(attr)
    stdev_no = sigma(attr, mean_no)
    noPDF = pdf(input_x, mean_no, stdev_no)
    return yesPDF, noPDF
