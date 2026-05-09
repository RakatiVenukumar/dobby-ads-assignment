# Guess the number
print('''                                              
   ____  __ __   ____   ______ ______        
  / ___\|  |  \_/ __ \ /  ___//  ___/        
 / /_/  >  |  /\  ___/ \___ \ \___ \         
 \___  /|____/  \___  >____  >____  >        
/_____/             \/     \/     \/         
    __  .__                                  
  _/  |_|  |__   ____                        
  \   __\  |  \_/ __ \                       
   |  | |   Y  \  ___/                       
   |__| |___|  /\___  >                      
             \/     \/                       
                        ___.                 
      ____  __ __  _____\_ |__   ___________ 
     /    \|  |  \/     \| __ \_/ __ \_  __ \
    |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
    |___|  /____/|__|_|  /___  /\___  >__|   
         \/            \/    \/     \/       ''')

import random

print("GUESS THE NUMBER GAME!!")

num = random.randint(1,50)

def guess_the_number():
    tries = int(input("enter the tries: "))
    print(f"You have {tries} number of tries")

    while tries > 0:
        guess = int(input("Make a guess: "))
        
        if guess == num:
            print("Congratulations, You have guess the correct number!")
            break
        
        else:
            tries -= 1
            print(f"Wrong guess, you are left with {tries-1} tries")
            if guess > num :
                print("Your guess is greater than the number")
            elif guess < num:
                print("Your guess is lesser than the number")

    if tries == 0:
        print(f"You are out of tries and the correct number is {num}")
        
        
level = input("choose the level 'easy' or 'hard':\n ")

if level == 'easy':
    guess_the_number()
    
elif level == 'hard':
    guess_the_number()
    