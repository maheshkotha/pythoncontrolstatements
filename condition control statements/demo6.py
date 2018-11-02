for x in range(8):
    for y in range(7-x+1,0,2):
        print(" ",end=" ")
    for y in range(x):
        print("*",end=" ")
    print()
# for x in range(8):
#     for y in range(x):
#         print(" ",end=" ")
#     for y in range(7-2*x,0,-1):
#         print("*",end=" ")
#     print()