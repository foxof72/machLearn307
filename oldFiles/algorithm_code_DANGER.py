import os

from oldFiles.nominalOpsOld import *
from oldFiles.numericOpsOld import *

# Assumptions we assume that there will be either a space or at least still a comma division for a missing value
# we are assuming that the last attribute is a yes no value, and that this is the class that we are classifying for but we can change this
attribute_type_list = []
namesOfNominalClasses = []  # I made this a string
all_attribute_names = []
list_of_instances = []
attributes = []  # this will need to be added to their programs


def createListOfAttributes(attributes):
    for i in range(len(
            attributes) - 1):  # we can put this into a function but this creates a list of if the attributes are numeric and nominal
        if i > 1:
            parse_attribute = attributes[i]
            attribute_parts = parse_attribute.split(" ", 2)
            attribute_name = attribute_parts[1]
            attribute_type = attribute_parts[2]
            if "numeric" in attribute_type:
                attribute_type = "numeric"
                attribute_type_list.append(attribute_type)

            else:
                attribute_type = "nominal"
                attribute_type_list.append(attribute_type)
                namesOfNominalClasses.append(attribute_name)
            all_attribute_names.append(attribute_name)


def sortNominalAndNumeric(attribute_type_list,
                          listOfInstances):  # the attribute_type_list[[attributename, attribute_type
    # this function takes the sorting above and separates the values into numeric and nominal temp lists before pushing the whole instance into the greater list
    numAttr = len(listOfInstances[1])
    nominalInstanceList = []
    numericInstanceList = []

    for i in range(len(listOfInstances)):  # this is the instances
        temp_numeric = []  # these are created so that the intances are still separated for our yes/no classifying function
        temp_nominal = []

        for j in range(numAttr):  # this is the attributes
            if attribute_type_list[j] == "numeric":  # this is to create the numerical list
                temp_numeric.append(float(listOfInstances[i][
                                              j]))  # this is taking the instance value and the attribute and appending it to the temp list
            if attribute_type_list[j] == "nominal":  # this is to create the nominal list
                temp_nominal.append(listOfInstances[i][
                                        j])  # this is taking the instance value and the attribute and appending it to the list
                if (listOfInstances[i][j] == "yes\n" or listOfInstances[i][j] == "no\n"):
                    temp_numeric.append(listOfInstances[i][
                                            j])  # this is to provide for the case that yes/ no is nominal but should still be appended to the numeric
        numericInstanceList.append(
            temp_numeric)  # this is taking the instance value and the attribute and appending it to the list
        nominalInstanceList.append(
            temp_nominal)  # this is taking the instance value and the attribute and appending it to the list

    return numericInstanceList, nominalInstanceList


def fractionGenerator(attribute, yesList, noList, yesTotal, numericList, noTotal):
    print ("start generation: ")
    print ("yesTotal: " + str(yesTotal))
    print ("noTotal: " + str(noTotal))
    try:
        float(attribute[1])
        yesPDF, noPDF = numeric_value(attribute[0], numericList, attribute[1])
        return yesPDF, noPDF
    except ValueError as e:
        yesDic = yesList[attribute[0]]
        noDic = noList[attribute[0]]
        print (yesDic)
        print (noDic)
        numYes = float(yesDic[attribute[1]])
        print ("numYes: " + str(numYes))
        numNo = float(noDic[attribute[1]])
        print ("numNo: " + str(numNo))
        yesFraction = float(numYes / yesTotal)
        noFraction = float(numNo / noTotal)
        print ("yesFraction: " + str(yesFraction))
        print ("noFraction: " + str(noFraction))
        return (yesFraction, noFraction)


