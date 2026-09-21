nomes = ["maria", "joao", "jose", "rosa", "jose", "ze"]
nome = input("Nome: ")
if nome in nomes: 
    posicao = nomes.index(nome)
    print(f"posição de {nome} na lista: {posicao}")
else:
    print(f"{nome} nao esta na lista.")