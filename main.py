import requests
import os
from dotenv import load_dotenv
load_dotenv()
params = {
    "lat": 25.192181,
    "lon": 75.850838,
    "appid": os.getenv('API_KEY'),
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)
print(response.json())
