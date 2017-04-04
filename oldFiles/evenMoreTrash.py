import math
import statistics
from nominalOps import classifer


def avg(attr):
    masterList = []
    for vals in range(0, len(attr)):
        print (attr[vals].keys())
        dictSum = attr[vals].keys()
    for i in range(0, len(dictSum)):
        for j in range(0, len(dictSum[i])):
            intCast = attr()
            masterList.append()
    # print "avg: " + str(float(summation / len(attr)))
    return


def sigma(mean, listYN):
    masterList = []
    for vals in range(0, len(listYN)):
        tempList = listYN[vals].keys()
        masterList.append(tempList)
    statistics.variance(tempList, mean)
    return math.sqrt(listYN)
    # print "attrLen: " + str(len(attr))
    # print len(listYN)
    # print str(float(sum([pow(val - mean, 2) for val in listYN])))
    # variance = float(sum([pow(val - mean, 2) for val in listYN]) / float(len(listYN) - 1))
    # print "variance: " + str(variance)
    # return float(math.sqrt(variance))


def pdf(x, mean, stdev):
    print ("stdv: " + str(stdev))
    exponent = math.exp(-(math.pow(x - mean, 2) / (2 * math.pow(stdev, 2))))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent


def numeric_value(attributeToUse, list_of_numerics, input_x):
    list_yes, list_no, list_tot = classifer(list_of_numerics)
    attr = list_yes[attributeToUse]
    mean_yes = avg(list_yes)
    stdev_yes = sigma(mean_yes, list_yes)
    yesPDF = pdf(input_x, mean_yes, stdev_yes)
    print ("no start")
    print ("\n\n")
    print (len(list_no))
    attr = list_no[attributeToUse]
    mean_no = avg(list_no)
    stdev_no = sigma(mean_no, list_no)
    noPDF = pdf(input_x, mean_no, stdev_no)
    return yesPDF, noPDF
