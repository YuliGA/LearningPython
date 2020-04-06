def suma(a,b):
  return str(a + b)

def resta(a,b):
  return str(a - b)

def multiplicacion(a,b):
  return str(a * b)

def division(a,b):
  return str(a / b)

def calculadora(a,b,signo):
  if signo == "+":
    return ("El resultado de la operación es: " + suma(a,b))
  elif signo == "-":
    return ("El resultado de la operación es: " + resta(a,b))
  elif signo == "*":
    return ("El resultado de la operación es: " + multiplicacion(a,b))
  elif (signo == "/") & (b != 0):
    return ("El resultado de la operación es: " + division(a,b))
  elif signo == "/":
    return ("Pelotudo! no puedes dividir entre 0")
  else:
    return ("No escogio un signo válido") 

respuesta = "Si"
while respuesta == "Si":
  a = float(input("Ingrese un número "))
  b = float(input("Ingrese un número "))
  signo = input("Ingrese una operación ")
  print(calculadora(a,b,signo))
  respuesta = "cualquier cosa"
  while (respuesta != "Si") & (respuesta != "No"):
    respuesta = input("¿Desea realizar otra operación? Escriba Si o No ")

print("Sayonara")

