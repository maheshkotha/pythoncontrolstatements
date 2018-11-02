for x in range(4):

    for y in range(4,x,-1):
        print(" ",end="")
    for y in range(x+1):
        print("*",end="")


    print()
for x in range(4):

    for y in range(x+2):
        print(" ", end="")

    for y in range(4,x+1,-1):
        print("*",end="")
    print()