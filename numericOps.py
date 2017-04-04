import math
import statistics
from nominalOps import classifer


def sortNumeric(attribute_type_list,listOfInstances):  # the attribute_type_list[[attributename, attribute_type
    # this function takes the sorting above and separates the values into numeric and nominal temp lists before pushing the whole instance into the greater list
    numAttr = len(listOfInstances[1])
    #nominalInstanceList = []
    numericInstanceList = []

    for i in range(len(listOfInstances)):  # this is the instances
        temp_numeric = []  # these are created so that the intances are still separated for our yes/no classifying function
        #temp_nominal = []

        for j in range(numAttr):  # this is the attributes
            if attribute_type_list[j] == "numeric":  # this is to create the numerical list
                temp_numeric.append(float(listOfInstances[i][j]))  # this is taking the instance value and the attribute and appending it to the temp list
            if attribute_type_list[j] == "nominal":  # this is to create the nominal list
                temp_numeric.append(31415) # this is taking the instance value and the attribute and appending it to the list
                if (listOfInstances[i][j] == "yes\n" or listOfInstances[i][j] == "no\n"):
                    temp_numeric.append(listOfInstances[i][j])  # this is to provide for the case that yes/ no is nominal but should still be appended to the numeric
        numericInstanceList.append(temp_numeric)  # this is taking the instance value and the attribute and appending it to the list
        #nominalInstanceList.append(
         #   temp_nominal)  # this is taking the instance value and the attribute and appending it to the list
    # print("this is the numeric instance list")

    # print(numericInstanceList)
    # print("this is a nominal instance list")
    # print(nominalInstanceList)

    return numericInstanceList


def classiferNumeric(listOfInstances):
	print (listOfInstances)
	listOfAttributes = []
	listOfYes = []
	listOfNo = []
	numAttr = len(listOfInstances[1])  # this is a variable for the # of attributes
	for k in range(numAttr-1):  # runs through the attributes
        #attributeValues = {}
		
		attributeValuesYes = []
		attributeValuesNo = []
		
		
		for j in range(len(listOfInstances)):  # runs through the instances
			
			currentValue = listOfInstances[j][k]
			if "yes" in listOfInstances[j][numAttr - 1]  :
				# == "yes\n": #TODO: we can change all of these cases to be "yes" in ________ because then we can be dynamic about what class we are trying to produce
				print("This is what you got currently")
				print(attributeValuesYes)
				if listOfInstances[j][k] != 31415:
					attributeValuesYes.append(float(currentValue))
			elif "no" in listOfInstances[j][numAttr - 1]  :  # == "no\n":
				if listOfInstances[j][k] != 31415:
						
						attributeValuesNo.append(float(currentValue))
               
		listOfYes.append(attributeValuesYes)
		
		listOfNo.append(attributeValuesNo)
	print("this is list of yes")
	print(listOfYes)
	print("this is list of no")
	print(listOfNo)
	return listOfYes, listOfNo
	
def forAttributesSelected(instancesForClassification):
	for i in range(len(instancesForClassification)):
		print(instancesForClassification[i][0])

def avg(attr):
	masterList = []
	for vals in range(0, len(attr)):
		print (attr[vals].keys())
		dictSum = attr[vals].keys()
	for i in range(0, len(dictSum)):
		for j in range(0, len(dictSum[i])):
			intCast = attr()
			masterList.append()
	#print "avg: " + str(float(summation / len(attr)))
	return #why don't you return the average here 

	
def avg2(attr): #where attribute is passing a list from within a list from the numeric classifier 
	
	length = len(attr)
	total = 0
	for i in range(length):
		total = attr[i] +total
		print ("Happy")
	avg = total/length
	print(avg)
	return avg
	
		

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
