fruta = "banana"
cuenta = 0
for car in fruta:
  if car == 'a':
    cuenta = cuenta + 1
print (cuenta)

# Como ejercicio, encapsule este codigo en una funcion llamada cuentaLetras, y generalicela de forma que acepte la cadena y la letra como parametros.

cadena = str(input("Ingrese una palabra: "))
letra = str(input("Ingrese la letra que desea contar en la palabra: "))

def cuentaLetras(cadena, letra):
  cuenta = 0
  for caracter in cadena:
    if caracter == letra:
      cuenta = cuenta + 1
  print (cuenta)
    
cuentaLetras(cadena, letra)
