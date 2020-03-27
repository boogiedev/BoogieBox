from bjdeck import *

class BlackJackPlayer:
    """
    CLASS INIT
    """
    def __init__(self, name:str) -> None:
        self.hand = []
        self.name = name
        self.numAces = 0
        self.handTotal = 0
        self.isBusted = False
        self.has21 = False
        self.hasBJ = False
    """
    CLASS RESETTERS
    """
    def resetHand(self) -> None:
        self.hand = []

    """
    CLASS GETTERS
    """
    def getHandTotal(self) -> int:
        total = 0
        if self.hand:
            total = sum([x.numVal for x in self.hand])
            if self.numAces:
                j = [total]
                for i in range(1, self.numAces + 1):
                    j.append(total - 10*i)
                for pos in j:
                    if pos == 21:
                        total = 21
                        break
                    else:
                        pass



        self.handTotal = total

    def getNumAces(self) -> int:
        total = 0
        for x in self.hand:
            if x.isAce:
                total += 1
        self.numAces = total

    """
    CLASS METHODS
    """

    'ADD CARD TRIGGERS ALL INTERNAL METHODS'
    def addCard(self, card:object) -> None:
        self.hand.append(card)
        self.getNumAces()
        self.getHandTotal()
        self.update21()
        self.isBusted = self.isOver21(self.handTotal)


    def showPrettyHand(self) -> None:
        val_lst = [str(x.val) + " " * (2 -len(str(x.val))) for x in self.hand]
        symb_list = [x.suitSymbol + " " for x in self.hand]
        n = len(self.hand)

        top_b = " _____________________ " * n
        top_v = "".join([f"|  {x}                 |" for x in val_lst])
        bot_v = "".join([f"|                 {x}  |" for x in val_lst])
        mid_v = "".join([f"|         {x}          |" for x in symb_list])
        fill = "|                     |" * n
        bot_b = "|_____________________|" * n


        card = [top_b, fill, top_v, fill, fill, fill, fill, mid_v, fill, fill, fill, fill, bot_v, bot_b]

        print(f"{self.name}\'S HAND | TOTAL: {self.handTotal}")
        print(("=" * 23) * n)

        for x in card:
            print(x)
        print(("-" * 23) * n)

    def isOver21(self, count:int) -> bool:
        return count > 21

    def update21(self) -> bool:
        if self.handTotal == 21:
            self.has21 = True
            if len(self.hand) == 2:
                self.hasBJ = True
                # print(f"{self.name} drew a Black Jack!")
