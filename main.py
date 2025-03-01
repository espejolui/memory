# 1. Botón de iniciar -- Ya
# 2. Generar un número y mostrar -- Ya
# 3. Guardarlo en una lista -- Ya
# 4. Borrarlo en pantalla del usuario de la terminal, pero sin salir del juego
# 5. Pedir que lo dijite luego y guardarlo en una lista
# 6. Comparar las dos listas, si son iguales repetir el proceso sino, perdiste

import random
import time
import os
import re

color_list = ["verde", "rojo", "amarillo", "naranja"]
memory_color = []

print("¡Midamos tu memoria!")
time.sleep(.5)

while True:
  print("Memoriza el siguiente color:\n")
  time.sleep(1)

  color = random.choice(color_list)
  memory_color.append(color)

  print(" - ".join(memory_color))
  time.sleep(2)
  os.system('cls' if os.name == 'nt' else 'clear')

  # Convierte la entrada del usuario a minúsculas y elimina espacios en los extremos
  color_user = input("Escribe los colores mostrados: \n").lower().strip()

  # Divide la cadena en una lista usando una expresión regular
    # r''  -> Indica que es una cadena sin procesar (raw string), evitando problemas con caracteres de escape.
    # []   -> Define un conjunto de caracteres a buscar.
    # ,    -> Coincide con la coma como separador.
    # \s   -> Coincide con cualquier espacio en blanco (espacio, tabulación, salto de línea, etc.).
    # +    -> Indica que se debe coincidir con uno o más caracteres del conjunto definido ([]).
  color_user = re.split(r'[,\s]+', color_user)

  if color_user != memory_color:
    print("Perdiste :(")
    break
