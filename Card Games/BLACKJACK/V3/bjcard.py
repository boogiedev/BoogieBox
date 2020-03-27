import sys
sys.path.append('C:/Users/wesle/PyScripts/Universal Classes/Cards')

from officialCard import Card

class BlackJackCard(Card):

    def __init__(self, val, suit):
        self.faceToNum = {"A":11,"K":10,"Q":10,"J":10}
        super().__init__(val, suit)
