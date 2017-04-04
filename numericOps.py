import math
from algorithm_code import classifer

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

def numeric_value(list_of_numerics, input_x):
    probs_yes = []
    probs_no = []
    list_yes, list_no, list_tot = classifer(list_of_numerics)
    index = 0
    for attr in list_yes:
        print str(attr)
        probs_yes[index] = 1
        mean_yes = avg(attr)
        stdev_yes = sigma(attr, mean_yes)
        print mean_yes
        print stdev_yes
        x = input_x[index]
        probs_yes[index] = pdf(x, mean_yes, stdev_yes)
        print probs_yes[index]
        index += 1

    index = 0
    for attr in list_no:
        print str(attr)
        probs_no[index] = 1
        mean_no = avg(attr)
        stdev_no = sigma(attr, mean_no)
        print mean_no
        print stdev_no
        x = input_x[index]
        probs_no[index] = pdf(x, mean_no, stdev_no)
        print probs_no[index]
        index += 1
    return probs_yes, probs_no