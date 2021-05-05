#FUNCTIONS
"""
Functions are a way by which you can just call it, to do certain repetitive blocks of code which you want to do over and over again.
Function is started by a keyword "def Function_Name(Input): and then an indent spacing is given where you execute an action and give out an output"
"""

#General Structure of a Function is as follows,
"""
def Function_Name(Input):
    action
    return output
    all code written after the tab space aka indent is considered a part of the function.
all code written before the tab space aka indent is considered as not a part of the function.
"""
#def - tells computer you are about to define a Function

#Example of a function:
#Creating a Function:
def AddOne(input):
    output = input + 1
    # both "Number" and "output" are local variables
    return output
    #"return" takes it outside the function

var = 0
print(var)
#Calling a function
var2 = AddOne(var)
#AddOne(var) gets practically replaced by the value of output. You can right output directly because its a Local Variable and it can't be called like a Global Variable and hence results in error.
"""
we call the functions name, here it is "AddOne", Add brackets to the input variable.
"""
print(var2)
#Calling AddOne function again instead of doing the entire process.
var3 = AddOne(var2)
#AddOne(var2) runs the same function of AddOne on var2 and it's result is stored in var3)
print(var3)

#function inputs are not necessarily needed to be variables, we can use numbers too.
var4 = AddOne(2)
print(var4)

#inputs can be pretty much anything, not just int but also float or string etc. but only float and int can be operated together, and strings could be operated together.
#decimal/float
var5 = AddOne(2+3.5) #both floats are calculated and taken as one number automatically
print(var5)

#multiple inputs can be given within a single function.
#Example

def AddOneAddTwo(NumberOne,NumberTwo):
    output = NumberOne + 1
    output += NumberTwo + 2
    #the above is same as, output = output + NumberTwo + 2
    return output

#calling multiple inputs Function
sum = AddOneAddTwo(1,2)
print(sum)
#you can also call it by variable names
sum = AddOneAddTwo(var2,var3)
print(sum)
