import time
import random
import os
import re

class Actions:

  def play(self):
    print("¡Midamos tu memoria!")
    time.sleep(.5)

  def generate_color(self):
    color_list = ["verde", "rojo", "amarillo", "azul"]
    return random.choice(color_list)

  def show_colors(self,colors):
    print("Memoriza el siguiente color:\n")
    time.sleep(1)
    print(" - ".join(colors))
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

  def user_input(self):
     color_user = input("Escribe los colores mostrados: \n").lower().strip()

      # Divide la cadena en una lista usando una expresión regular
     # r''  -> Indica que es una cadena sin procesar (raw string), evitando problemas con caracteres de escape.
     # []   -> Define un conjunto de caracteres a buscar.
     # ,    -> Coincide con la coma como separador.
     # \s   -> Coincide con cualquier espacio en blanco (espacio, tabulación, salto de línea, etc.).
     # +    -> Indica que se debe coincidir con uno o más caracteres del conjunto definido ([]).
     return re.split(r'[,\s]+', color_user)
