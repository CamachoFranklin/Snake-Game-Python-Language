# Importamos las librerias a utilizar
import turtle
import time

# Se crea una variable que indicará el tiempo en que se moverá la serpiente
retraso = 0.1

# Se crea el lienzo donde estará corriendo el juego
screen = turtle.Screen()

# Se le dan las dimensiones a la pantalla
screen.setup(650 , 650)

# Se le coloca el color al fondo
screen.bgcolor('grey')

# Cambiamos el nombre a la ventana
screen.title('Snake Game "La culebrita" - Proyecto Programacion III (Grupo 5)')

# Se crea el objeto de la serpiente (snake)
serpiente = turtle.Turtle()

# Se le asigna la velocidad de movimiento a la serpiente
serpiente.speed(1)

# Se le asigna la forma a la serpiente en este caso 'square' = cuadrado
serpiente.shape('square')

# Se usa la función penup para que la "Serpiente" no vaya a dibujar el rastro por donde pasa
serpiente.penup()

# Se posiciona la serpiente en el centro de la ventana
serpiente.goto(0 , 0)

# Función que se usará para que la serpiente no se pueda mover
serpiente.direction = 'stop'

# Se le asigna el color a la serpiente
serpiente.color('green')

# Se crea la función de movimiento
def movimiento():

    # Se crea la condición para el caso en que la serpiente se mueva hacia arriba
    if serpiente.direction == 'up':

        # La función ycord devuelve la coordenada de la serpiente en el eje Y
        y = serpiente.ycord()

        # La función sety mueve un objeto en el eje Y, a la posición actual se le suman 20 pixeles.
        serpiente.sety(y + 20)

    # Se crea la condición para el caso en que la serpiente se mueva hacia abajo
    if serpiente.direction == 'down':

        # La función ycord devuelve la coordenada de la serpiente en el eje Y
        y = serpiente.ycord()

        # La función sety mueve un objeto en el eje Y, a la posición actual se le restan 20 pixeles.
        serpiente.sety(y - 20)

    # Se crea la condición para el caso en que la serpiente se mueva hacia la derecha
    if serpiente.direction == 'right':

        # La función xcord devuelve la coordenada de la serpiente en el eje X
        x = serpiente.xcord()

        # La función setx mueve un objeto en el eje X, a la posición actual se le suman 20 pixeles.
        serpiente.setx(x + 20)

    # Se crea la condición para el caso en que la serpiente se mueva hacia arriba
    if serpiente.direction == 'left':

        # La función xcord devuelve la coordenada de la serpiente en el eje X
        x = serpiente.xcord()

        # La función setx mueve un objeto en el eje X, a la posición actual se le restan 20 pixeles.
        serpiente.setx(x - 20)

# Ciclo que actualiza la pantalla con cada movimiento de la serpiente
while True:

    # Actualizamos la pantalla con cada movimiento de la serpiente
    screen.update()

    # Se hace uso de la función movimiento
    movimiento()

    # Se agrega un delay al movimiento de la serpiente
    time.sleep(retraso)

# Función para mantener la ventana abierta
turtle.done()