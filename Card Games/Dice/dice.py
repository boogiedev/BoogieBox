from random import randint
from dicerollLoops import *
from visuals import *


"""
MAIN PROGRAM FUNCTIONS
"""
def overHeadDisplay(func):
    def wrapped_func(*args):
        # Prints ascii title screen
        print("")
        print("")
        print("")
        print("     ▄████████    ▄████████    ▄████████  ▄█  ███▄▄▄▄    ▄██████▄ ")
        print("    ███    ███   ███    ███   ███    ███ ███  ███▀▀▀██▄ ███    ███")
        print("    ███    █▀    ███    ███   ███    █▀  ███▌ ███   ███ ███    ███")
        print("    ███          ███    ███   ███        ███▌ ███   ███ ███    ███")
        print("    ███        ▀███████████ ▀███████████ ███▌ ███   ███ ███    ███")
        print("    ███        ▀███████████ ▀███████████ ███▌ ███   ███ ███    ███")
        print("    ███    ███   ███    ███    ▄█    ███ ███  ███   ███ ███    ███")
        print("    ████████▀    ███    █▀   ▄████████▀  █▀    ▀█   █▀   ▀██████▀ ")
        print("")
        print("")
        print("   ▄████████    ▄████████    ▄████████    ▄███████▄    ▄████████")
        print("   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███")
        print("   ███    █▀    ███    ███   ███    ███   ███    ███   ███    █▀ ")
        print("   ███         ▄███▄▄▄▄██▀   ███    ███   ███    ███   ███       ")
        print("   ███        ▀▀███▀▀▀▀▀   ▀███████████ ▀█████████▀  ▀███████████")
        print("   ███    █▄  ▀███████████   ███    ███   ███                 ███")
        print("   ███    ███   ███    ███   ███    ███   ███           ▄█    ███")
        print("   ████████▀    ███    ███   ███    █▀   ▄████▀       ▄████████▀ ")
        print("                ███    ███                                       ")
        print("")
        print("")
        print("")
        return func() if args is None else func(*args)
        # if args is None:
        #     return func()
        # else:
        #     return func(*args)
    return wrapped_func




class Dice():
    """
CLASS SHARED ATTRIBUTES
    """
    roll_faces = {
    1:"""""",
    2:"""""",
    3:"""""",
    4:"""""",
    5:"""""",
    6:""""""
    }


    """
CLASS INIT/DATAMODEL
    """
    def __init__(self, pips:int) -> None:
        self.pips = pips

    def __repr__(self):
        dice_art = r"""
  ____
 /\' .\    _____
/: \___\  / .  /\
\' / . / /____/..\
 \/___/  \'  '\  /
          \'__'\/
"""
        return f"""
{dice_art}
This is a {self.pips} sided die
"""

    def __call__(self):
        self.animate_roll()
        return self.roll()

    """
CLASS GETTERS
    """
    def display_roll(self):
        pass

    """
CLASS METHODS
    """
    def roll(self) -> int:
        roll_val = randint(1, self.pips)
        self.display_roll(roll_val)
        print(f"Rolled a {roll_val}")
        return roll_val

    def animate_roll(self) -> None:
        timeout = time.time() + 1
        while time.time() < timeout:
            for face in dice_1_roll_loop:
                print(face)
                time.sleep(0.09)
                clear()
    @overHeadDisplay
    def display_roll(self, roll:int) -> None:
        # ascii dice (1-6)
        if roll == 6:
            print (" _______ ")
            print ("| *   * |")
            print ("| *   * |")
            print ("| *   * |")
            print (" ------- ")

        elif roll == 5:
            print (" _______ ")
            print ("| *   * |")
            print ("|   *   |")
            print ("| *   * |")
            print (" ------- ")

        elif roll == 4:
            print (" _______ ")
            print ("| *   * |")
            print ("|       |")
            print ("| *   * |")
            print (" ------- ")

        elif roll == 3:
            print (" _______ ")
            print ("| *     |")
            print ("|   *   |")
            print ("|     * |")
            print (" ------- ")

        elif roll == 2:
            print (" _______ ")
            print ("| *     |")
            print ("|       |")
            print ("|     * |")
            print (" ------- ")

        elif roll == 1:
            print (" _______ ")
            print ("|       |")
            print ("|   *   |")
            print ("|       |")
            print (" ------- ")




if __name__ == "__main__":
    dice_1 = Dice(6)
    # print(dice_1)

    dice_1()
