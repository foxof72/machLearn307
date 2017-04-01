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
        print(list_of_instances)
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
def seenIt(thingToCheck, valueList):
    for i in (0, len(valueList)):
        if valueList[i] == thingToCheck:
            return True  # you've seen this value before
    return False  # you have not seen this value before


def nominalClassifer(listOfInstances):
    listOfAttributes = []
    # for i in range(len(list_of_instances)): #runs through the instances
    for k in range(len(listOfInstances[1])):  # runs through the attributes
        attributeValues = {}
        for j in range(len(listOfInstances)):  # runs through the instances
            # attributeValues = defaultdict(int)
            currentValue = listOfInstances[j][k]
            print "currentValue: " + currentValue
            if currentValue in attributeValues:
                print "already in "
                attributeValues[currentValue] += 1
            else:
                print "not in"
                attributeValues[currentValue] = 1
        listOfAttributes.append(attributeValues)
    return listOfAttributes

# this code is for testing
output = nominalClassifer(list_of_instances)
print output
# end testing







