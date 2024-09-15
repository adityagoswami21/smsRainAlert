import requests
import os
from dotenv import load_dotenv
load_dotenv()
params = {
    "lat": 23.344101,
    "lon": 85.309563,
    "appid": os.getenv('API_KEY'),
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)
weather_data = response.json()
will_rain = False
weather_ids = []
for ids in weather_data['list']:
    weather_id = ids['weather'][0]['id']
    # print(weather_id)
    weather_ids.append(int(weather_id))
print(weather_ids)
