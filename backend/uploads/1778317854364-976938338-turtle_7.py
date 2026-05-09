import random
from turtle import Turtle,colormode
a = Turtle()
a.shape('classic')
a. speed(0)
colormode(255)

for i in range(74):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    a.color(r,g,b)
    a.circle(100)
    a.left(5)
  
a.screen.mainloop()
