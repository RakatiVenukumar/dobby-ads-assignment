import os 

print('''       .__.__                 __               
  _____|__|  |   ____   _____/  |_             
 /  ___/  |  | _/ __ \ /    \   __\            
 \___ \|  |  |_\  ___/|   |  \  |              
/____  >__|____/\___  >___|  /__|              
     \/             \/     \/                  
                        __  .__                
  _____   __ __   _____/  |_|__| ____   ____   
  \__  \ |  |  \_/ ___\   __\  |/  _ \ /    \  
   / __ \|  |  /\  \___|  | |  (  <_> )   |  \ 
  (____  /____/  \___  >__| |__|\____/|___|  / 
       \/            \/                    \/  
                                               
        _________    _____   ____              
       / ___\__  \  /     \_/ __ \             
      / /_/  > __ \|  Y Y  \  ___/             
      \___  (____  /__|_|  /\___  >            
     /_____/     \/      \/     \/             ''')

print('WELCOME TO SILENT AUCTION GAME!!')

def bid_winner(bidder_details):
    highest_bid = 0
    winner = ''
    for i in bidder_details: #name
        bid_price = bidder_details[i]  #bid_price
        if highest_bid < bid_price: 
            highest_bid = bid_price
            winner = i
    print(f"the winner is {winner} and the bid price is {highest_bid}")

dict1 = {}
end = True
while end:
    name = input("Enter the name of the bidder: ")
    bid = int(input("Enter the bid price: "))
    dict1[name] = bid
    a = input("Enter 'yes' to continue and 'no' to exit:\n ")   
    if a == 'no':
        end = False
        bid_winner(dict1)
    elif a == 'yes':
        os.system('cls')
