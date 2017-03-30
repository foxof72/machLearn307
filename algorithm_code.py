import os
import socket
import sys
import time
import random

print("Welcome to the HAJ 1R Algorithm")
print("Please enter the name of of an arff file that is present in the folder that you are running this program in:")

file_name = "data.arff"
print ("The File that you requested is " + file_name)


def split_instances(data):
    print("This is you calling split instances")


checkexists = os.path.isfile(file_name)
print("Does the file exits" + str(checkexists))

while checkexists == False:
    print (
        "Sorry, but it seems like your file does not exist in this folder. Please double check your spelling and try again.")
    print('Hint: Don\'t forget to put the document type extension.')
    file_name = "data.arff"
    print ("The File that you requested is " + file_name)
    checkexists = os.path.isfile(file_name)
    print("Does the file exits" + str(checkexists))  # can remove this later

list_of_instances = []
attributes = []  # TODO: this will need to be added to their programs
datavarcheck = "@data"
datasection = False
file = open(file_name, "r")
for data in file:

    print "data: ", data
    if '@data' in data:
        datasection = True
        print(
            "did you get here")  # this if statment is not picking it up @data, it think it has something to do with reading lines
    if data is not None and datasection is True:
        instance = data.split(",")
        # print("Your data is: " + data )
        # print (instance)
        list_of_instances.append(instance)
        # this appends to the greater list of instances
    if datasection is False:
        attributes.append(data)  # this will need to be added to their programs
print("this is the list of instances")
print(list_of_instances[1][0])
