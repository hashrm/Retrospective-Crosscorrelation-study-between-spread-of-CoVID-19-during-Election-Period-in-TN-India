# Loops-1
"""
For loops in Python
For loops are a way to iterate over items or elements
For loops are an excellent way to go through content in a distinct manner
For Loops in Python allows you to
-> Predefine what you want to start counting with,
-> How you want your step size to be
-> When to end.
-> For loops in Python are For___in___ loops.
They iterate over something given to go through or go over it.
"""

# Looping through Strings
# Lets start with an example
# variable = value
Word = "Hello"
#Lets declare a List called Letters
Letters = []
# Now lets try to printout individual letters
for w in Word:
    print(w)
    if w == "e":
        print("what a funny letter")
    Letters.append(w)
print(Letters)

for l in Letters:
    print(l)

# Looping through Lists
Numbers = [1,2,3,4,5]
for n in Numbers:
    if n%2 == 1:
        ## n%int is a modulo division stmt, which defines that "n" perfectly fits within the range by specific range of divisions in whole number.
        ## 1%2 = 1
        ## 2%2 = 0
        ## 3%2 = 1
        ## 4%2 = 0
        ## 5%2 = 1
        ## variable%2 == 0 -> Variable is an even number
        ## variable%2 == 1 -> Variable is an odd number
        print(n)
# Looping in a range
# General Func:
# for n in range(starting_value,stopping_value,increment)
# stopping value is non inclusive
Numbers2 = []
# Printing every number from 0
for n2 in range(10):
    print(n2)
    Numbers2.append(n2)
print(Numbers2)

# Printing Odd numbers from 0 using 2 as increment
Numbers3 = []
for n3 in range(1,10,2):
    print(n3)
    Numbers3.append(n3)
print(Numbers3)
