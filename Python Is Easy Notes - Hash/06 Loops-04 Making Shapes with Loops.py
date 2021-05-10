"""
Making shapes with loops
"""
Length = 10
ToPrint = "<->"
for pos in range(1,Length+1):
    print(ToPrint*pos)
for pos in range(Length-1,0,-1):
    print("</>"*pos)
