qtd = int(input("quant "))
lista = []
inf =  2454545454

for i in range(qtd):
    name = input("Digite o nome: ")
    name = name.capitalize()
    if name in lista:
        for i in range(inf):
            for name in lista:
                name = input(f"Nome {name}")  # estrutura de repetiçõa > lista usabdo loop e input do usuario; dicionario cm um loop for; contador; while, raplece, slit ao inves do fpor, nao precisa dele, isalpha, sum