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

def add_card_touch_up_inside(sender):
    # generates random card to add to user's cards
    
    global user_total
    global addcard_button
    
    # process
    user_card3 = random.randint(1, 10 + 1)
    user_total = user_total + user_card3
    
    # output
    showusercard3 = "Resources/card" + str(user_card3) + ".PNG"
    view['usercard3_imageview'].image = ui.Image(showusercard3)
    view['usertotal_label'].text = "Total: " + str(user_total)
    
    # disable button
    view['addcard_button'].enabled = False
    
def check_card_touch_up_inside(sender):
    # checks who wins and shows the winner
    
    global user_total
    global dealer_total
    global addcard_button
    global check_button
    
    showdealercard1 = "Resources/card" + str(dealer_card1) + ".PNG"
    showdealercard2 = "Resources/card" + str(dealer_card2) + ".PNG"
    showdealercard3 = "Resources/card" + str(dealer_card3) + ".PNG"
    view['dealercard1_imageview'].image = ui.Image(showdealercard1)
    view['dealercard2_imageview'].image = ui.Image(showdealercard2)
    view['dealercard3_imageview'].image = ui.Image(showdealercard3)
    
    view['dealertotal_label'].text = "Total: " + str(dealer_total)
    
    if (user_total > 21 and dealer_total > 21) or (user_total == dealer_total):
        view['result_label'].text = "You tied."
        
    elif (dealer_total <= 21 and user_total > 21) or (user_total < dealer_total and dealer_total <= 21):
        view['result_label'].text = "You lose."
    
    else:
        view['result_label'].text = "You win."
    
    # disable button
    view['addcard_button'].enabled = False
    view['check_button'].enabled = False

view = ui.load_view()
view.present('sheet')

#show cards
showusercard1 = "Resources/card" + str(user_card1) + ".PNG"
showusercard2 = "Resources/card" + str(user_card2) + ".PNG"
showdealercard1 = "Resources/cardback.PNG"
showdealercard2 = "Resources/cardback.PNG"
showdealercard3 = "Resources/cardback.PNG"
view['usercard1_imageview'].image = ui.Image(showusercard1)
view['usercard2_imageview'].image = ui.Image(showusercard2)
view['dealercard1_imageview'].image = ui.Image(showdealercard1)
view['dealercard2_imageview'].image = ui.Image(showdealercard2)
view['dealercard3_imageview'].image = ui.Image(showdealercard3)

#show user total
view['usertotal_label'].text = "Total: " + str(user_total)
