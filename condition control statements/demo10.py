def str_bit(stri):
    a = ''
    count = 0
    for i in stri:
        count = count + 1
        if count %2 != 0:
            a = a + i
    print(a)
name = input("enter string")

str_bit(name)

