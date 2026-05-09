import random
from turtle import Turtle,Screen

width,height = 500,500
colors = [ 'yellow',' gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue',' cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray']

def no_of_turtles():
    while True:
        n = int(input("Enter the number of turtles: "))
        if 2 <= n <= 10:
            return n
        else:
            print("Enter the number of turtles between 2 and 10")
            return no_of_turtles()
    
turtles = no_of_turtles()
print(turtles)
s = Screen()
s.setup(width,height)

space = width//(turtles+1)
turtle_list = []

for i in range(1,turtles+1):
    t = Turtle()
    t.shape("turtle")
    t.speed(0)
    t.color(random.choice(colors))
    t.penup()
    t.goto(-width//2 + (space*i), height//2)
    t.left(90)
    turtle_list.append(t)
    
def race():
    is_race_on = True
    while is_race_on:
        for t in turtle_list:
            t.forward(random.randint(1,20))
            
            x,y = t.position()
            if x >= width//2:
                print(f'Winner is {t.pencolor()} turtle')
                is_race_on = False
                
race()
          
s.mainloop()