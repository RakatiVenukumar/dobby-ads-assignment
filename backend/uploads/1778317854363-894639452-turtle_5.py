import random
from turtle import Turtle,colormode

colormode(255)
a  = Turtle()
a.shape('turtle')

for i in range(50):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    a.color(r,g,b)
    a.pensize(15)
    a.speed(0)
    a.setheading(random.randrange(0,360,90))
    a.forward(30)