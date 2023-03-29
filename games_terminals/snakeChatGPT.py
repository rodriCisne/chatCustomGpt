import random
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

# Inicializar la ventana de curses
curses.initscr()

# Obtener las dimensiones de la ventana
win = curses.newwin(20, 60, 0, 0)

# Habilitar el reconocimiento de teclas especiales (flechas, etc.)
win.keypad(True)

# Establecer el refresco a 100 ms
win.timeout(100)

# Establecer la posición inicial de la serpiente
snake_x = 30
snake_y = 10

# Crear la serpiente inicial (3 caracteres)
snake = [[snake_y, snake_x], [snake_y, snake_x-1], [snake_y, snake_x-2]]

# Crear la fruta en una posición aleatoria
fruit = [10, 20]
win.addch(fruit[0], fruit[1], curses.ACS_PI)

# Establecer la dirección inicial (hacia la derecha)
key = KEY_RIGHT

# Iniciar el bucle principal
while True:
    # Obtener la tecla presionada
    next_key = win.getch()
    key = key if next_key == -1 else next_key

    # Si la serpiente toca el borde, perder
    if snake[0][0] in [0, 19] or snake[0][1] in [0, 59] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    # Establecer la nueva posición de la cabeza
    new_head = [snake[0][0], snake[0][1]]
    if key == KEY_DOWN:
        new_head[0] += 1
    if key == KEY_UP:
        new_head[0] -= 1
    if key == KEY_LEFT:
        new_head[1] -= 1
    if key == KEY_RIGHT:
        new_head[1] += 1
    snake.insert(0, new_head)

    # Si la serpiente come la fruta, crear una nueva fruta y aumentar la longitud de la serpiente
    if snake[0] == fruit:
        fruit = None
        while fruit is None:
            new_fruit = [random.randint(1, 18), random.randint(1, 58)]
            fruit = new_fruit if new_fruit not in snake else None
        win.addch(fruit[0], fruit[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        win.addch(tail[0], tail[1], ' ')

    # Dibujar la serpiente
    win.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
    
