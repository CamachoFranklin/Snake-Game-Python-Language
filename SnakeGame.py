# Importamos la librerias a utilizar
import turtle

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



# Función para mantener la ventana abierta
turtle.done()