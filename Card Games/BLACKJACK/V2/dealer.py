from player import *
class Dealer(Player):

    hideCard = True

    def showHand(self):
        val_lst = [x.face + " " if x.is_face else str(x.val) + " " * (2 -len(str(x.val))) for x in self.hand]
        symb_list = [x.symbol + " " for x in self.hand]
        n = len(self.hand)

        cover = "| ::::::::::::::::::: |"
        top_b = " _____________________ " * n
        fillx = "|                     |" * n
        bot_b = "|_____________________|" * n
        fill = "|                     |" * n

        if self.hideCard:
            top_v = f"|  {val_lst[0]}                 |" + cover
            bot_v = f"|                 {val_lst[0]}  |" + cover
            mid_v = f"|         {symb_list[0]}          |" + cover
            fill = "|                     |" + cover

        else:
            top_v = "".join([f"|  {x}                 |" for x in val_lst])
            bot_v = "".join([f"|                 {x}  |" for x in val_lst])
            mid_v = "".join([f"|         {x}          |" for x in symb_list])

        card = [top_b, fillx, top_v, fill, fill, fill, fill, mid_v, fill, fill, fill, fill, bot_v, bot_b]
        # FINAL PRINTING
        print(self.name + "\'S HAND")
        print(("=" * 23) * n)
        for x in card:
            print(x)
        print(("-" * 23) * n)

    def flipCard(self):
        self.hideCard = not self.hideCard
