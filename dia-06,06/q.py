x = str(input("digite uma palavra: "))
lista = []
lista.append(x)
if x in lista:
    print(f'"{x}" está na lista')
else:
    print(f'Não foi possível colocar {x} na lista')
