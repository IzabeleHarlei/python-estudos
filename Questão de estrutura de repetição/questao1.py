lista_notas = [50,60,70,80,90,100]
for nota in lista_notas:
    if nota >= 90:
        print("A")
    elif nota >= 80 and nota < 90:
        print("B")
    elif nota >= 70 and nota < 80:
        print("C")    
    elif nota >= 60 and nota < 70:
        print("D")
    else:
        print("F")
      
  