def findStats(listOfKeys, yesList, noList, yesTotal, numericList, noTotal):
    noFrac = []  # all the fractions to be multiple together for no
    yesFrac = []  # all the fractions to be multiple for yes
    print ("\n\n")
    print ("find stats yes total: " + str(yesTotal))
    print ("find stats no total: " + str(noTotal))
    yesTotal = float(yesTotal)
    noTotal = float(noTotal)
    yes = float(yesTotal / (yesTotal + noTotal))
    no = float(noTotal / (yesTotal + noTotal))
    print ("total yes odds: " + str(yes))
    print ("total no odds: " + str(no))
    print ("\n\n")
    for i in range(0, len(listOfKeys)):  # this for loop loads the lists with fractions for calculations
        yesOdd, noOdd = fractionGenerator(listOfKeys[i], yesList, noList, yesTotal, numericList, noTotal)
        print ("\n\n")
        yesFrac.append(yesOdd)
        noFrac.append(noOdd)
    yesFrac.append(yes)
    noFrac.append(no)
    yesChance = yesFrac[0]
    print ("yesChance: " + str(yesChance))
    noChance = noFrac[0]
    print ("noChance: " + str(noChance))
    for j in range(1, len(yesFrac)):  # does yes calculation
        yesChance = float(yesChance * yesFrac[j])
    for x in range(1, len(noFrac)):  # does no calculation
        noChance = float(noChance * noFrac[x])
    # now normalize
    print ("noChance later: " + str(noChance))
    print ("yesChance later: " + str(yesChance))
    yesNormal = yesChance / (yesChance + noChance) * 100
    noNormal = noChance / (yesChance + noChance) * 100
    return yesNormal, noNormal


# end of John's calculation function
createListOfAttributes(attributes)
numericInstanceList, nominalInstanceList = sortNominalAndNumeric(attribute_type_list, list_of_instances)
# this code is for testing
numListYes, numListNo, numTotals = classifer(
    numericInstanceList)  # this is not working currently because yes\n and no\n are not in it
nomListYes, nomListNo, nomTotals = classifer(nominalInstanceList)

# print list_of_instances
outYes, outNo = getYN(list_of_instances)
# print "outYes: " + str(outYes)
# print "outNo: " + str(outNo)
# print(list_of_instances)
listYes, listNo, listTotals = classifer(list_of_instances)


# testList = [[0, 'GP'], [1, 'F'], [19, 'yes']]
# yes, no = findStats(testList, listYes, listNo, outYes, numericInstanceList, outNo)
# print ("\n\n ")
# print ("yes final: " + str(yes) + "%")
# print ("no final: " + str(no) + "%")


# print("This is the num list yes")
# print (numListYes)





# this is where you start editing
def userFacing(allAttributeList, AllListTotals, namesOfNominalClasses):
    instanceToBeClassified = []
    classNumber = ""
    print()
    print("What attribute would you like to classify on?")
    print("Select on your keyboard what attribute you would like to classify on: ")
    for i in range(len(namesOfNominalClasses)):
        name = str(namesOfNominalClasses[i])
        # if name in namesOfNominalClasses:
        print(str(i) + ": " + str(namesOfNominalClasses[i]))
    keyboardInput = input()
    while (int(keyboardInput) > len(namesOfNominalClasses) or int(keyboardInput) < 0):
        keyboardInput = input("Sorry, that was out of range. Please insert another number:")
    classifyBy = namesOfNominalClasses[int(keyboardInput)]  # this is where you get what you classify by
    print("You are classifying on " + classifyBy + ".")
    for i in range(len(allAttributeList)):
        if classifyBy == str(allAttributeList[i]):
            classNumber = i
            break

    print("Sweet! Now let's create an instance to classify:")
    for j in range(len(allAttributeList)):
        attrChoices = str(AllListTotals[j])
        tempChoices = attrChoices.split("'")
        # print(tempChoices)
        choices = []
        for i in range(len(tempChoices)):
            if ((i % 2) != 0):
                choices.append(tempChoices[i])
        # print(tempChoices[i])
        print("Please select what you would like to classify on for " + allAttributeList[j] + ": (or -1 to exit)")
        for i in range(len(choices)):
            print(str(i) + ": " + choices[i])
        choice = input()
        if choice == -1:
            break
        while (int(choice) > len(choices) - 1 or int(choice) < 0):
            choice = input("Sorry, that option is out of range:")
        choice = int(choice)
        temp_attribute = [choice, choices[choice]]
        instanceToBeClassified.append(temp_attribute)

    return instanceToBeClassified


print("Welcome to the HAJ NaiveBayes Algorithm")
print("Please enter the name of of an arff file that is present in the folder that you are running this program in:")

file_name = "smallData.arff"
print ("The File that you requested is " + file_name)


def split_instances(data):
    print("This is you calling split instances")


checkexists = os.path.isfile(file_name)
print("Does the file exist? " + str(checkexists))

while checkexists == False:
    print (
        "Sorry, but it seems like your file does not exist in this folder. Please double check your spelling and try again.")
    print("Hint: Don't foget to put the document type extension.")
    file_name = input("File Name: ")
    print ("The File that you requested is " + file_name)
    checkexists = os.path.isfile(file_name)
    print("Does the file exits" + str(checkexists))  # can remove this later

