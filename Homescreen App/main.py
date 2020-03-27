from weather import *
from user import *
from homescreen import *

# IMPORT VISUALS
from visuals import *

"""VISUALS OBJECT"""
visuals = Visuals()
"VISUAL CLASS FUNCS"
dprint = visuals.delay_print
clear = visuals.clear

"""
MAIN PROGRAM OBJECT INITS
"""

" USER INIT "
user = User()
userDict = user.infoDict
userCity = userDict["location"]["city"]
userRegion = userDict["location"]["region"]
userCountry = userDict["location"]["country"]

"""
HOMESCREEN AND WIDGETS
"""
" MAIN HOMESCREEN "
homescreen = HomeScreen()

" WEATHER WIDGET "
weather = WeatherWidget("408959dd477d10a2d5b6d2e57e0f10b6", userCity)
weatherDict = weather.infoDict
weatherMsg = weather.weatherMessage
#




if __name__ == "__main__":
    # inHomeScreen = True
    # while inHomeScreen:
    #     pass
    # print(userDict)
    # print(weatherDict)
    print(homescreen.home)
    curScreen = homescreen.createScreen("temperature", weatherDict)
    for x in curScreen:
        print(x)
    curScreen = homescreen.createScreen("location", userDict)
    for x in curScreen:
        print(x)
    curScreen = homescreen.createScreen("ip", userDict)
    for x in curScreen:
        print(x)
    pass
