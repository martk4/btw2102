import turtle 
import os

wn = turtle.Screen ()
wn.title("recyclist by martk4")
wn.bgcolor("white")
wn.setup(width=375, height=800)
wn.tracer(0)

g = 0

# g_flask 

g_flask = turtle.Turtle ()
g_flask.speed(0)
g_flask.shape("circle")
g_flask.color("red")
#g_flask.shapesize(stretch_wid = 2, stretch_len = 1)
g_flask.penup()
g_flask.goto(0,500)
g_flask.dx = 0 
g_flask.dy = -9.81

# Swipe Function

def swiperight_green():
    x = g_flask.xcor()
    x +=100
    g_flask.setx(x)
# Keyboard binding

wn.listen()
wn.onkeypress(swiperight_green, "Right")

# Game Loop
while True:
    wn.update()

    # Move the flask
    g_flask.setx(g_flask.xcor() + g_flask.dx)
    g_flask.sety(g_flask.ycor() * g_flask.dy)

    # Swipe
    if swiperight_green:
        g_flask.setx(100)
        g_flask.dx *=-1
