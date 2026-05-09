# Higher lower game

print('''.__    .__       .__                  
|  |__ |__| ____ |  |__   ___________ 
|  |  \|  |/ ___\|  |  \_/ __ \_  __ \
|   Y  \  / /_/  >   Y  \  ___/|  | \/
|___|  /__\___  /|___|  /\___  >__|   
     \/  /_____/      \/     \/       
   .__                                
   |  |   ______  _  __ ___________   
   |  |  /  _ \ \/ \/ // __ \_  __ \  
   |  |_(  <_> )     /\  ___/|  | \/  
   |____/\____/ \/\_/  \___  >__|     
                           \/         
                                      
         _________    _____   ____    
        / ___\__  \  /     \_/ __ \   
       / /_/  > __ \|  Y Y  \  ___/   
       \___  (____  /__|_|  /\___  >  
      /_____/     \/      \/     \/   ''')
print("WELCOME TO HIGHER LOWER GAME!!")

import random

data = [

        {
            'Name':'Virat Kohli',
            'Followers':267,
            'Description':'Cricketer',
            'Country':'India'
        },
        
        {
            'Name':'Rohit Sharma',
            'Followers':178,
            'Description':'Cricketer',
            'Country':'India'
        },
        
        {
            'Name':'Narendra Modi',
            'Followers':220,
            'Description':'Politician',
            'Country':'India'
        },
        
        {
            'Name':'Christiano Ronaldo',
            'Followers':433,
            'Description':'Footballer',
            'Country':'Portugal'
        },
        
        {
            'Name':'Lionel Messi',
            'Followers':389,
            'Description':'Footballer',
            'Country':'Argentina'
        }, 
        
]

def winner(guess,follower_1,follower_2):
    if follower_1 >= follower_2:
        if guess == 1:
            return True
        else:
            return False
    elif follower_1 <= follower_2:
        if guess == 2:
            return True
        else:
            return False

score = 0
end = True
while end:   
    a = random.choice(data)
    b = random.choice(data)

    print(f"Compare 1: {a['Name']}, a {a['Description']}, from {a['Country']}")
    print(f"Compare 2: {b['Name']}, a {b['Description']}, from {b['Country']}")
        
    guess = int(input("who has more followers: 1 or 2\n "))

    follower_count_1 = a['Followers']
    follower_count_2 = b['Followers']

    check_winner = winner(guess,follower_count_1,follower_count_2)
    print(check_winner)

    if check_winner == False:
        end = False
        break
    elif check_winner == True:
        score += 1
        print(f"You're right! Current score: {score}")

print(f"You lose. Final score: {score}")

if score < 5:
    print("you can do better ")
elif score > 5 and score < 10:
    print("you are doing great")
elif score > 10:
    print("you are amazing")
        