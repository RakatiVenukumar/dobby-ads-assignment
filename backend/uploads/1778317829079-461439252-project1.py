# rock paper scissor
 
import random

print('''                       __                      
_______  ____   ____ |  | __                  
\_  __ \/  _ \_/ ___\|  |/ /                  
 |  | \(  <_> )  \___|    <                   
 |__|   \____/ \___  >__|_ \                  
                   \/     \/                  
                                              
 ___________  ______   ___________            
 \____ \__  \ \____ \_/ __ \_  __ \           
 |  |_> > __ \|  |_> >  ___/|  | \/           
 |   __(____  /   __/ \___  >__|              
 |__|       \/|__|        \/                  
                .__                           
    ______ ____ |__| ______ _________________ 
   /  ___// ___\|  |/  ___//  ___/  _ \_  __ \
   \___ \\  \___|  |\___ \ \___ (  <_> )  | \/
  /____  >\___  >__/____  >____  >____/|__|   
       \/     \/        \/     \/             ''')

a = ('''choose 0 for rock
          1 for paper
          2 for scissor :''' )

def game(comp,user):
    if (user == comp):
        return None
    elif (user == 2 and comp == 0):
        return False
    elif ( user == 0 and comp == 2):
        return True
    elif (int(comp) > int(user)):
        return False
    elif (int(comp) < int(user)):
        return True
        
comp = print("comp's turn: choose 0 1 or 2?")
a = random.randint(0,2)
if (a == 0):
    comp = 0
elif (a == 1):
    comp = 1
else:
    comp = 2

user = input("choose 0 1 or 2?")
b = game(comp,user)

print(f"computer choose {comp}")
print(f"user choose {user}")

if (b == None):
    print("the game is a tie")
elif ( b == True):
    print("user wins")
elif (b == False):
    print("computer wins")
    