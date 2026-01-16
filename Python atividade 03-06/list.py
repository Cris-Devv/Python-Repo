last = 10
line = list(range(1, last + 1))

while True:
    print(f"\nThere are {len(line)} clients on the line")
    print(f"Current line: {line}")
    print("Press F to add a client to the end of the list")
    print("or A to provide service. Press S to quit.")
    operation = input("Operation (F, A or S): ")
    operation = operation.upper()

    if operation == "A":
        if len(line) > 0:
            served = line.pop(0)
            print(f"Client {served} served")
        else:
            print("Empty line. There's no one to be served.")

    elif operation == "F":
        last += 1
        line.append(last)

    elif operation == "S":
        break

    else:
        print("Invalid operation. Press only F, A or S!")
