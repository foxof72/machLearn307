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
    # print("this is the numeric instance list")

    # print(numericInstanceList)
    # print("this is a nominal instance list")
    # print(nominalInstanceList)

    return numericInstanceList, nominalInstanceList