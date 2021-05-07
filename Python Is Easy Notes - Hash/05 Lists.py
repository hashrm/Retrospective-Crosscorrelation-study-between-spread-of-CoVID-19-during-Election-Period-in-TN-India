print("Lists")
"""
Lits are a great way to organize data.
Add lots of data into one variable.
It makes it easier to call a certain set of data, variables at a time.
"""
"""
The general structure of a list has a variable to which the values are declared & a set of elements in square brackets, comma separated from each other.
TestList = ["element1","element2","element3"]
In programming we start conting from zero, the count of each element in the list is as follows,
TestList = [0,1,2] #these are the index of the element.
TestList = [-3,-2,-1] #these are the index of the element in reverse order, Useful for calling the last elements.
"""
# Lets create our first List
Scores = [90.75,77,80,85,90]
# Printing the results
print(Scores)
# Printing the result of a specific elements from the list of elements
print(Scores[0])
# Printing the result of a specific elements by accessing list in reverse order
# The following code prints the last elements of the list.
print(Scores[-1])
#The following prints the first 2 elements from the list.
#it means from element with index 0, upto element with index 2, excluding element with index 2.
print(Scores[0:2])
# To print the list from a starting value till the end of list, all you have to do is, [index of starting element:]
print(Scores[2:])
# Assigning a new value to an element in the list by calling out the index:
Scores[0] = 95
print(Scores)
# Performing operators to an element in the list by calling out the index:
Scores[0] += 2
print(Scores)
# It is not necessary that all elements of a List should be of the same data type, It can be ass different as needed.
# Here we are replacing the Scores[0] element with a string "Hello"
Scores[0] = "Hello"
print(Scores)
#Changing the string to a random integer again
Scores[0] = 75
print(Scores)
#to delete a specific set of values, for example, If students 2, and 3; i.e, elements 1,2 wants their scores to be deleted from the list
#Scores[1:3] = []
#print(Scores)
# An element of the list can also be a List
Scores[2] = ["Hello","World"]
print(Scores)
# To see the list stored in an element
print(Scores[2])
# To see a specific element from the list, stored as an element: # Use index of the list of the list element.
print(Scores[2][0])
# To make changes to the existing list
# Syntax:
# variable.function(value)
# To add a new element to the end of the List
Scores.append(82)
print(Scores)
