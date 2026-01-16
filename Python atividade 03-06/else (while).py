list = [2, 3, 5, 10, 377]

search = int(input("Type the number you want to search: "))

x = 0
while x < len(list):
    if list[x] == search:
        print(f"The number {search} is in your list.")
        break
    x += 1
else:
    print(f"The number {search} doesn't exist.")