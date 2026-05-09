from turtle import Turtle


a = Turtle()
a.shape('classic')
a. speed(0)
a.color("red","yellow")
a.begin_fill()

for i in range(37):
    a.forward(100)
    a.forward(100)
    a.right(170)
a.end_fill()
    
a.screen.mainloop()