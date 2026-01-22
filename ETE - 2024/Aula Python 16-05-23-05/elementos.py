elementos = 5
lista = list(range(1, elementos+1)) #list cria uma lista baseado em um número inteiro. range determina o alcance da lista
i = 0

while True:
    pesquisa = int(input("Digite o elemento que você deseja buscar: "))

    while pesquisa < len(lista):
        i+=1
        if pesquisa == lista[i]: 
            print(f"O elemento {pesquisa} existe na lista.")
            break

    else:
        print(f"O elemento {pesquisa} não existe na lista. Tente novamente.")