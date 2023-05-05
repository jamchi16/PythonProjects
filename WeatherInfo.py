import requests
from pprint import pprint

API_key = 'e3e06807f4892429442173b80098e75d'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
