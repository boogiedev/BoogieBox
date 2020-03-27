from deck import *


class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name

    def clearHand(self):
        self.hand = []

    def showHand(self):
        val_lst = [x.face + " " if x.is_face else str(x.val) + " " * (2 -len(str(x.val))) for x in self.hand]
        symb_list = [x.symbol + " " for x in self.hand]
        n = len(self.hand)

        top_b = " _____________________ " * n
        top_v = "".join([f"|  {x}                 |" for x in val_lst])
        bot_v = "".join([f"|                 {x}  |" for x in val_lst])
        mid_v = "".join([f"|         {x}          |" for x in symb_list])
        fill = "|                     |" * n
        bot_b = "|_____________________|" * n


        card = [top_b, fill, top_v, fill, fill, fill, fill, mid_v, fill, fill, fill, fill, bot_v, bot_b]

        print(self.name + "\'S HAND")
        print(("=" * 23) * n)

        for x in card:
            print(x)
        print(("-" * 23) * n)

        
