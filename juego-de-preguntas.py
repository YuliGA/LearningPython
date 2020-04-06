jugador = (input("¿Cuál es tu nombre? "))

preguntas = ["¿Cuál es el lugar más frío de la tierra?", "¿Quién escribió La Odisea?", "¿Cuál es el río más largo del mundo?","¿Cómo se llama la Reina del Reino Unido?", "¿En qué país se encuentra la torre de Pisa?"]

opciones = ['A) La Patagonia\nB) La Antartida\nC) El Polo Sur\nD) El Oeste', 'A) El Cesar\nB) Jackie Chan\nC) Homero\nD) Galileo', 'A) Amazonas\nB) Nilo\nC) La Plata\nD) Negro', 'A) Margarita\nB) Isabel\nC) Juana\nD) Luna', 'A) Brasila\nB) India\nC) China\nD) Italia']

puntaje = 0

def inicio(jugador):
  if jugador != "":
    print("Que comience el juego " + jugador)
  else:
    print("Ingresa tu nombre para comenzar a jugar!")
    jugador = (input("¿Cuál es tu nombre? "))
    inicio(jugador)

inicio(jugador)

print("Pegunta 1:" + (preguntas[0]))
print("Opciones:\n" + (opciones[0]))

respuesta1 = (input("Escribe una respuesta "))

def valida_res1():
  if respuesta1 == "B" or respuesta1 == "b":
    print("Correcto! " + "Empezamos bien, " + str(jugador) + ".")
    return True
  else:
    print("Incorrecto! =( \n" + "Total Respuestas Correctas: 0/5")
    print("Era una pregunta muy fácil " + str(jugador))
    return False

if valida_res1():
  print("Has ganado " + str(puntaje + 10) + " puntos.\n")
  print("Pegunta 2:" + (preguntas[1]))
  print("Opciones:\n" + (opciones[1]))

  def valida_res2():
    respuesta2 = (input("Escribe una respuesta "))
    if respuesta2 == "C" or respuesta2 == "c":
      print("Correcto! " + "Muy bien " + str(jugador))
      return True
    else:
      print("Incorrecto! =( \n" + "Total Respuestas Correctas: 1/5")
      print("¿Cómo no lo sabías? " + str(jugador))
      return False

  if valida_res2():
    print("Has ganado " + str(puntaje + 20) + " puntos.\n")
    print("Pegunta 3:" + (preguntas[2]))
    print("Opciones:\n" + (opciones[2]))

    def valida_res3():
      respuesta3 = (input("Escribe una respuesta "))
      if respuesta3 == "A" or respuesta3 == "a":
        print("Correcto! " + str(jugador + "¡Tú sí que sabes!" ))
        return True
      else:
        print("Incorrecto! =( \n" + "Total Respuestas Correctas: 2/5")
        print("Elemental " + str(jugador))
        return False

    if valida_res3():
      print("Has ganado " + str(puntaje + 30) + " puntos.\n")
      print("Pegunta 4:" + (preguntas[3]))
      print("Opciones:\n" + (opciones[3]))

      def valida_res4():
        respuesta4 = (input("Escribe una respuesta "))
        if respuesta4 == "B" or respuesta4 == "b":
          print("Correcto! " + "¡Geni@ " + str(jugador) + "!")
          return True
        else:
          print("Incorrecto! =( \n" + "Total Respuestas Correctas: 3/5")
          print("Metiste la pata " + str(jugador))
          return False

      if valida_res4():
        print("Has ganado " + str(puntaje + 40) + " puntos.\n")
        print("Pegunta 5:" + (preguntas[4]))
        print("Opciones:\n" + (opciones[4]))

        def valida_res5():
          respuesta5 = (input("Escribe una respuesta "))
          if respuesta5 == "D" or respuesta5 == "d":
            print("Correcto! " + str(jugador) + ", MegaCrack!!")
            return True
          else:
            print("Incorrecto! =( \n" + "Total Respuestas Correctas: 4/5")
            return False

        if valida_res5():
          print("Contestaste todas las preguntas correctamente!")
          print("Has ganado el juego! Sumaste " + str(puntaje + 50) + " puntos.")
