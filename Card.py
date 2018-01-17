class Card(object):
    '''
    An object representing a card
    '''

    def __init__(self, rank, suit):
        '''
        Create an instance of a card
        '''

        self.rank = rank
        self.suit = suit


    def getRank(self):
        '''
        Return the rank of the card
        '''

        return self.rank

    def getSuit(self):
        '''
        Return the suit of the card
        '''

        return self.suit

    def BJValue(self):
        '''
        Return the BlackJack rank of the card
        '''

        if self.rank <= 10:
            return self.rank

        elif self.rank >=11:
            return 10

    def __str__(self):
        '''
        Return the card's suit and rank in a string
        '''

        string = ""

        if self.rank == 1:
            string = "Ace of "
        elif self.rank >= 2 and self.rank <= 10:
            string = str(self.rank) + " of "
        elif self.rank == 11:
            string = "Jack of "
        elif self.rank == 12:
            string = "Queen of "
        else:
            string = "King of "

        #Outputs the suit of the card in a string
        if self.suit == "d":
            string = string + "Diamonds"
        elif self.suit == "c":
            string = string + "Clubs"
        elif self.suit == "h":
            string = string + "Hearts"
        else:
            string = string + "Spades"

        return string