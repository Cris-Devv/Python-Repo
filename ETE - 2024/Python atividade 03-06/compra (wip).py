batata = 0

while True:
    compra = int(input("Quantas batatas você quer comprar? "))
    batata = batata + compra
    if batata > 0:
        break
    else:
        print("You can't buy this amount. Try again.")
    
while batata > 0:
    vender = int(input("Quantas batatas vão sair? "))
    batata = batata - vender