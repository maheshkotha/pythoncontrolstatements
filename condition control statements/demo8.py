#name = input("Enter Name: ")
name = "mahesh"
count = 0
c1 = 0
for x in name:
    count += 1
    for y in x:
        print(y,end="")
        c1 += 1
        if count > c1:
            print()


