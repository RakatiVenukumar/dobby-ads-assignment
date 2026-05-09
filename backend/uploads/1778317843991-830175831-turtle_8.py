import random
from turtle import Turtle,colormode

a = Turtle()
colormode(255)
a. speed(0)

for i in range(100):
    a.dot(20)
    a.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    a.penup()
    a.goto(random.randrange(-360,360),random.randint(-360,360))
    a.dot(20)
    a.pendown()
a.screen.mainloop()

