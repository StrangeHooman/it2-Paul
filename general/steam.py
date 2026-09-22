import requests
import json
import os
from pathlib import Path
from dotenv import load_dotenv

script_dir = Path(__file__).resolve().parent

load_dotenv(dotenv_path=script_dir/".env")

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

except requests.exceptions.RequestException as e:
    print("Error: ", e)


games = data["response"]["games"]
total_playtime = 0

ordered_playtime: list = []

for i in range(len(games)):
    self_info = (games[i]["name"], games[i]["playtime_forever"]/60)
    if len(ordered_playtime) == 0:
        ordered_playtime.append(self_info)

    else:
        for j in range(len(ordered_playtime)):
            if self_info[1] > ordered_playtime[j][1]:
                ordered_playtime.insert(j, self_info)
                break

            elif j == len(ordered_playtime)-1:
                ordered_playtime.append(self_info)

    total_playtime += games[i]["playtime_forever"]

print("Total wasted time:", total_playtime/60)

[print(ordered_playtime[i],"") for i in range(len(ordered_playtime))]