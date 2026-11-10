import requests
import json
kaupunki=input("Anna paikkakunta: ")
api_key="c88b8e3ef5c97a3df487fc7b09b89f75"
#q=kaupunki,FI&appid=api_key
sää=f"https://api.openweathermap.org/data/2.5/weather?q={kaupunki},FI&appid=c88b8e3ef5c97a3df487fc7b09b89f75&units=metric"
Paikkakunta="http://api.openweathermap.org/geo/1.0/direct?q=" + kaupunki + "&limit=1&appid=c88b8e3ef5c97a3df487fc7b09b89f75&units=metric"
vastaus=requests.get(sää).json()
lämpötila=vastaus["main"]["temp"]
kuvaus=vastaus["weather"][0]["description"]
print(f"Paikkakunta: {kaupunki} ")
print(f"Säätila: {kuvaus}")
print(f"Lämpötila: {lämpötila}")

