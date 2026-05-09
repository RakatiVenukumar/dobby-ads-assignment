from turtle import Turtle

a = Turtle()

a.color("red",'blue')
a.begin_fill()
a.circle(100)
a.end_fill()
a.right(90)
a.penup()
a.forward(100)
a.pendown()
a.pensize(5)
a.color("red","orange")
a.begin_fill()
a.circle(50)
a.end_fill()

a.screen.mainloop()

