import sys
from os import system, name


def clear():
  if name == "nt":
    _ = system("cls")
  else:
    _ = system("clear")

def dealCards(deck, players):
    for _ in range(2):
        for player in players:
            player.hand.append(deck.drawCard())

def hitCard(deck, player,players):
    print(f"{player.name}, it is your action, would you like to hit? ")
    hitting = True
    while hitting:
        choice = input("Press enter to hit or type \"S\" to stay: ")
        if choice.lower() == "s":
            hitting = False
            continue
        else:
            player.hand.append(deck.drawCard())
            clear()
            showAllHands(players)
    print("Your action is over")

def showAllHands(players):
    for player in players:
        player.showHand()

def getTotal(player):
    count = 0
    for card in player.hand:
        if card.val > 10:
            count += 10
        else:
            count += card.val
    return count
def isBusted(count):
    return count > 21

if __name__ == "__main__":
    from blackjack import *



    playing = True
    while playing:
        deck = Deck(1)
        deck.shuffle()
        dealer = Dealer("DEALER")
        player = Player("PLAYER")

        players = [dealer,player]

        print("Welcome to BlackJack, where the house always wins!\n")
        print("Just play by pressing enter! ")
        input()
        dealCards(deck, players)

        showAllHands(players)

        hitCard(deck, player,players)
        player_total = getTotal(player)
        if isBusted(player_total):
            print("You have busted buster! Let the house hol dat money real quick ")
        else:
            print(f"{player.name}\'s total is {str(player_total)}")
        input()

        dealer.flipCard()
        dealer_total = getTotal(dealer)
        print(dealer_total)
        while dealer_total < 17:
            print(f"{dealer.name}\'s total is {str(dealer_total)}")
            print(f"{player.name}\'s total is {str(player_total)}")
            if not isBusted(dealer_total):
                dealer.hand.append(deck.drawCard())
                dealer_total = getTotal(dealer)
                showAllHands(players)
                input("Enter to continue ")
                clear()
        clear()
        print(f"{dealer.name}\'s total is {str(dealer_total)}")
        print(f"{player.name}\'s total is {str(player_total)}")
        showAllHands(players)
        input("Play again?")
