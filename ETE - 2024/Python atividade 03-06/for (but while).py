list = []

while True:
    num = int(input("Digita numero 0 para: "))
    if num == 0:
        break
    list.append(num)
    
x = 0
while x < len(list):
    print(list[x])
    x+=1