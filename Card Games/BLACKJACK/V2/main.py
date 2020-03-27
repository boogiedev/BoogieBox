from deck import *
from dealer import *


def valueConverter(card):
    if card.val > 10:
        return 10
    else:
        return card.val

def handTotal(hand):
    aces, total = 0, 0
    for card in hand:
        if card.isAce:
            aces += 1
        else:
            total += valueConverter(card)
    possibleVals = []
    aceVals = [aces + 10*x for x in range(aces + 1)]
    for addAce in aceVals:
        possibleVals.append(total + addAce)
    best = []
    for val in possibleVals:
        if val == 21:
            return val
        elif val <= 21:
            best.append(val)
    if not best:
        return min(possibleVals)
    else:
        return max(best)







if __name__ == "__main__":
    deck = Deck(1)
    # lenDeck = len(deck.cards)
    # frmt = f"There are %s count of %ss"
    # print()
    # print(frmt%(lenDeck, "card"))
    # vals = [card.val for card in deck.cards]
    # for val in set(vals):
    #     print(frmt%(str(vals.count(val)), str(val)))
    ace = Card(14, "Spades")
    seven = Card(7, "Spades")
    ten = Card(10, "Spades")
    hand = [ace, ace, seven]
    hand2 = [ace, ace, ace, ace, ten, ten]
    hand3 = [ace,ten]
    hand4 = [seven, seven, ace, ace, ace]
    print(handTotal(hand4))
