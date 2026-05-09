from turtle import Turtle,Screen

screen = Screen()
a = Turtle()

def forward():
    a.setheading(0)
    a.forward(20)

def backward():
    a.setheading(0)
    a.backward(20)

def up():
    a.setheading(90)
    a.forward(20)
    
def down():
    a.setheading(90)
    a.backward(20)
def left():
    a.circle(50,10)

def right():
    a.circle(-50,10)
    
def reset():
    a.reset()
    a.home()
    
screen.onkey(forward, "f")
screen.onkey(backward, "b")
screen.onkey(up, "u")
screen.onkey(down, "d")
screen.onkey(left, "l")
screen.onkey(right, "r")
screen.onkey(reset, "Escape")

screen.listen()
screen.mainloop()