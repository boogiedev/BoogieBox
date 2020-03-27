import json
import requests

class WeatherWidget:
    SUP = str.maketrans("*", "⁰")

    # Base URL
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"
    # Messages
    msg = [
"""

CITY ENTERED: %s
CODE: %s
MESSAGE: %s

ENTER A VALID CITY OR WAIT FOR SERVER (IF CITY IS VALID)

""",
"""

- INFORMATION -
CITY: %s
COUNTRY: %s

- TEMPERATURE -
WEATHER: %s
KELVIN: %s
FAHRENHEIT: %s
CELSIUS: %s

"""
]

    """
    CLASS INIT
    """
    def __init__(self, api_key:str, curCity:str):
        self.api_key = api_key
        self.curCity = curCity
        self.rawData = self.callAPI()
        self.infoDict = self.frmtInfoDict(self.rawData)



        self.weatherMessage = self.msg[1] % (self.infoDict["area"]["city"], self.infoDict["area"]["country"], self.infoDict["temperature"]["WEATHER"], str(self.infoDict["temperature"]["KELVIN"]) + "*".translate(self.SUP), str(self.infoDict["temperature"]["FAHRENHEIT"]) + "*".translate(self.SUP), str(self.infoDict["temperature"]["CELSIUS"]) + "*".translate(self.SUP))



    def getURL(self, city) -> str:
        # Create complete URL
        return self.baseUrl + "appid=" + self.api_key + "&q=" + city


    """
    CLASS FUNCTIONS
    """
    def callAPI(self, city=None) -> dict:
        if city is None:
            city = self.curCity
        # Get response object
        response = requests.get(self.getURL(city))
        # Convert Response Object into json (a dictionary so we can see the info)
        converted = response.json()
        return converted

    def frmtInfoDict(self, raw_data) -> dict:
        weatherData = raw_data["weather"][0]
        tempData = raw_data["main"]

        curWeather = weatherData["description"]
        curTemp = tempData["temp"]


        dict_ = {
        "temperature":{"KELVIN":curTemp, "FAHRENHEIT":round(1.8 * round(curTemp - 273) + 32, 2), "CELSIUS":round(curTemp - 273, 2), "WEATHER":curWeather.title()},
        "area": {"city":raw_data["name"], "country":raw_data["sys"]["country"]}}

        return dict_


    def findTemp(self) -> None:
        # User input for city name
        city = input("ENTER A CITY: ").title()
