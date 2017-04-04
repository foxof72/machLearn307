import os

print("Welcome to the HAJ 1R Algorithm")
print("Please enter the name of of an arff file that is present in the folder that you are running this program in:")

file_name = "smallData.arff"
print ("The File that you requested is " + file_name)


def split_instances(data):
    print("This is you calling split instances")


checkexists = os.path.isfile(file_name)
print("Does the file exits" + str(checkexists))

while checkexists == False:
    print (
    "Sorry, but it seems like your file does not exist in this folder. Please double check your spelling and try again.")
    print("Hint: Don't foget to put the document type extension.")
    file_name = input("File Name: ")
    print ("The File that you requested is " + file_name)
    checkexists = os.path.isfile(file_name)
    print("Does the file exits" + str(checkexists))  # can remove this later

list_of_instances = []
attributes = []  # this will need to be added to their programs
datavarcheck = "@data"
datasection = False
file = open(file_name, "r")
# attribute_list = []
nominalAttributes = []
numericAttributes = []

# whole_file = file.read()
# if '@data' in whole_file:
#	print ("Checking if @data is in the whole file")
# for data in file:
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
        # print("Your data is: " + data )
        # print (instance)
        list_of_instances.append(instance)
        # print(list_of_instances)
    # this appends to the greater list of instances
    # print("this is the list of instances")
    # print(list_of_instances)
    if datasection is False:
        attributes.append(data)  # this will need to be added to their programs

for i in range(len(attributes) - 1):

    if i > 1:

        parse_attribute = attributes[i]
        # print(parse_attribute)
        attribute_parts = parse_attribute.split(" ", 2)
        # print(attri	bute_parts)
        attribute_name = attribute_parts[1]
        attribute_type = attribute_parts[2]
        if "numeric" in attribute_type:
            attribute_type = "numeric"
            numericAttributes.append(attribute_name)
        else:
            attribute_type = "nominal"
            nominalAttributes.append(attribute_name)
# print("Nominal Attributes = ")
# print(nominalAttributes)
# print("Numeric Attributes = " )
# print(numericAttributes)



print(list_of_instances)

# this function checks to see if you've seen a value before or nah
def getYN(listOfInstances):
    for i in range(0, len(listOfInstances)):
        yesNo = listOfInstances[i][30]  # warning: hard coded for 30 attributes
        # print "yes/no: " + yesNo
        yesCounter = 0
        noCounter = 0
        return yesNo

def nominalClassifer(listOfInstances):
    listOfAttributes = []
    listOfYes = []
    listOfNo = []
    # for i in range(len(list_of_instances)): #runs through the instances
    # for i in range(0, len(listOfInstances)):
    #     yesNo = listOfInstances[i][30]  # warning: hard coded for 30 attributes
    #     # print "yes/no: " + yesNo
    #     yesCounter = 0
    #     noCounter = 0
    #     if yesNo == "yes":
    #         yesCounter += 1
    #     else:
    #         noCounter += 1
    for k in range(len(listOfInstances[1])):  # runs through the attributes
        attributeValues = {}
        attributeValuesYes = {}
        attributeValuesNo = {}
        for j in range(len(listOfInstances)):  # runs through the instances
            # print "yes or no:" + getYN(listOfInstances)
            # attributeValues = defaultdict(int)
            print(listOfInstances[j][k])
            print("This is if the instance is yes or no")
            print(listOfInstances[j][30])
            currentValue = listOfInstances[j][k]
            # print "currentValue: " + currentValue
            if currentValue in attributeValuesYes or currentValue in attributeValuesNo:
                # print "already in "
                print "30: " + listOfInstances[j][30]
                if listOfInstances[j][30] == "yes\n" and currentValue in attributeValuesYes:
                    print "yes already"
                    attributeValuesYes[currentValue] += 1
                elif currentValue in attributeValuesNo and listOfInstances[j][30] == "no\n":
                    print "no already"
                    attributeValuesNo[currentValue] += 1
                elif listOfInstances[j][30] == "no\n":
                    # this is the case if the attribute is already in attributevalues
                    attributeValuesNo[currentValue] = 1
                attributeValues[currentValue] += 1
            elif currentValue not in attributeValuesYes or currentValue not in attributeValuesNo:
                # print "not in"
                if listOfInstances[j][30] == "yes\n" and currentValue not in listOfYes:
                    print "yes new"
                    attributeValuesYes[currentValue] = 1
                    print "attrYes: " + str(attributeValuesYes)
                elif listOfInstances[j][30] == "no\n":
                    print "no new"
                    attributeValuesNo[currentValue] = 1
                attributeValues[currentValue] = 1
        listOfAttributes.append(attributeValues)
        listOfYes.append(attributeValuesYes)
        listOfNo.append(attributeValuesNo)

    print listOfYes
    print listOfNo

    # return listOfAttributes

# this code is for testing
output = nominalClassifer(list_of_instances)

#print output
print output
# end testing
