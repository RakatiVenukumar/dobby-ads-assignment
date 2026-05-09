# hangman game!!!

import random

print(''' .__                                                 
|  |__ _____    ____    ____   _____ _____    ____  
|  |  \\__  \  /    \  / ___\ /     \\__  \  /    \ 
|   Y  \/ __ \|   |  \/ /_/  >  Y Y  \/ __ \|   |  \
|___|  (____  /___|  /\___  /|__|_|  (____  /___|  /
     \/     \/     \//_____/       \/     \/     \/ 
                                                    
   _________    _____   ____                        
  / ___\__  \  /     \_/ __ \                       
 / /_/  > __ \|  Y Y  \  ___/                       
 \___  (____  /__|_|  /\___  >                      
/_____/     \/      \/     \/        ''')

print("WELCOME TO HANGMAN GAME!!!")

l1 = ['venu','girish','kedhar','vikram','pranav','sravya','deepankar','akshitha','vindhya','varsha']

word = random.choice(l1)

list1 = list(word)
 
list2 = ["_"] * len(word)
print(list2)

count = 6
while count > 0:
    guess = input("guess the letter: ")
    
    if guess in list1:
        print("correct guess!")
        
        for i in range(len(word)):
            if word[i] == guess:
                list2[i] = guess
        print(list2)
        
        if "_" not in list2:
            print("Congratulations, You have guessed the correct word!!")
            break
        
    else:
        count -= 1
        print("wrong guess")
        print(f"you have left with {count} tries")
        
if(count==0):
    print(f"you are out of tries the word is {word}")
