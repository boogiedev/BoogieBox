from bjdealer import *
sys.path.append('C:/Users/wesle/PyScripts/Universal Classes')
from visuals import *
from blackjacktext import *

"""VISUAL INIT"""
visual = Visuals()
clear = visual.clear
"CHANGE THIS LATER BITCH"
# print = visual.delay_print





"GAME METHODS"
def dealToAll(playerDict:dict) -> None:
    global DECK
    for _ in range(2):
        for player in playerDict:
            card = DECK.drawCard()
            playerDict[player].addCard(card)



def checkPlayersForBJ(playerDict:dict) -> None:
    if not checkDealerForBJ(playerDict["Dealer"]):
        for x in playerDict:
            player = playerDict[player]
            if x.hasBJ:
                print(f"{x.name} has a Black Jack!")

def checkDealerForBJ(dealer:object) -> bool:
    if dealer.hasBJ:
        dealer.flipCard()
        showTable(playerDict)
        print("Tough Luck! The dealer has a Black Jack!")
        return True
    else:
        return False

def showTable(playerDict:dict) -> None:
    clear()
    for player in playerDict:
        playerDict[player].showPrettyHand()


def hitCard(player:object) -> None:
    global DECK
    card = DECK.drawCard()
    player.addCard(card)

def hitLoop(player:object) -> None:
    prompt = "\nPress Enter To Hit | Type Anything To Stay\n"
    if not player.hasBJ and not DEALER.hasBJ:
        x = input(prompt)
        while x == "":
            hitCard(player)
            clear()
            showTable(playerDict)
            print(player.handTotal)
            if player.isBusted:
                print("You busted!")
                break
            x = input(prompt)

# INITIALIES GAME WITH PROMPTS
def gameINIT() -> tuple:
    print(welcome)
    print(askName)
    z = input()
    x = inputNumber(askDeckCount)
    y = inputNumber(askPlayerCount)
    return x, y, z

# SETS UP TABLE WITH DEALER, PLAYERS AND PLAYER POSITION AS GLOBAL VALUES
def makePlayerList() -> None:
    pass
def makePlayerDict(numPlayers=None, mainPlayer="Main Player(You)") -> dict:
    j = {}
    j["Dealer"] = BlackJackDealer()
    if numPlayers is not None:
        for i in range(1, numPlayers):
            player = f"Player {i}"
            j[player] = BlackJackPlayer(player)
    j[mainPlayer] = BlackJackPlayer(mainPlayer)
    return j

def inputNumber(message):
    while True:
        print(message)
        userInput = input()
        if userInput == "":
            return None
            break
        try:
            userInput = int(userInput)
            if userInput > 10:
                print("Please choose a number between 1 and 10.")
        except ValueError:
            print("Please enter a number. Try again.")
            continue
        else:
            return userInput
            break




if __name__ == "__main__":
    """DECK PLAYER INIT"""
    DECKCOUNT, NUMPLAYERS, USERNAME = gameINIT()
    DECK = BlackJackDeck(DECKCOUNT)
    # SHUFFLE DECK
    DECK.shuffle()
    """TABLE(PLAYER) INIT"""
    playerDict = makePlayerDict(NUMPLAYERS, USERNAME)
    # GLOBAL PLAYER OBJECT INIT
    DEALER = playerDict["Dealer"]
    PLAYER = playerDict[USERNAME]

    aceH = BlackJackCard("A", "Hearts")
    kingH = BlackJackCard("K", "Hearts")
    threeH = BlackJackCard(3, "Hearts")
    PLAYER.addCard(aceH)
    PLAYER.addCard(kingH)
    PLAYER.addCard(threeH)

    PLAYER.showPrettyHand()
    print(PLAYER.handTotal)






    """TESTING AREA"""
    # DECK.showDeck()
    # print(DECK.getDeckCount())
    #
    # aceH = BlackJackCard("A", "Hearts")
    # kingH = BlackJackCard("K", "Hearts")
    # dealer.addCard(aceH)
    # dealer.addCard(kingH)

    # P1.addCard(aceH)
    # P1.addCard(aceH)
    #
    # dealToAll()
    # showTable()
    # checkPlayersForBJ()
    #
    #
    #
    # hitLoop()
    #
    #
    # print(DECK.getDeckCount())


    # print(playerDict)
    #
    # # TESTING MAIN GAME LOOP
    # dealToAll(playerDict)
    # showTable(playerDict)
    # for name, player in playerDict.items():
    #     if name != "Dealer":
    #         hitLoop(player)
    # DEALER.flipCard()
    # showTable(playerDict)
