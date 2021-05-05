##VARIABLE
#variables are a way of storing information
#that you may know or may not know in the
#begining of the code.
#User inputs can be stored as variables
#An example for variables is given below
one = 1
two = 2
three = 3
#here, "one" is the variable and
#"1" is the value added to it.

#you can print the values stored in the variable by calling the variable inside a print function
print(one)
print(two)
print(three)
#we can also print backwards
#we can also reuse variables
print(two)
print(one)
#you can modify/over write the value of the variable by declaring a new value to it.
#for example
two = 4
print(two)
#the above prints the value as 4 and the overall otput will be, 123214, i.e the change is applicable only to the after modification.

#you can also create decimal variables and store decimal values, It can be named as anything not necessarily as decimal or such
#it is called as decimal or float variable in python.
decimal = 1.1
print(decimal)

#next is printing a string variable
#it is called a string variable in python, It can be named as anything not necessarily as string_variable or such
string_variable = "Hello"
print(string_variable)

##Python figures out what type a variable is, automatically.
#We can just assign a value to it and use it later.
#Different, different types of variables can't be added together, they should be of one common way.
#Variables with values determined under quotation marks are considered to be as strings.

string_variable = "Hello" + "1"
print(string_variable)
#this prints "Hello1", # When 2 strings are added, its called string concatenation

##Types of Variables in python:
#int, long(longer int), float/decimal, string

##Global Variable:
#all variables contained, not inside any functions are called Global Variables
#they are core of the code and can be accessed from anywhere, Printing the variable prints the value of it.

#Local Variables are declared inside a function,
#what is a function? See Down
# General Structure of Function,
#def FunctionName():
#    Local_Variable = "New Variable"
#    Action
#    Required Output
#    return

#def FunctionName():
#    Local_Variable = "New Variable"
#    print(Local_Variable)
#    return
##: When all the lines except the above 4 are commented, we can get the output of local variable.

# you can also assign the value to multiple variables ina single line using commas(,):
onesq, twosq, threesq = 1, 4, 9
print(onesq+twosq+threesq)

#a calculation can also be assigned as a value of a variable.
#Example:
five = 3+2
print(five)
#python is Uppercase, Lower case sensitive when it comes to naming vriables, so always use same name without case change in all related functions.
#operating undefined variables also creates an error,
#For Eg: If ive never declared Hariesh(Undefined Variable) + One, One is defined and Hariesh is undefined. So it will cause an error.
#left = right (left is always the variable name, right is always the value.)

##COUNTING Variable
#count variable can be used count everything that something happens.
count = 0
print(count)
#value of count is 0, so it prints 0.
#if I want to changethe count value by an integer, add the same integer to count value, it results in the new count value.
#for example, when count is 0 and count = count + 1 is assigned, then count value becomes 1.
count = count+1
print(count)
count = count+1
print(count)
#the other shorthand to mention, count = count + 1 is
count += 1
print(count)
#similar to addition(+), sub(-), mux(*), div(/) etc can be done
count*= 3
#it is same as count = count*3
print(count)
count/= 9
print(count)
