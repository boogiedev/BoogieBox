
class Card:
    suits_symbols = ['♠', '♦', '♥', '♣']
    val_to_face_dict = {14:"A",13:"K",12:"Q",11:"J"}
    face_card_dict = {"A":"Ace", "K":"King", "Q":"Queen", "J":"Jack"}
    suits_to_symbol = {'Spades':'♠', 'Diamonds':'♦', 'Hearts':'♥', 'Clubs':'♣'}
    facedown = f"""
 _____________________
|                     |
| {":" * 19} |
| {":" * 19} |
| {":" * 19} |
| {":" * 19} |
| {":" * 19} |
| {":" * 19} |
| {":" * 19} |
| {":" * 19} |
| {":" * 19} |
| {":" * 19} |
| {":" * 19} |
| {":" * 19} |
|_____________________|
"""
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit
        self.symbol = self.suits_to_symbol[suit]
        self.is_face = self.val > 10
        self.face = self.getFace()

    def __repr__(self) -> str:
        if self.is_face:
            i = self.val_to_face_dict[self.val]
            if i in self.face_card_dict:
                val = self.face_card_dict[i.upper()]
        else:
            val = self.val
        return (f"{str(val).title()} of {self.suit}")

    def getFace(self):
        if self.is_face:
            return self.val_to_face_dict[self.val]
        return None

    def prettyCard(self) -> str:
        if self.is_face:
            val = self.face + " "
        else:
            val = str(self.val) + " " * (2 -len(str(self.val)))
        card = f"""
         _____________________
        |                     |
        |  {val}                 |
        |                     |
        |                     |
        |                     |
        |                     |
        |          {self.symbol}          |
        |                     |
        |                     |
        |                     |
        |                     |
        |                 {val}  |
        |_____________________|
        """
        #print(f"{str(self.val).title()} of {self.suit}")
        return card
