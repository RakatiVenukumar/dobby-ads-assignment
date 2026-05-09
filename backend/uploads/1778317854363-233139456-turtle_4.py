import random
from turtle import Turtle

a = Turtle()
a.speed(3)

colors = [ 'yellow',' gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue',' cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray']

for i in range(3,8):
    angle = 360/i
    b = random.choice(colors)
    a.color(b)
    for j in range(i):
        a.forward(100)
        a.right(angle)
        
a.screen.mainloop()    