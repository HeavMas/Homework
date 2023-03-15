import requests
import json

url = "https://rickandmortyapi.com/api/character"
response = requests.get(url, params={"page": 2})
data = json.loads(response.text)
for character in data["results"][14:74]:
    name = character["name"]
    planet = character["origin"]["name"]
    episodes = character["episode"]
    print(f"{name} {planet} {episodes}:")
