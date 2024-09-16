import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
params = {
    "lat": 23.344101,
    "lon": 85.309563,
    "appid": os.getenv('API_KEY'),
    "cnt": 4
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)
weather_data = response.json()
# print(weather_data)
will_rain = False
weather_ids = []
for ids in weather_data['list']:
    weather_id = ids['weather'][0]['id']
    # print(weather_id)
    weather_ids.append(int(weather_id))
    if int(weather_id) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella!")
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="It's going to rain today, Bring an umbrella!☔",
                        from_=os.getenv("FROM_NO"),
                        to=os.getenv("TO_NO")
                    )

    print(message.status)