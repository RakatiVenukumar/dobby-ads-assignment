import turtle

a = turtle.Turtle()
for i in range(10):
    l = ['red','blue','green','orange','yellow','purple','white','black']
    a.color(l[i])
    a.forward(10)
    a.penup()
    a.forward(10)
    a.pendown()
    i = i + 1
a.screen.mainloop()

