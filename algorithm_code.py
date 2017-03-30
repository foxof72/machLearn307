import os
import socket
import sys
import time
import re
import random


print("Welcome to the HAJ 1R Algorithm") 
print("Please enter the name of of an arff file that is present in the folder that you are running this program in:")

file_name = input("File Name: ")
print ("The File that you requested is " + file_name)

def split_instances(data): 
	print("This is you calling split instances") 
	


checkexists = os.path.isfile(file_name)
print("Does the file exits" + str(checkexists))

while checkexists == False: 
	print ("Sorry, but it seems like your file does not exist in this folder. Please double check your spelling and try again.")
	print("Hint: Don't foget to put the document type extension.")
	file_name = input("File Name: ")
	print ("The File that you requested is " + file_name)
	checkexists = os.path.isfile(file_name)
	print("Does the file exits" + str(checkexists)) #can remove this later
	
	
list_of_instances= []
attributes = [] #this will need to be added to their programs
datavarcheck = "@data"
datasection = False
file = open(file_name, "r") 
#whole_file = file.read()
#if '@data' in whole_file:
#	print ("Checking if @data is in the whole file")
for data in file:  
	
	print(data)
	print ("this is before the if @data statement")
	if '@data' in data:
		datasection = True
		print("did you get here") #this if statment is not picking it up @data, it think it has something to do with reading lines
	if data	!= None and datasection is True: 
		instance = data.split(",")
		#print("Your data is: " + data )
		#print (instance)
		list_of_instances.append(instance) 
		#this appends to the greater list of instances 
		print("this is the list of instances")
		print(list_of_instances)
	if datasection is False: 
		attributes.append(data)#this will need to be added to their programs
		
		
		

		
