#guess the number game 

import random

print("GUESS THE NUMBER GAME!!")

num = random.randint(1,50)

level = input("choose the level 'easy' or 'hard':\n ").lower()

if level == 'easy':
    tries = 10
    print("You have 10 tries to make the correct guess!!")
    
    while tries > 0:
        guess = int(input("Make a guess: "))
        
        if guess != num:
            tries -= 1
            print(f"Wrong guess, you are left with {tries} tries")
            if guess > num :
                print("Your guess is greater than the number")
            elif guess < num:
                print("Your guess is lesser than the number")
                
        else:
            print("Congratulations, You have guess the correct number!")
            break

    if tries == 0:
        print(f"You are out of tries and the correct number is {num}")

elif level == 'hard':
    tries = 5
    print("You have 5 tries to make the correct guess!!")
    
    while tries > 0:
        guess = int(input("Make a guess: "))
        
        if guess != num:
            tries -= 1
            print(f"Wrong guess, you are left with {tries} tries")
            if guess > num :
                print("Your guess is greater than the number")
            elif guess < num:
                print("Your guess is lesser than the number")
                
        else:
            print("Congratulations, You have guess the correct number!")
            break

    
    if tries == 0:
        print(f"You are out of tries and the correct number is {num}")

