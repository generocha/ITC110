'''
This class represents a playing card
it will contain a number and suit
Gene Rocha
12/2/2019
'''
class Card():
    # Class initiallization. Pass in
    # and set the values
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = 0

    # get suit value
    def getSuit(self):
        return self.suit

    # get rank value
    def getRank(self):
        return self.rank

    # set the playing value of the card
    def setValue(self):
        if self.rank > 10:
            self.value = 10
        else:
            self.value = self.rank
        return self.value

    # convert suit letter to name
    def getSuit(self):
        self.s = ""
        if self.s == 'd':
            self.s = 'Diamonds'
        elif self.suit == 'h':
            self.s = 'Hearts'
        elif self.suit == 'c':
            self.s = 'Clubs'
        else:
            self.s = 'Spades'
        return self.s

    # return a string with the name of card
    def __str__(self):
        if self.rank > 1 and self.rank < 11:
            self.name = str(self.rank) + " of " + self.getSuit()
        if self.rank == 1:
            self.name = 'The Ace of ' + self.getSuit()
        if self.rank == 11:
            self.name = 'The Jack of ' + self.getSuit()
        if self.rank == 12:
            self.name = 'The Queen of ' + self.getSuit()
        if self.rank == 13:
            self.name = 'The King of ' + self.getSuit()
        return self.name