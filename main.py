from game.utils import Actions

# Con if __name__ == "__main__" → El juego solo se ejecuta si main.py se ejecuta directamente.
# __name__ es una variable especial que vale main si se ejecuta el archvio principal, pero si es importado se toma el nombre del archivo sin la extensión
if __name__ == "__main__":
    game_actions = Actions()  # Crea una instancia de la clase Actions
    game_actions.play() # Inicia el juego.
    memory_color = [] # tupla vacía para almacenar los colores generados
    while True:
        # invoco la función para genrar el color y lo guardo en una variable
        color = game_actions.generate_color()
        # Añado el color generado a la tupla
        memory_color.append(color)
        # Muestro los valores de la tupla al usuario
        game_actions.show_colors(memory_color)
        # Almaceno el color ingresado por el usuario
        color_user = game_actions.user_input()

        # Comparo si las dos tuplas son iguales
        if color_user != memory_color:
            print("Perdiste :(")
            break