datavarcheck = "@data"
datasection = False
file = open(file_name, "r")

while True:
    # print(data)
    data = file.readline()
    if not data:
        break
    # print ("this is before the if @data statement")
    if '@data' in data:
        datasection = True
        data = file.readline()  # add this to code

    # print("did you get here") #this if statment is not picking it up @data, it think it has something to do with reading lines
    if data != None and datasection is True:
        instance = data.split(",")

        list_of_instances.append(instance)

    # this appends to the greater list of instances
    # print("this is the list of instances")
    # print(list_of_instances)
    if datasection is False:
        attributes.append(data)  # this will need to be added to their programs
        # print(
        # "What attribute would you like to classify your instance on?")  # assumption that it must be a yes or no class, but this does not necessarly need to be the case
        # if we get things working then we can have it create a variable and take the values of that class and we can put that variable in our if statements



        # ToDo: have the user select what class they want to classify on
        # ToDo: here is where you should have a question and answer setting for what attributes it wants to classify an instance on

# MAIN
createListOfAttributes(attributes)
numericInstanceList, nominalInstanceList = sortNominalAndNumeric(attribute_type_list, list_of_instances)
numListYes, numListNo, numTotals = classifer(numericInstanceList)
nomListYes, nomListNo, nomTotals = classifer(nominalInstanceList)
listYes, listNo, listTotals = classifer(list_of_instances)
outYes, outNo = getYN(list_of_instances)
testList = [[0, 'GP'], [1, 'F'], [7, 4]]
yes, no = findStats(testList, listYes, listNo, outYes, numericInstanceList, outNo)
print ("\n\n ")
print ("yes final: " + str(yes) + "%")
print ("no final: " + str(no) + "%")


# print("This is the num list yes")
# print (numListYes)




# this is where you start editing
def userFacing(allAttributeList, AllListTotals, namesOfNominalClasses):
    instanceToBeClassified = []
    classNumber = ""
    print()
    print("What attribute would you like to classify on?")
    print("Select on your keyboard what attribute you would like to classify on: ")
    for i in range(len(namesOfNominalClasses)):
        name = str(namesOfNominalClasses[i])
        # if name in namesOfNominalClasses:
        print(str(i) + ": " + str(namesOfNominalClasses[i]))
    keyboardInput = input()
    while (int(keyboardInput) > len(namesOfNominalClasses) or int(keyboardInput) < 0):
        keyboardInput = input("Sorry, that was out of range. Please insert another number:")
    classifyBy = namesOfNominalClasses[int(keyboardInput)]  # this is where you get what you classify by
    print("You are classifying on " + classifyBy + ".")
    for i in range(len(allAttributeList)):
        if classifyBy == str(allAttributeList[i]):
            classNumber = i
            break

    print("Sweet! Now let's create an instance to classify:")
    for j in range(len(allAttributeList)):
        attrChoices = str(AllListTotals[j])
        tempChoices = attrChoices.split("'")
        # print(tempChoices)
        choices = []
        for i in range(len(tempChoices)):
            if ((i % 2) != 0):
                choices.append(tempChoices[i])
        # print(tempChoices[i])
        print("Please select what you would like to classify on for " + allAttributeList[j] + ":")
        for i in range(len(choices)):
            print(str(i) + ": " + choices[i])

        choice = input()

        while (int(choice) > len(choices) - 1 or int(choice) < 0):
            choice = input("Sorry, that option is out of range:")

        # if int(choice) > len(choices) or int(choice) < 0:
        #	print("We are sorry, but that was out of range.")
        #	for i in range(len(choices)):
        #		print(str(i) + ": " + choices[i])
        #	choice = input()
        #	while(
        choice = int(choice)
        temp_attribute = [choice, choices[choice]]
        instanceToBeClassified.append(temp_attribute)

    return instanceToBeClassified


# print output
# print output
# end testing


# Anthony Green's changes
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


instanceForClassification = userFacing(all_attribute_names, listTotals, namesOfNominalClasses)
print(instanceForClassification)
yes, no = findStats(instanceForClassification, listYes, listNo, outYes, numericInstanceList, outNo)
print ("\n\n ")
print ("yes final: " + str(yes) + "%")
print ("no final: " + str(no) + "%")
exit(0)
