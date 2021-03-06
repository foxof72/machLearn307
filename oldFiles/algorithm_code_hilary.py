#Hilary Shea, John Williams, and Anthony Green 
#Naive Bayes
import os


#Assumptions we assume that there will be either a space or at least still a comma division for a missing value 
# we are assuming that the last attribute is a yes no value, and that this is the class that we are classifying for but we can change this 



print("Welcome to the HAJ 1R Algorithm")
print("Please enter the name of of an arff file that is present in the folder that you are running this program in:")

file_name = "small_set.arff"
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

list_of_instances = []
attributes = []  # this will need to be added to their programs
datavarcheck = "@data"
datasection = False
file = open(file_name, "r")
# attribute_list = []
#nominalAttributes = []
#numericAttributes = []
attribute_type_list =[]
fullAttributeList = []


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
	#print("What attribute would you like to classify your instance on?") #assumption that it must be a yes or no class, but this does not necessarly need to be the case
	#if we get things working then we can have it create a variable and take the values of that class and we can put that variable in our if statements 
	
	
	
	#ToDo= have the user select what class they want to classify on 
	#ToDo: here is where you should have a question and answer setting for what attributes it wants to classify an instance on 

for i in range(len(attributes) - 1): # we can put this into a function but this creates a list of if the attributes are numeric and nominal 
	if i > 1:
		parse_attribute = attributes[i]
		attribute_parts = parse_attribute.split(" ", 2)
		attribute_name = attribute_parts[1]
		attribute_type = attribute_parts[2]
		fullAttributeList.append(attribute_name)
		
		
		if "numeric" in attribute_type:
			attribute_type = "numeric"
			attribute_type_list.append(attribute_type)
			
		else:
			attribute_type = "nominal"
			attribute_type_list.append(attribute_type)
			






# this function checks to see if you've seen a value before or nah
def getYN(listOfInstances):
    for i in range(0, len(listOfInstances)):
        yesNo = listOfInstances[i][30]  # warning: hard coded for 30 attributes
        # print "yes/no: " + yesNo
        yesCounter = 0
        noCounter = 0
        return yesNo
		
		
def sortNominalAndNumeric(attribute_type_list,listOfInstances):  #the attribute_type_list[[attributename, attribute_type
	#this function takes the sorting above and separates the values into numeric and nominal temp lists before pushing the whole instance into the greater list 
	numAttr = len(listOfInstances[1])
	nominalInstanceList = []
	numericInstanceList = []
	for i in range(len(listOfInstances)): #this is the instances
		temp_numeric = [] #these are created so that the intances are still separated for our yes/no classifying function 
		temp_nominal=[]
		for j in range(numAttr): #this is the attributes
			if attribute_type_list[j] == "numeric": #this is to create the numerical list
				temp_numeric.append(float(listOfInstances[i][j])) #this is taking the instance value and the attribute and appending it to the temp list 
			if attribute_type_list[j] == "nominal": #this is to create the nominal list
				temp_nominal.append(listOfInstances[i][j]) #this is taking the instance value and the attribute and appending it to the list 
				if(listOfInstances[i][j] == "yes\n" or listOfInstances[i][j] == "no\n"): 
					temp_numeric.append(listOfInstances[i][j]) #this is to provide for the case that yes/ no is nominal but should still be appended to the numeric 
		numericInstanceList.append(temp_numeric) #this is taking the instance value and the attribute and appending it to the list 
		nominalInstanceList.append(temp_nominal) #this is taking the instance value and the attribute and appending it to the list 
	#print("this is the numeric instance list")
	
	#print(numericInstanceList)
	#print("this is a nominal instance list")
	#print(nominalInstanceList)
	return numericInstanceList, nominalInstanceList 
	
	


def Classifer(listOfInstances): #why is this called nominal classifier???
	listOfAttributes = []
	listOfYes = []
	listOfNo = []
	numAttr = len(listOfInstances[1]) #this is a variable for the # of attributes
	
	for k in range(numAttr):  # runs through the attributes
		attributeValues = {}
		attributeValuesYes = {}
		attributeValuesNo = {}
		
		for j in range(len(listOfInstances)):  # runs through the instances
			
			currentValue = listOfInstances[j][k]
			if "yes" in listOfInstances[j][numAttr-1]: # == "yes\n": #TODO: we can change all of these cases to be "yes" in ________ because then we can be dynamic about what class we are trying to produce 
				
				if currentValue in attributeValuesYes:
					attributeValuesYes[currentValue] += 1
					attributeValues[currentValue] +=1
					
				elif currentValue not in attributeValues: 
					attributeValuesYes [currentValue] = 1
					attributeValues[currentValue] = 1
				else: 
					attributeValuesYes [currentValue] = 1
					attributeValues[currentValue] += 1
				
			elif "no" in listOfInstances[j][numAttr-1]:# == "no\n": 
				if currentValue in attributeValuesNo:
					attributeValuesNo[currentValue] += 1
					attributeValues[currentValue] += 1
				elif currentValue not in attributeValues: 
					attributeValuesNo [currentValue] = 1
					attributeValues[currentValue] = 1
				else: 
					attributeValuesNo[currentValue] = 1
					attributeValues[currentValue] += 1

					
		listOfAttributes.append(attributeValues)
		listOfYes.append(attributeValuesYes)
		listOfNo.append(attributeValuesNo)
	#print("this is the list of yes")
	#print (listOfYes)
	#print("this is the list of no")
	#print (listOfNo)
	#print("this is the list of all the totals")
	#print (listOfAttributes)
	return listOfYes, listOfNo, listOfAttributes

	
	
numericInstanceList, nominalInstanceList=sortNominalAndNumeric(attribute_type_list,list_of_instances) 
	#this code is for testing
numListYes, numListNo, numTotals = Classifer(numericInstanceList) #this is not working currently because yes\n and no\n are not in it 

nomListYes, nomListNo, nomTotals= Classifer(nominalInstanceList)

#print(list_of_instances)
listYes, listNo, listTotals = Classifer(list_of_instances)

print (listTotals)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#this is where you start editing
print("What attribute would you like to classify on?")
print("Select on your keyboard what attribute you would like to classify on: ")
for i in range(len(fullAttributeList)):
	print(str(i) + ": " + fullAttributeList[i])
keyboardInput = input()
if int(keyboardInput) < len(fullAttributeList) and int(keyboardInput) > 0: 
	classifyBy = fullAttributeList[int(keyboardInput)]
else: 
	keyboardInput = input("Sorry, that was out of range")
	
print("You are classifying on " + classifyBy + ".")


print("Sweet! Now let's create an instance to classify:" )
for j in range(len(fullAttributeList)):
	attrChoices = str(listTotals[j])
	tempChoices = attrChoices.split("'")
#print(tempChoices)
	choices = []
	for i in range(len(tempChoices)):
		if( (i%2) !=0 ):
			choices.append(tempChoices[i]) 
		#print(tempChoices[i])
	print("Please select what you would like to classify on for this attribute:")
	for i in range(len(choices)):
		print(str(i) + ": " + choices[i])

	choice = input()
	if int(choice) > len(choices) or int(choice) < 0: 
		print("We are sorry, but that was out of range.")
		for i in range(len(choices)):
			print(str(i) + ": " + choices[i])
		choice = input()
	print(choice)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#just send over the # cooresponding to the number in the list

 #put this in a loop so you class classify all that you want to classify


#also if you are classifying multiple instances you should make sure that you are creating a summary, so all of the classifications can pop up 






#print("This is the num list yes")
#print (numListYes)


#print output
#print output
# end testing
