import random
from bjcard import *

class BlackJackDeck:

    suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    faces = ["A", "K", "Q", "J"][::-1]

    """
    CLASS INIT
    """
    def __init__(self, number_of_decks=None) -> None:
        self.number_of_decks = number_of_decks
        if self.number_of_decks is None:
            self.number_of_decks = 8
        self.cards = []
        self.build()
        self.isEmpty = False

    def build(self) -> None:
        for i in range(self.number_of_decks):
            for suit in self.suits:
                for i in range(2,11):
                    self.cards.append(BlackJackCard(i, suit))
                for face in self.faces:
                    self.cards.append(BlackJackCard(face, suit))

    def shuffle(self) -> None:
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    """
    CLASS GETTERS
    """
    def showDeck(self) -> None:
        for card in self.cards:
            print(card)
    def getDeckCount(self) -> None:
        return len(self.cards)

    def getEmptyCard(self) -> None:
        i = random.randint(0, 3)
        return BlackJackCard(0, self.suits[i])

    """
    CLASS METHODS
    """
    def drawCard(self) -> object:
        self.isEmpty = bool(self.cards)
        if self.isEmpty:
            return self.cards.pop()
        else:
            print("This deck is out of cards!")
