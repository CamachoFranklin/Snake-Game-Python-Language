# Importamos las librerias a utilizar
import turtle
import time
import random

# Se crea una variable que indicará el tiempo en que se moverá la serpiente
retraso = 0.1

# Se crea la variable marcador
puntaje = 0

# Se crea la variable para el puntaje más alto
puntajeAlto = 0

# Se crea el lienzo donde estará corriendo el juego
screen = turtle.Screen()

# Se le dan las dimensiones a la pantalla
screen.setup(650 , 650)

# Se le coloca el color al fondo
screen.bgcolor('black')

# Cambiamos el nombre a la ventana
screen.title('Snake Game "La culebrita" - Proyecto Programacion III (Grupo 5)')

# La función tracer mejora la animación en pantalla
screen.tracer(0)

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
serpiente.color('white')

# Se instancia el objeto de "comida"
comida = turtle.Turtle()

# Se le asigna la forma a la comida en este caso 'circle' = circulo
comida.shape('circle')

# Se le asigna el color a la comida
comida.color('red')

# Se usa la función penup para que la "comida" no vaya a dibujar el rastro por donde pasa
comida.penup()

# Se envia la comida al punto dado al comienzo del juego
comida.goto(0 , 100)

# Se agrega una rapidez de 0 a la comida
comida.speed(0)

# Se crea una lista (vector) vacío que contendrá el cuerpo.
cuerpo = []

# Se crea un objeto llamado texto
texto = turtle.Turtle()

# Se le asigna la velocidad de 0 al texto
texto.speed(0)

# Se le asigna el color al color al texto
texto.color('white')

# Se usa la función penup para que el texto no vaya a dibujar el rastro por donde pasa
texto.penup()

# Se oculta el icono del objeto 
texto.hideturtle()

# Se asigna la posición estática
texto.goto(0 , -260)

""" Se hace uso de la función write que muestra un mensaje, le agrega una posición y además
asigna el tipo de fuente, su tamaño y en caso de no existir la fuente seleccionada, ocupa
la por defecto """
texto.write("Puntaje: 0\tPuntaje más alto: 0", align = "center", font=("verdana", 12, "normal"))

# Se crea la función que va a determinar el movimiento hacia arriba
def arriba():

    # Se le asigna el movimiento hacia arriba a la variable
    serpiente.direction = 'up'

# Se crea la función que va a determinar el movimiento hacia arriba
def abajo():

    # Se le asigna el movimiento hacia abajo a la variable
    serpiente.direction = 'down'

# Se crea la función que va a determinar el movimiento hacia la derecha
def derecha():

    # Se le asigna el movimiento hacia la derecha a la variable
    serpiente.direction = 'right'

# Se crea la función que va a determinar el movimiento hacia la izquierda
def izquierda():

    # Se le asigna el movimiento hacia la izquierda a la variable
    serpiente.direction = 'left'

# Se crea la función de movimiento
def movimiento():

    # Se crea la condición para el caso en que la serpiente se mueva hacia arriba
    if serpiente.direction == 'up':

        # La función ycor devuelve la coordenada de la serpiente en el eje Y
        y = serpiente.ycor()

        # La función sety mueve un objeto en el eje Y, a la posición actual se le suman 20 pixeles.
        serpiente.sety(y + 20)

    # Se crea la condición para el caso en que la serpiente se mueva hacia abajo
    if serpiente.direction == 'down':

        # La función ycor devuelve la coordenada de la serpiente en el eje Y
        y = serpiente.ycor()

        # La función sety mueve un objeto en el eje Y, a la posición actual se le restan 20 pixeles.
        serpiente.sety(y - 20)

    # Se crea la condición para el caso en que la serpiente se mueva hacia la derecha
    if serpiente.direction == 'right':

        # La función xcor devuelve la coordenada de la serpiente en el eje X
        x = serpiente.xcor()

        # La función setx mueve un objeto en el eje X, a la posición actual se le suman 20 pixeles.
        serpiente.setx(x + 20)

    # Se crea la condición para el caso en que la serpiente se mueva hacia arriba
    if serpiente.direction == 'left':

        # La función xcor devuelve la coordenada de la serpiente en el eje X
        x = serpiente.xcor()

        # La función setx mueve un objeto en el eje X, a la posición actual se le restan 20 pixeles.
        serpiente.setx(x - 20)

# La función Listen prepara la pantalla para una interacción del teclado
screen.listen()

# onkeypress recibe por parametro la función que activará al presionar la tecla indicada
screen.onkeypress(arriba, "Up")
screen.onkeypress(abajo, "Down")
screen.onkeypress(derecha, "Right")
screen.onkeypress(izquierda, "Left")

