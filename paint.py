# Código modificado por:
# Autor: Sergio Adolfo Sanoja Hernández
# Autor: Fabián Castillo Rodríguez

from turtle import *
import turtle
from freegames import vector


def line(start, end):
    """
    Draw a line from start to end.
    """
    up()                # Pull the pen up.
    turtle.seth(0)      # Turn the head to view at 0 degrees.
    goto(start.x, start.y)
    down()              # Pull the pen down, start drawing.
    goto(end.x, end.y)


def square(start, end):
    """
    Draw a square from start to end.
    """
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
    """
    Draw a circle from start to end with radius (end.x - start.x)/2.
    """
    up()
    goto(end.x, end.y)
    radius = ((end.x - start.x)/2)        # Define the radius of the circle.
    turtle.seth(90)                       # Turn the head to view at 90 degrees.
    down()
    begin_fill()
    turtle.circle(radius)                 # Start drawing the circle from the radius.
    end_fill()


def rectangle(start, end):
    """
    Draw a rectagle from start to end.
    """
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
    """
    Draw a triangle from start to end.
    """
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
    """"
    Store starting point or draw shape.
    """
    start = state['start']
    # Checks if its the first or second tap.
    if start is None:
        state['start'] = vector(x, y)   # Defines in the state, the starting point.
    else:
        shape = state['shape']          # Defines the state's shape as the selected one.
        end = vector(x, y)              # Defines the ending point.
        shape(start, end)               # Assigns the start and end point to the shape.
        state['start'] = None           # Resets the 'start' value.


def store(key, value):

    "Store value in state at key."
    state[key] = value                 #  Defines the  selected value in state.

state = {'start': None, 'shape': line}     # Sets the inicial values in state.
setup(420, 420, 370, 0)                    # Sets the size and position of the main window.
onscreenclick(tap)                         # Calls the "tap" function on screen click.
listen()                                   # Prepares the turtle to receive directions.
onkey(undo, 'u')                           # Erases the last drawn shape.


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