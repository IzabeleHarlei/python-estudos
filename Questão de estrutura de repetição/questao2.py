palavra = input()
for vogal in palavra:
 if vogal == "a" or vogal == "o" or vogal == "e" or vogal == "i" or vogal == "u":
  contagens_vogal = palavra.count(vogal)
  print(contagens_vogal)
