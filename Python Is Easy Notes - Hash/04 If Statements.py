#If Statements
print("If Statements")
"""
if statements execute action, only if something specific occured.
Mainly to do something based on conditions
"""
#General Structure of an "if" statements
"""
if condition:
    action
"""
#Lets write an if statement to create a counter for the number of likes for a facebook post.
#lets create a var called "click" first
click = False
#In Python we can have True or False values, these are called Boolean values.

Like = 0

click = True

#if statement goes here,
if click == True:
    """
    = is an assignment of a value to a variable,
    == is is equality where we verify whether the value of the variable and the value which we ask for are the same value
    """
    Like += 1
    # Now to reset the click value to False so that we can count again when we get a new Like from another Click.
    click = False

print(Like)

# Now lets work on a temperature reglator sing a thermostat.
Temperature = 25
Thermo = 15
print(Thermo)

# what if temperature gets under 15 and I want to maintain the heat inside:
if Temperature <= 15:
    Thermo += 5
print(Thermo)

# what if temperature outside gets higher and I want to minimize it inside:
if Temperature >= 20:
    Thermo -= 3
print(Thermo)

## Lets do if statements in words, i.e. strings

Time = "Night"
Sleepy = False
Pajamas = "Off"
InBed = True

if Time == "Night" or Sleepy == True or InBed == True:
    Pajamas= "On"

elif Time == "Day" or Sleepy == False or InBed == False:
    Pajamas = "Off"
else:
    Pajamas = "Oh Boy!"
print(Pajamas)
