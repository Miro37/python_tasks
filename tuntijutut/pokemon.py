import requests
import json
kysely=input("Hae pokemonia: ")

haku=(f"https://pokeapi.co/api/v2/pokemon/{kysely.lower()}/")
vastaus=requests.get(haku)
if vastaus.status_code == 200:
    vastaus=vastaus.json()
    print(f"Nimi: " ["name"])



