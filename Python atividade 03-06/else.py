list = [2, 3, 5, 10, 377]

search = int(input("Type the number you want to search: "))

for x in list:
    if x == search:
        print(f"The number {search} is on the list.")
        break
        
else:
    print(f"The number {search} is not on the list.")