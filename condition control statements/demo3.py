d1  = {"idno":101,
       "name":"Ravi",
       "salary":125000.00}

for x in d1:
    print(x)
print("------------------------")
for x in d1:
    print(d1[x])
print("------------------------")
for x in d1.items():
    print(x)
print("------------------------")
for x in d1.keys():
    print(x)
print("------------------------")
for x in d1.values():
    print(x)
print("------------------------")
for x, y in d1.items():
    print(x,y)

