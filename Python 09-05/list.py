last = 10
line = list(range(1, last + 1))

while True:
    print(f"\nExistem {len(line)} clientes na fila")
    print(f"Fila atual: {line}")
    print("Digite F para adicionar um cliente ao fim da fila.")
    print("ou A para realizar o atendimento. S para sair.")
    operation = input("Operation (F, A or S): ")
    operation = operation.upper()

    if operation == "A":
        if len(line) > 0:
            served = line.pop(0)
            print(f"Cliente {served} served")
        

    elif operation == "F":
        last += 1
        line.append(last)

    elif operation == "S":
        break

    else:
        print("Operação inválida: Digite apenas F, A ou S!")
