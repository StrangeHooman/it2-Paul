import requests
import json
import os
from pathlib import Path
from dotenv import load_dotenv

script_dir = Path(__file__).resolve().parent

load_dotenv(dotenv_path=script_dir/"apis.env")

steam_api = os.environ.get("STEAM_API")
steam_ID_64 = os.environ.get("STEAM_ID_64")

url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"

params = {
    "key" : steam_api,
    "steamid" : steam_ID_64,
    "format": "json",
    "include_appinfo": 1,
    "include_played_free_games": 1
}

print(params)

try:
    response = requests.get(url, params=params)

    response.raise_for_status()

    print(type(response))

    data = response.json()

    print(data)

except requests.exceptions.RequestException as e:
    print("Error: ", e)


games = data["response"]["games"]
total_playtime = 0

for i in range(len(games)):
    total_playtime += games[i]["playtime_forever"]

print("Total wasted time:", total_playtime)