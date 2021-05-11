# Using Simple for Loops to create a Tic Tac Toe field
"""
Tic Tac Toe field has 2 components, Height and Cols
 01234
  | | 0
 -----1
  | | 2
 -----3
  | | 4
"""

for row in range(5):
    if row%2 == 0:
        for column in range(1,6):
            if column%2 == 1:
                if column != 5:
                    print(" ", end = "") # If you put end="" it won't go to the next row to print the next element
                else:
                    print(" ") # This will move the 5th element, which is the last point in the line, to go to the next row to print the next element since it doesnn't has end statement in the end.
            else:
                print("|",end ="")
    elif row%2 != 0:
        print("-----")
