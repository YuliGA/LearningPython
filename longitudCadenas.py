fruta = str(input("Ingresa una palabra: "))

def deletreo():
  indice = 0
  while indice < len(fruta):
   letra = fruta[indice]
   print (letra)
   indice = indice + 1

deletreo()

print()

def deletreoInverso():
  n = 1
  while n <= len(fruta):
   print(fruta[-n])
   n = n + 1

deletreoInverso()
