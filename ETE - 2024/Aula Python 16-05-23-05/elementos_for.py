lista = [0, 1, 2]

pesquisar = int(input("Digite um número pra pesquisar: "))
for percorre in lista:
    if percorre == pesquisar:
        print(f"Elemento {pesquisar} encontrado.")
        break
else:
        print(f"Elemento {pesquisar} não encontrado.")