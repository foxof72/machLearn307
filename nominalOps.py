def getYN(listOfInstances):
    # print listOfInstances
    yesCounter = 0
    noCounter = 0
    for i in range(0, len(listOfInstances)):
        yesNo = listOfInstances[i][30]  # warning: hard coded for 30 attributes
        # print "yes/no: " + yesNo
        if yesNo == "yes\n":
            # print "yes if"
            yesCounter += 1
        elif yesNo == "no\n":
            # print "no if"
            noCounter += 1
    # print "yes seperate function: " + str(yesCounter)
    # print "no serperate function: " + str(noCounter)
    return yesCounter, noCounter

def classifer(listOfInstances):
    listOfAttributes = []
    listOfYes = []
    listOfNo = []
    numAttr = len(listOfInstances[1])  # this is a variable for the # of attributes
    for k in range(numAttr):  # runs through the attributes
        attributeValues = {}
        attributeValuesYes = {}
        attributeValuesNo = {}
        for j in range(len(listOfInstances)):  # runs through the instances
            # print "yes or no:" + getYN(listOfInstances)
            # attributeValues = defaultdict(int)
            # print(listOfInstances[j][k])
            # print("This is if the instance is yes or no")
            # print(listOfInstances[j][numAttr-1])
            currentValue = listOfInstances[j][k]
            if "yes" in listOfInstances[j][
                        numAttr - 1]:  # == "yes\n": #TODO: we can change all of these cases to be "yes" in ________ because then we can be dynamic about what class we are trying to produce
                # print ("YES CASE")
                if currentValue in attributeValuesYes:
                    attributeValuesYes[currentValue] += 1
                    attributeValues[currentValue] += 1
                # print(attributeValuesYes[currentValue])
                elif currentValue not in attributeValues:
                    attributeValuesYes[currentValue] = 1
                    attributeValues[currentValue] = 1
                # print(attributeValuesYes[currentValue])
                else:
                    attributeValuesYes[currentValue] = 1
                    attributeValues[currentValue] += 1
            elif "no" in listOfInstances[j][numAttr - 1]:  # == "no\n":
                # print ("NO CASE")
                if currentValue in attributeValuesNo:
                    attributeValuesNo[currentValue] += 1
                    attributeValues[currentValue] += 1
                elif currentValue not in attributeValues:
                    attributeValuesNo[currentValue] = 1
                    attributeValues[currentValue] = 1
                else:
                    attributeValuesNo[currentValue] = 1
                    attributeValues[currentValue] += 1
        listOfAttributes.append(attributeValues)
        listOfYes.append(attributeValuesYes)
        listOfNo.append(attributeValuesNo)

    return listOfYes, listOfNo, listOfAttributes  # added two return values; yesCounter noCounter