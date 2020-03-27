# Genius API Project
import json
import requests
from bs4 import BeautifulSoup

client_id = "your client id!"
client_secret = "your client secret!"
client_token = "your client token!"
base_url = 'https://api.genius.com/search'
headers = {'Authorization': 'Bearer ' + client_token}

def lyrics_from_song_api_path(song_api_path):
    song_url = base_url + song_api_path
    path = song_api_path
    #gotta go regular html scraping... come on Genius
    page_url = "http://genius.com" + path
    page = requests.get(page_url)
    html = BeautifulSoup(page.text, "html.parser")
    #remove script tags that they put in the middle of the lyrics
    [h.extract() for h in html('script')]
    #at least Genius is nice and has a tag called 'lyrics'!
    lyrics = html.find("div", class_="lyrics").get_text() #updated css where the lyrics are based in HTML
    return lyrics

def jsonReader(jsonFile):
    try:
        for key, value in jsonFile.items():
            print(f"|KEY:{key} | VALUE:{value}\n")
    except:
        print("Input is not a JSON/DICT object")


def request_song_info(song_title, artist_name):
  data = {'q': f"{song_title} {artist_name}"}
  response = requests.get(base_url, data=data, headers=headers)
  return response.json()

song = input("Enter a song: ")
artist = input("Enter the artist: ")

"DATA OBJECTS"
# JSON/DICT Object
api_test = request_song_info(song, artist)
# JSON/DICT Object
api_testReponse = api_test["response"]
# LIST Object
api_responseHits = api_testReponse["hits"]
# JSON/DICT Object
main_info = api_responseHits[0]
# JSON/DICT Object
main_info_result = main_info["result"]

# API Paths
song_api_path = main_info_result["api_path"]

# Music Data
lyric_url_path = main_info_result["path"]
title = main_info_result["title"]
featured_artists = main_info_result["title_with_featured"]
full_lyrics = lyrics_from_song_api_path(song_api_path)



print(full_lyrics)

input()









#
