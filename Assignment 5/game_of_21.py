# Created by Jenny Trac
# Created on Oct 31 2017
# Program lets you play game of 21 against the computer(dealer)
# uses unlimited number of cards from 1-10

import ui
from numpy import random

#constants and variables
user_card1 = random.randint(1, 10+1)
user_card2 = random.randint(1, 10+1)
user_total = user_card1 + user_card2
dealer_card1 = random.randint(1, 10+1)
dealer_card2 = random.randint(1, 10+1)
dealer_card3 = random.randint(1, 10+1)
dealer_total = dealer_card1 + dealer_card2 + dealer_card3

#show cards
showusercard1 = "Resources/card" + str(user_card1) + ".PNG"
view['usercard1_imageview'].image = ui.Image(showusercard1)

print("Utotal" + str(user_total))
print("dealtotal" + str(dealer_total))

def add_card_touch_up_inside(sender):
    # generates random card to add to user's cards
    
    global user_total
    
    new_card = random.randint(1, 10 + 1)
    user_total = user_total + new_card
    
    print("new" + str(new_card))
    print("Utotal" + str(user_total))
    
def check_card_touch_up_inside(sender):
    # checks who wins and shows the winner
    
    global user_total
    global dealer_total
    
    if (user_total > 21 and dealer_total > 21) or (user_total == dealer_total):
        view['result_label'].text = "You tied."
        
    elif (dealer_total <= 21 and user_total > 21) or (user_total < dealer_total and dealer_total <= 21):
        view['result_label'].text = "You lose."
    
    else:
        view['result_label'].text = "You win."
    
view = ui.load_view()
view.present('sheet')