# Ciclo que actualiza la pantalla con cada movimiento de la serpiente
while True:

    # Actualizamos la pantalla con cada movimiento de la serpiente
    screen.update()

    # Se crea la condición que indica, que sí la serpiente choca con los bordes de la pantalla
    # Se reinicia el juego
    if (serpiente.xcor() > 300 or
    serpiente.xcor() < -300 or
    serpiente.ycor() > 300 or
    serpiente.ycor() < -300):
        
        # Se congela la pantalla por dos segundos
        time.sleep(2)

        # Se recorre la lista "cuerpo"
        for i in cuerpo:

            # Se elimina cada uno de los objetos creados en los espacios de la lista
            i.clear()

            # Se oculta el objeto
            i.hideturtle()

        # Se envia la serpiente al punto inicial
        serpiente.home()

        # Se le indica a la serpiente que debe permanecer estática
        serpiente.direction = 'stop'

        # Se elimina el cuerpo
        cuerpo.clear()

        # Se reinicia el puntaje
        puntaje = 0

        # Se limpia el texto
        texto.clear()

        # Se actualizan los puntajes
        texto.write(f"Puntaje: {puntaje}\tPuntaje más alto: {puntajeAlto}",
        align="center",
        font=("verdana", 12, "normal"))

    # Se crea un ciclo que genera coordenadas (x,y) aleatorias si la comida y la serpiente tienen contacto
    if serpiente.distance(comida) < 20:

        # Se genera el valor aleatorio de la coordenada "X"
        x = random.randint(-250 , 250)
        
        # Se genera el valor aleatorio de la coordenada "Y"
        y = random.randint(-250 , 250)

        # La comida es enviada a las coordenadas aleatorias dentro de los limites
        comida.goto(x , y)

        # Se instancia el objeto de "nuevoCuerpo"
        nuevoCuerpo = turtle.Turtle()

        # Se le asigna la forma al nuevoCuerpo en este caso 'square' = cuadrado
        nuevoCuerpo.shape('square')

        # Se le asigna el color al nuevoCuerpo
        nuevoCuerpo.color('gray')

        # Se usa la función penup para que el "nuevoCuerpo" no vaya a dibujar el rastro por donde pasa
        nuevoCuerpo.penup()

        # Se envia al nuevoCuerpo al punto dado al comienzo del juego
        nuevoCuerpo.goto(0 , 0)

        # Se agrega una rapidez de 0 a la nuevoCuerpo
        nuevoCuerpo.speed(0)

        # Se le agrega a la lista "Cuerpo" el objeto "Nuevo cuerpo"
        cuerpo.append(nuevoCuerpo)
        
        # Por cada comida que tenga contacto con la serpiente se suman 10 puntos
        puntaje += 10

        # Si el puntaje actual, es mayor al puntaje más alto, se cumple la siguiente sentencia
        if puntaje > puntajeAlto:

            # Si se cumple la condición se actualiza el puntaje alto
            puntajeAlto = puntaje
            
            # Se limpia el texto
            texto.clear()

            # Se actualizan los puntajes
            texto.write(f"Puntaje: {puntaje}\tPuntaje más alto: {puntajeAlto}",
            align="center",
            font=("verdana", 12, "normal"))

        # Si el puntaje actual, es menor al puntaje más alto, se cumple la siguiente sentencia
        if puntaje < puntajeAlto:

            # Se limpia el texto
            texto.clear()

            # Se actualizan los puntajes
            texto.write(f"Puntaje: {puntaje}\tPuntaje más alto: {puntajeAlto}",
            align="center",
            font=("verdana", 12, "normal"))

    # Se crea una variable "total" que devuelva la medida del cuerpo
    total = len(cuerpo)

    # Se crea un ciclo for para recorrer la lista "Cuerpo"
    # La lectura comienza a la inversa, obviando la posición 0 y contando de 1 en 1.
    for i in range(total - 1, 0, -1):

        # Se obtiene la coordenada "X" del nuevo objeto, es decir del nuevo cuerpo de la serpiente
        x = cuerpo[i - 1].xcor()

        # Se obtiene la coordenada "X" del nuevo objeto, es decir del nuevo cuerpo de la serpiente
        y = cuerpo[i - 1].ycor()

        # Se envía el nuevo cuerpo a la par de la serpiente 
        cuerpo[i].goto(x , y)

    # Si existe más de un elemento en la lista "cuerpo"
    if total > 0:
        
        # Se obtiene la coordenada "X" del objeto serpiente
        x = serpiente.xcor()

        # Se obtiene la coordenada "Y" del objeto serpiente
        y = serpiente.ycor()

        # Se envia el cuerpo a dicha coordenada
        cuerpo[0].goto(x , y)

    # Se hace uso de la función movimiento
    movimiento()

    # Se crea el ciclo, para validar la colisión contra el cuerpo
    for i in cuerpo:
        
        # Si uno de los segmentos de la lista "cuerpo" se toca con "serpiente"
        if i.distance(serpiente) < 20:

            # Se recorre nuevamente la lista "cuerpo"
            for i in cuerpo:

                # Se elimina cada uno de los objetos creados en los espacios de la lista
                i.clear()

                # Se oculta el objeto
                i.hideturtle()
            
            # Se envia a la serpiente a la posición inicial
            serpiente.home()

            # Se "elimina" el "cuerpo" que es basicamente limpiar la lista.
            cuerpo.clear()

            # Se le indica a la serpiente que debe permanecer estática
            serpiente.direction = 'stop'

            # Se reinicia el puntaje
            puntaje = 0

            # Se limpia el texto
            texto.clear()

            # Se actualizan los puntajes
            texto.write(f"Puntaje: {puntaje}\tPuntaje más alto: {puntajeAlto}",
            align="center",
            font=("verdana", 12, "normal"))

    # Se agrega un delay al movimiento de la serpiente
    time.sleep(retraso)

# Función para mantener la ventana abierta
turtle.done()