list = []

while True:
    num = int(input("Insert a number on the list (Type 0 to exit): "))
    if num == 0:
        break
    list.append(num)
    
for x in list:
    print(x)