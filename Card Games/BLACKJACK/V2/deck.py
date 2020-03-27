import random
from card import *
class Deck:
    not_empty = True
    suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    
    def __init__(self, number_of_decks):
        self.number_of_decks = number_of_decks
        self.cards = []
        self.build()

    def build(self) -> list:
        for i in range(self.number_of_decks):
            for suit in self.suits:
                for i in range(2,15):
                    self.cards.append(Card(i, suit))
    def shuffle(self) -> None:
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    def drawCard(self):
        try:
            return self.cards.pop()
        except:
            print("This deck has exhausted all of its cards")
            self.not_empty = False
            return self.getEmptyCard()
    def showDeck(self):
        for card in self.cards:
            print(card)
    def deckCount(self):
        return len(self.cards)

    def getEmptyCard(self):
        i = random.randint(0, 3)
        return Card(0, self.suits[i])
