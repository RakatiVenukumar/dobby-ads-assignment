from turtle import Turtle

a = Turtle()
def draw_square():
    for i in range(4):
        a.forward(100)
        a.left(90)

#circle
a.penup()
a.goto(-200,200)
a.pendown()
a.pensize(5)
a.color("red")
a.circle(50)


#square
a.penup()
a.goto(200,200)
a.pendown()
a.pensize(5)
a.color("blue")
for i in range(4):
        a.forward(100)
        a.left(90)


#triangle
a.penup()
a.goto(-200,-200)
a.pendown()
a.pensize(5)
a.color("orange")
for i in range(3):
        a.forward(100)
        a.left(120)
        

#pentagon
a.penup()
a.goto(200,-200)
a.pendown()
a.pensize(5)
a.color("green")
for i in range(5):
        a.forward(100)
        a.left(72)
        
a.screen.mainloop()     