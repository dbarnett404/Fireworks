import turtle
import random
import math

WIDTH = 700
HEIGHT = 700
pen = turtle.Turtle()
screen = turtle.getscreen()
drawing = False

"""
Draws the firework on a left mouse click
The radius and points can be any sensible number (within reason) 
Python will make a random number between the range
"""
def draw_fireworks(x, y):
    if not drawing:
        radius = random.randrange(25, 100)
        points = random.randrange(25, 50)
        firework(x, y, radius, points)

"""
Does the actual drawing!
"""
def firework(x, y, radius, points):
    #The global variagble stops it drawing until it is finished
    global drawing
    drawing= True
    #This could be any amount of colours you like!
    colors = ['red', 'orange', 'green', 'blue', 'indigo', 'violet']
    #Picks a randomn colour
    color_index = random.randrange(len(colors))
    pen.color(colors[color_index])
    pen.goto(x, y)
    pen.pendown()
    for i in range(points):
        pen.goto(x, y)
        pen.pendown()
        #Works out the maths to calculate a point on a circle
        x1 = x + radius * math.cos(2 * math.pi * i / points)
        y1 = y + radius * math.sin(2 * math.pi * i / points)
        pen.goto(x1, y1)
        pen.penup()
    drawing = False


def setup():
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor('black')
    screen.listen()
    pen.penup()
    pen.speed(0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    setup()
    screen.onscreenclick(draw_fireworks, 1)
    screen.mainloop()
