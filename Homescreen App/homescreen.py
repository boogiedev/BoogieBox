class HomeScreen:

    SCRNDIMEN = (70, 14)
    SPACER = "=" * 70
    makeInfo = lambda x, y=66: "| " + x + (((abs(len(x) - y))) * " ") + " |"
    makeCenter = lambda x, y=68: ("|" + abs((abs(len(x) - y)//2)) * " " + x + abs((abs(len(x) - y)//2)) * " "  + "|") if len(x) % 2 == 0 else ("|" + abs((abs(len(x) - y)//2)) * " " + x + abs((abs(len(x) - y)//2)) * " "  + " |")

    welcome = "WELCOME TO THE HOMESCREEN"

    home = f"""
{SPACER}
{makeInfo("  ")}
{makeCenter(welcome)}
{makeInfo("  ")}
{makeInfo("  ")}
{makeInfo("  ")}
{makeInfo("  ")}
{makeInfo("  ")}
{makeInfo("  ")}
{makeInfo("  ")}
{makeInfo("  ")}
{makeInfo("  ")}
{makeInfo("  ")}
{SPACER}
"""

    def __init__(self):
        self.homeDisp = self.home

    def createScreen(self, key:str, data:dict) -> list:
        makeInfo = lambda x, y=66: "| " + x + (((abs(len(x) - y))) * " ") + " |"
        makeCenter = lambda x, y=68: ("|" + abs((abs(len(x) - y)//2)) * " " + x + abs((abs(len(x) - y)//2)) * " "  + "|") if len(x) % 2 == 0 else ("|" + abs((abs(len(x) - y)//2)) * " " + x + abs((abs(len(x) - y)//2)) * " "  + " |")


        dict_ = data[key]
        top = [self.SPACER, makeInfo("  "), makeCenter(key.upper()), makeInfo("  ")]
        bot = [makeInfo("  "), self.SPACER]

        for k, v in dict_.items():
            k = k.upper()
            row = makeInfo(f"{k}: {v}")
            top.append(row)

        filler = self.SCRNDIMEN[1] - (len(top) + len(bot))
        for i in range(filler):
            top.append(makeInfo("  "))
        screen = top + bot

        return screen
