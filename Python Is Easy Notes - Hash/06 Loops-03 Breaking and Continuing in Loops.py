#break and Continuing in loops
"""
It helps to manage the flow, If you have different things, requirements and want to end halfway in between or as such and continue after a moment or range,
"""

################################################################################
# Program 1
# To know the position of elements in the list
################################################################################

# Lets create a variable to note the position of participants in the list.
# position = 1
# Lets create a list with participants
Participants = ["Jen","Alex","Tina","Joe","Ben"]
# for name in participants:
#     if name == "Alex":
#         print("About to break")
#         break
#     print("About to Increment")
#     position += 1
# print(position)
# print(participants)

################################################################################


################################################################################
# Program 2
# To know the position of elements in the list with index
################################################################################

# Lets create a list with participants
# for currentIndex in range(len(Participants)):       #loop over all elements in list                            #print value of currentIndex
#     if Participants[currentIndex] == "Joe":         #check if list element is equal to Joe
#         print("Have Breaked")                       #print message
#         break                                      #come out of the loop
#     print("Not Breaked")                           #print message
# print(currentIndex+1)                              #print currentIndex of matched element

################################################################################
# Program 3
# Continous Statement
################################################################################
for number in range(10):
    #Checking if the reminder is absolute 0 when divided by 3.
    if number%3 == 0:
        print(number)
        print("is divisible by 3")
        #Now continue to do it amongst other values in the range too.
        continue
    print(number)
    print('Not Divisible by 3')
################################################################################
