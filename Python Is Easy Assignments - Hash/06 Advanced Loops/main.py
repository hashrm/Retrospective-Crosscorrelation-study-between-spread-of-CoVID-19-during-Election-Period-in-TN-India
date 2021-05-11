# Homework Assignment 06: Advanced Loops
"""
Expected Pattern:
 01234
  | |     0
 -----    1
  | |     2
 -----    3
  | |     4
"""

MAXIMUM_ROWS_ALLOWED = 49
MAXIMUM_COLUMNS_ALLOWED = 204

#Creating a functon with Rows and Columns
def createPlayingBoard(rows, columns):
    # Making Sure they are Integers
    if type(rows) != int or type(columns) != int:
        return False
    # It's not possible to create the playing board shape with a negative number
    if rows <= 1 or columns <= 1:
        return False
    # For Extra Credit, If the cells out of the screen and not passible to see the ends, It wont be clear.
    if rows > MAXIMUM_ROWS_ALLOWED or columns > MAXIMUM_COLUMNS_ALLOWED:
        return False

    #rows loop
    for row in range(0, rows):
        # if the rows are even, print '|'
        if row % 2 == 0:
            for column in range(0, columns):
                # if the column is even, print spaces
                if column % 2 == 0:
                    endChar = ""
                    # if it is the last element, end with a new line
                    if column == columns - 1:
                        endChar = "\n"
                    print(" ", end = endChar)
                # if the columns are odd, print '|'
                else:
                    print("|", end="")

        # if the rows are odd, print '-'
        else:
            for column in range(0, columns):
                endChar = ""
                # if it is the last element, end with a new line
                if column == columns - 1:
                    endChar = "\n"
                print("-", end=endChar)
    print("")
    return True



def playingBoardCreated(rows, columns):
    if(createPlayingBoard(rows, columns)):
        print('Here is your playing board.')
    else:
        print('Err, No playing board for you.')


playingBoardCreated(5, 5)
