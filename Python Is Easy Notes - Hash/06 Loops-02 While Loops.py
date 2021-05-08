#While loops
"""
While loops are a way of repeating or doing something while a certain condition is true.
"""
# While General Form
# while(condition):
#     action-1
#     action-2
#     action-3 or as many as we want, but always atleast 1.

# Lets create a counter with while loop, A counter is a function that calculates how many times a certain function is done.
# It helps to keep track of where you are and how many times youve done.


# #######################
# Program 1
#########################

# Program to count

# Creating a variable called counter, to count the nos of occurances
counter = 1

while(counter <= 10):
#    print(counter)
    counter += 1

# #######################
# Program 2
#########################
# Program to add the total of all count values
# Creating a variable called counter1, to count the nos of occurances
counter1 = 1
# Creating a variable called sum, to add the number of occurances
sum = 0

while(counter1 <= 10):
    sum += counter1
    counter1 += 1
#    print(sum)
#########################


#########################
# Program 3
#########################
#Printing Letters corresponding to index using While Loop

# Creating a list with Letters
Letters = ["a","b","c","d","e"]
# Lets create and Index, this is used to increment the value by 1 in the and print it in a while loop.
Index = 0
while(Index < len(Letters)):
    #print(Index)
    #print(Letters[Index])
    Index += 1
########################

########################
#Program 4
########################
# Finding the time an object takes to fall, with height and certain speed
########################
height = 5000
speed = 50
time = 0
# FUNFACT: actually what this while loop does is = Time = height/speed while time is mentioned as zero.
while(height>0):
    height = height-speed
    time += 1
# print(height)
print(time)
########################
########################
