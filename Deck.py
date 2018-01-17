from Card import *
import random

class Deck(object):
        """A deck of cards"""

        def __init__(self):
                """Initialize the deck of cards"""
                self.cards = []
                suits = ["c","d","h","s"]

                #generate the cards
                for suit in suits:
                        for rank in range(1,14):
                                self.cards.append(Card(rank,suit))

        def shuffle(self):
                """Shuffle the deck"""
                random.shuffle(self.cards)

        def __str__(self):
                deck_str = ""
                for card in self.cards:
                        deck_str = deck_str +"\n"+ card.__str__()

                return deck_str

        def getCard(self, rank, suit):
                """returns a card object of the specified rank a suit

                rank - an int from 1 to 13, where 1 is an Ace
                suit - one of 'c', 'd', 'h', or 's'

                return - Card
                """
                return Card(rank,suit)

        def getNthCard(self, n):
                """returns the nth card from the deck

                n - an int <= the size of the deck

                return - Card
                """
                return self.cards[n-1]

        def takeCard(self):
                """returns a card from the Deck and removes it from the deck
                """
                self.top_card = self.cards[0]
                self.cards.remove(self.cards[0])
                return self.top_card

        def reset(self):
                """ resets the deck so that the cards are grouped by suit and ordered by rank
                """
                self.cards = []
                suits = ["c","d","h","s"]

                #generate the cards
                for suit in suits:
                        for rank in range(1,14):
                                self.cards.append(Card(rank,suit))