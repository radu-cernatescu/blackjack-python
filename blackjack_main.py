#imports from the BlackJack.py
from BlackJack import *
#the play variable is initialized
play="y"
#the player_name is initialized
player_name = raw_input("Please enter your name:")
#while the play variable is "y" the blackjack game is iterated
while play=="y":
    #an instance of BlackJack is created
    blackjack_game = BlackJack(player_name)
    #prints the welcome message
    print blackjack_game.showWelcome()
    #plays the Blackjack game
    blackjack_game.play()
    #Prints the winner of the blackjack game
    print blackjack_game.getWinner()
    #Asks the player is they would like to play again.
    play = raw_input("Would you like to play another hand(Y/N)?").lower()

#Prints a goodbye message
print "Thank you for playing!"

