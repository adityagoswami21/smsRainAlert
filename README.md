## SMS Rain Alert System

This Python project fetches weather data from the [OpenWeatherMap API](https://openweathermap.org/api) and sends an SMS alert if it detects rain in the upcoming forecast using the [Twilio API](https://www.twilio.com/docs/usage/api).

## Features
- Retrieves weather forecast data for a specific location.
- Checks if it's likely to rain within the next four forecast periods.
- Sends an SMS notification to alert the user to bring an umbrella if rain is expected.

## Prerequisites
Before running the application, ensure you have the following:

- Python 3.11.7 installed on your machine.
- An account with [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) to get the API key.
- A [Twilio](https://www.twilio.com/) account to obtain your account_sid, auth_token, and phone numbers.
- A .env file to securely store environment variables.

## Installation

1. *Clone the repository:*

   bash
   git clone <your-repo-url>
   cd <your-project-directory>
   

2. *Create and activate a virtual environment (optional but recommended):*

   bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   

3. *Install dependencies:*

   bash
   pip install -r requirements.txt
   

4. **Create a .env file** in the root directory and add the following environment variables:

   env
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   FROM_NO=your_twilio_phone_number
   TO_NO=your_verified_phone_number
   API_KEY=your_openweathermap_api_key
   

## Usage

1. *Run the script:*

   bash
   python weather_notification.py
   

   The script will:

   - Fetch the weather forecast for the specified location (lat and lon).
   - Check if rain is expected within the next four forecast periods.
   - Send an SMS to your phone if rain is likely, reminding you to bring an umbrella.

## Code Explanation

1. *Fetching Weather Data:*
   The script uses the OpenWeatherMap API to fetch the forecast data for a specific location (latitude and longitude).

   python
   response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)
   weather_data = response.json()
   

2. *Checking for Rain:*
   It checks the weather conditions for each forecasted period and looks for weather IDs indicating rain (IDs < 700).

   python
   for ids in weather_data['list']:
       weather_id = ids['weather'][0]['id']
       if int(weather_id) < 700:
           will_rain = True
   

3. *Sending SMS:*
   If rain is detected, it sends an SMS using Twilio's API.

   python
   message = client.messages.create(
       body="It's going to rain today, Bring an umbrella!☔",
       from_=os.getenv("FROM_NO"),
       to=os.getenv("TO_NO")
   )
   

## Dependencies

- requests: For making HTTP requests to the OpenWeatherMap API.
- twilio: For sending SMS notifications.
- python-dotenv: For loading environment variables from a .env file.

Install them using:

bash
pip install requests twilio python-dotenv


## License

This project is licensed under the MIT License.
