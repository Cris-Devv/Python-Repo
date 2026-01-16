sujo = 4 #
lavado = list(range(1, sujo+1)) #range é pra transformar inteiros em lista/sequência. 1 é o início, sujo é a parada e o +1 adiciona pra parada pra acompanhar quando for continuar.

while True:
    print(lavado)
    operacao = input(f"B pra botar, T pra tirar, Q pra quitar.")
    operacao = operacao.upper()
    
    if operacao == "T":
        if len(lavado) > 0:
            lavo = lavado.pop()
            sujo -= 1
            print(f"prato {lavo} lavado")
    
    elif operacao == "B":
        sujo += 1
        lavado.append(sujo)
        

    elif operacao == "Q":
        break

    else:
        print("Isso nem é opção :(")