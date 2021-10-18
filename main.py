############### Blackjack Project #####################


# Created a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)



#Created a function called calculate_score() that takes a List of cards as input 
#and returns the score. 

def calculate_score(card):

  #Inside calculate_score() checked for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(card)==21 and len(card)==2:
    return 0

  #Inside calculate_score() checked for an 11 (ace). If the score is already over 21, removed the 11 and replaced it with a 1. 
  if 11 in card and sum(card)>21:
    card.remove(11)
    card.append(1)  

  return sum(card)

#Created a function called compare() and passed in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(u_score, c_score):
  if u_score==c_score:
    return "It is a draw"
  elif c_score==0:
    return " comp win"
  elif u_score==0:
    return "you win"
  elif u_score>21:
    return " you lose"
  elif c_score>21:
    return " comp lose"  
  elif u_score>c_score:
    return "you win"
  else:
    return " you lose"     

def play_game():    

  #Dealt the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  computer_cards = []
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())         


  #Called calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
  is_game_over=False
  #The score will need to be rechecked with every new card drawn 
  while is_game_over== False:
    user_score = calculate_score(user_cards)
    comp_score = calculate_score(computer_cards)
    print(f" your cards {user_cards} , current_score{user_score}")
    print(f"computer's first card {computer_cards[0]}")
    if comp_score==0 or user_score==0 or user_score>21:
      is_game_over= True
    #If the game has not ended, the user is asked if they want to draw another card. If yes, then the deal_card() function is used to add another card to the user_cards List. If no, then the game has ended.
    elif input("do you want to draw another card type yes:y or no:")=="y":
      user_cards.append(deal_card())
    else:
      is_game_over=True

  # Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while comp_score!=0 and comp_score<17:
    computer_cards.append(deal_card())
    comp_score= calculate_score(computer_cards)

  print(f"your final card{user_cards} your final score {user_score}")
  print(f"computer's hand{computer_cards} computer's final score {comp_score}")
  print(compare(user_score,comp_score))


# Asked the user if they want to restart the game. If they answer yes, start a new game of blackjack and show the logo from art.py.
from art import logo

while input(" Do you want to start the game and play blackjack type yes:y or no:")=="y":
  
  print(logo)
  play_game()
print(" Thankyou for playing The game is exit")  


