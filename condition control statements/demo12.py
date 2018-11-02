no = int(input("enter no: "))


res = 0
for i in range(1,no+1//2):
    if no % i == 0:

        res = res + i
if res == no:
    print("given no is perfect no")
else:
    print("not perfect")
