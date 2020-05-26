print ("Indique un año: ")
anio = int(input())

def es_bisiesto(anio):
  if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print("Es año bisiesto")
  else:
    print("El año no es bisiesto")

es_bisiesto(anio)
