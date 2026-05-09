# snake, water and gun game
import random

def game(comp,player):
    if comp == player:
       return None
    elif comp=="s":
        if player == "w":
            return False
    elif player == "g":
       return True
 
    elif comp=="w":
        if player == "g":
            return False
    elif player == "s":
       return True  
 
    elif comp=="g":
        if player == "s":
            return False
    elif player == "w":
       return True
 
print("comp turn: snake(s) water(w) or gun(g?")
a = random.randint(1, 3)

if a == 1:
    comp = "s"
elif a == 2:
    comp = "w"
elif a == 3: 
    comp  = "g" 

  
player = input("snake(s) water(w) or gun(g?\n")
b = game(comp,player)

print(f" computer chose {comp}")
print(f" player chose {player}")

if b == None:
    print("the game is a tie")
elif b:
    print("you win!")
else:
    print("you lose!")    
    

  
    