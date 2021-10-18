# Blackjack-Capstone
##It is a card game.
##The game is played between the user and the computer

############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

  #Firstly 2 cards are allotted to user and computer
  #The user cards and the sum of those cards is displayed The computers only first card is displayed
  #Then the user is aksed if they want to withdraw more card or no
  #If now the user says yes and withdraws a card and the sum goes above 21 the game there ends for the user and now it's computer's turn
  #If this is not the case then the user can still say yes and withdraw card
  #Also if the score of sum of user or computer is equal to 21 then it is a blackjack and the one having it wins. And it is denoted by returning zero vale
  #When the user is done the next turn is of the computer
  #The computer withdraws cards till it's score is less than 17
  #Finally the user score and computer score are compared
  # 1) user score==comp score
          #it is draw
  # 2) comp score==0
          # comp win
  # 3) user score ==0
          # user win
  # 4) user score > 21
          # user loose
  # 5) comp score > 21
          # user win 
  # 6) user score> comp score
          # user win
  # 7) comp score > user score
          # user loose       
             
  





