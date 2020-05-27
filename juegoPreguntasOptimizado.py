jugador = input("Introduce tu nombre:\n")
while jugador == "":
   jugador = input("Pelotudo! Necesito tu nombre!\n")
   
preguntas = ["¿Cuál es el lugar más frío de la tierra?", "¿Quién escribió La Odisea?", "¿Cuál es el río más largo del mundo?","¿Cómo se llama la Reina del Reino Unido?", "¿En qué país se encuentra la torre de Pisa?"]
opciones = ['A) La Patagonia\nB) La Antartida\nC) El Polo Sur\nD) El Oeste', 'A) El Cesar\nB) Jackie Chan\nC) Homero\nD) Galileo', 'A) Amazonas\nB) Nilo\nC) La Plata\nD) Negro', 'A) Margarita\nB) Isabel\nC) Juana\nD) Luna', 'A) Brasila\nB) India\nC) China\nD) Italia']
respuestas = ["b","c","a","b","d"]
ready = False
indice = 0
puntaje = 0
while not ready:
   print(preguntas[indice])
   print(opciones[indice])
   respuesta = input("Cual es tu respuesta?\n").lower()
   ready = (respuesta != respuestas[indice])
   if ready:
       print("Animal del monte!")
   else:
       print("Wuuuujuuu! Correcto!")
       puntaje += 10
   ready = (ready) | (indice == (len(preguntas) - 1))
   indice += 1
print("Puntaje:",puntaje)
