#Import from Deck.py, Player.py, Card.py
from Deck import *
from Player import *
from Card import *

#Blackjack class is initialized
class BlackJack(object):
    #The deck of the game is initialized
    gamedeck = Deck()

    #The __init__ method of the class is initialized with the player name
    def __init__(self, playerName):
        '''
        Initializes the game by
        - shuffling the deck
        - initializing a player1 (with given playerName) and dealer object (both are Player objects)
        '''
        #The deck is shuffled
        self.gamedeck.shuffle()
        #The player and dealer are initialized
        self.player1 = Player(playerName)
        self.dealer = Player("Dealer")

    #The getWinner method is defined
    def getWinner(self):
        '''
        returns the player object (either the class's player1 or dealer object) that is the winner
        based on their hands (closest to 21 without going over)

        return - Player object
        '''
        #The winner is returned based on the Blackjack score
        print "THE WINNER IS:"
        if self.player1.getBJScore()==21 or self.dealer.getBJScore()>21:
            return self.player1
        if self.dealer.getBJScore()==21 or self.player1.getBJScore()>21:
            return self.dealer
        if self.player1.getBJScore()>self.dealer.getBJScore() and self.player1.getBJScore()<22:
            return self.player1
        if self.dealer.getBJScore()>self.player1.getBJScore() and self.dealer.getBJScore()<22:
            return self.dealer
        if self.dealer.getBJScore()==self.player1.getBJScore():
            return self.dealer


    #The play method is defined
    def play(self):

        '''
        play the game using the class's deck, player1, and dealer objects
        '''

        '''
        initialize player1 and dealer hands (2 cards each)
        show player 1 hand
        player1 decision (hit or stand)
        dealer complete hand
        present game outcome - player1 win or lose
        '''
        #Adds two cards to the player's hand and to the dealer's hand
        self.player1.addToHand(self.gamedeck.takeCard())
        self.dealer.addToHand(self.gamedeck.takeCard())
        self.player1.addToHand(self.gamedeck.takeCard())
        self.dealer.addToHand(self.gamedeck.takeCard())
        #Gets the Blackjack score of the player
        self.player1.getBJScore()
        #Prints the player's information
        print self.player1
        #The hit variable is defined
        hit="hit"
        #while loop is iterated to give the player a card, as long as the hit variable is "hit"
        while hit=="hit":
            #The player is asked to input whether they want to hit or stand
            hit=raw_input("Hit or Stand?")
            #if player inputs his, another card is added, the blackjack score is gotten and the player's info is printed
            if hit.lower()=="hit":
                self.player1.addToHand(self.gamedeck.takeCard())
                self.player1.getBJScore()
                print self.player1
                #If the player gets higher than 21, the busted score is output
                if self.player1.getBJScore()>21:
                    print "You have BUSTED!"
                    hit="bust"
                #If the player gets 21, the gotten Blackjack message is gotten
                if self.player1.getBJScore()==21:
                    print "You have gotten BLACKJACK!"
                    hit="blackjack"
        #If the player busts, the dealer proceeds
        if hit!="bust":
            #While the dealer's black jack score is less than 17, he is forced to hit
            while self.dealer.getBJScore()<17:
                self.dealer.addToHand(self.gamedeck.takeCard())
                self.dealer.getBJScore()
                #If the dealer gets over 21, he gets the busted message
                if self.dealer.getBJScore()>21:
                    print "The dealer has BUSTED! \n"
                #If the dealer get 21, he gets the blackjack message
                if self.dealer.getBJScore()==21:
                    print "The dealer got blackjack!!!"

        #The blackjack score of the dealer is gotten
        self.dealer.getBJScore()
        #The dealer's info is printed
        print "The dealer's hand is:"
        print self.dealer

    #The showWelcome method is defined
    def showWelcome(self):
        '''
        outputs a welcome message to the the player
        '''
        #The welcome message is output
        return "{0}".format("Welcome "+self.player1.getName()+" to Black Jack!")