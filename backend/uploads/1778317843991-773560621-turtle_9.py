from turtle import Turtle,Screen, seth, setheading
screen = Screen()
a = Turtle()

def up():
    a.setheading(90)

def down():
    a.setheading(270)
    
def left():
    a.setheading(180)   
    
def right():
    a.setheading(0) 
    
def space():
    a.forward(20)
    
def reset():
    a.reset()
    a.home()
    
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(space, "space")
screen.onkey(reset, "Escape")

screen.listen()
screen.mainloop()