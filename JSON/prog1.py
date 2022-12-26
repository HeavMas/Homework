"""
Выведите из файла character.json Имя персонажа,родную планету и список эпизодов в которых он появлялся.
"""
import json
from pprint import pprint

with open("character.json", "r") as read_file:
    data = json.load(read_file)
print(data['name'], data['location']['name'], data['episode'])