# Modificado por:
# Autor: Sergio Adolfo Sanoja Hernández
# Autor: Fabián Castillo Rodríguez

from turtle import *
import turtle
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()                # Pull the pen up.
    turtle.seth(0)      # Turn the head to view at 0 degrees.
    goto(start.x, start.y)
    down()              # Pull the pen down, start drawing.
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    turtle.seth(0)
    goto(start.x, start.y)
    down()
    begin_fill()                # Start filling the drawn shape.
    
    # Traces the square by calculating its length and turning 90 degrees 4 times.
    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()                  # Stop filling the drawn shape.

def circle(start, end):
    "Draw circle from start to end."
    up()
    goto(end.x, end.y)
    radius = ((end.x - start.x)/2)        # Define the radius of the circle.
    turtle.seth(90)                       # Turn the head to view at 90 degrees.
    down()
    begin_fill()
    turtle.circle(radius)                 # Start drawing the circle from the radius.
    end_fill()

def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    turtle.seth(0)
    goto(start.x, start.y)
    down()
    begin_fill()

    # Traces the rectangle by calculating its lengths and turning 90 degrees 4 times.
    for count in range(2):      
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    up()
    turtle.seth(0)
    goto(start.x, start.y)
    down()
    begin_fill()
    
    # Traces the triangle by calculating its length and turning 120 degrees 3 times.
    for count in range(3):
        forward(end.x - start.x)
        left(120)
        
    end_fill()

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}      # 
setup(420, 420, 370, 0)                     # 
onscreenclick(tap)                          # 
listen()                                    # 
onkey(undo, 'u')                            # 

# Defines the keys to change the color of the shape.
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')

# Defines the shape drawn.
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()