#Anthony Green's changes
import math
def avg(attr):
    summation = 0
    for vals in attr:
        summation = vals + summation
    return summation/len(attr)

def sigma(attr, mean):
    variance = sum([pow(val - mean, 2) for val in attr]) / float(len(attr) - 1)
    return math.sqrt(variance)

def pdf(x, mean, stdev):
    exponent = math.exp(-(math.pow(x - mean, 2) / (2 * math.pow(stdev, 2))))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent

def numeric_value(list_of_numerics, input_x):
    probs = {}
    index = 0
    for attr in list_of_numerics:
        #print str(index)
        print str(attr)
        probs[index] = 1
        #i = 0
        #while i < len(list_of_numerics):
        mean = avg(attr)
        stdev = sigma(attr, mean)
        print mean
        print stdev
        x = input_x[index]
        probs[index] = pdf(x, mean, stdev)
        print probs[index]
        index += 1
        #i += 1
    return probs

#Test code
summaries = [[19, 20, 21], [19, 20, 21]]
inputVector = [20, 25]
probabilities = numeric_value(summaries, inputVector)
print "Probabilites " + str(probabilities)