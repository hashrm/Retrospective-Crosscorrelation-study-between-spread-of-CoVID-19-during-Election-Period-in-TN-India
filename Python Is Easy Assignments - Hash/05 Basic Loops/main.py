# Homework Assignment #5: Basic Loops - Fizz Buzz

# Defining a range is the easiest way to print all numbers in that range.
for number in range(1, 101):
    # By common LCM, for numbers divisible by both 3 & 5 they should also be divisible by 3*5 = 15
    if number%(3*5) == 0:
        print("FizzBuzz")
        continue
    # For only divisible by 3
    elif number%3 == 0:
        print("Fizz")
        continue
    # For only divisible by 5
    elif number%5 == 0:
        print("Buzz")
        continue
    print(number)

# Prime number is to be done for extra credit and it's slightly confusing, Is it possible to do it in a single if statement.
