"""
Create a function that accepts 3 parameters and checks for equality between any two of them.
Your function should return True if 2 or more of the parameters are equal, and false is none of them are equal to any of the others.
# Extra Credits:
                Modify your function so that strings can be compared to integers if they are equivalent.
For example, if the following values are passed to your function: 6,5,"5"
You should modify it so that it returns true instead of false.
# Hint:
        there's a built in Python function called "int" that will help you convert strings to Integers.
"""


#function that accepts 3 parameters
def equality(x,y,z):
    #converting strings to integers for extra credits.
    a = int(x)
    b = int(y)
    c = int(z)
    #comparing values whether any 2 or all 3 values match.
    if a == b:
        bool = True
        print(bool)
    elif a == c:
        bool = True
        print(bool)
    elif b == a:
        bool = True
        print(bool)
    elif b == c:
        bool = True
        print(bool)
    elif c == a:
        bool = True
        print(bool)
    elif c == b:
        bool = True
        print(bool)
    elif a == b == c:
        bool = True
        print(bool)
    else:
        bool = False
        print(bool)

#calling the function
function_call = equality(6,"5",5)
