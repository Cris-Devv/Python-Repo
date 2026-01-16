x = 1

while True:
    while x <= 100:
        print(x)
        x +=1
    choice = int(input("Type a number higher than 0 to repeat the code or type 0 to stop: "))
    if choice >= 1:
        x = 1
    else:
        print("while has stopped.")
        break