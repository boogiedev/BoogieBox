import json
import re
from urllib.request import urlopen
from typing import List

class User:
    dataCol = ["location", "ip"]
    messages = []

    """
CLASS INIT
    """
    def __init__(self):
        self.infoDict = self.updateDict()

    """
CLASS GETTERS
    """
    def getLocation(self) -> List[tuple]:
        url = 'http://ipinfo.io/json'
        response = urlopen(url)
        data = json.load(response)

        city = data['city']
        country = data['country']
        region = data['region']

        # print( 'Your IP detail\n ')
        # print( 'IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP))

        return [("city",city), ("region",region), ("country",country)]

    def getIPInfo(self) -> List[tuple]:
        url = 'http://ipinfo.io/json'
        response = urlopen(url)
        data = json.load(response)

        IP = data['ip']
        org = data['org']

        return [("IP",IP), ("ORG",org)]

    """
CLASS FUNCTIONS
    """
    def updateDict(self) -> None:
        dict_ = {}
        categories = [self.getLocation, self.getIPInfo]
        for i in range(len(self.dataCol)):
            sub_dict = {data[0]:data[1] for data in categories[i]()}
            dict_[self.dataCol[i]] = sub_dict
        return dict_
