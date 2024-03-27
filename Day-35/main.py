import requests
from twilio.rest import Client

API_KEY = "74afe4fd9b71d0631fa74804c1f63775"
account_sid = "ACaa38a9714a33546e063b885ccc1f9acc"
auth_token = "347ea8ab8687eee23764f7d281303ce5"

parameters = {
    "lat": -4.156770,
    "lon": 12.658655,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hr_data in weather_data["list"]:
    condition_code = hr_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Its Going to rain today ", from_='+12404340466',  to='+919340587377')

    # print(message.sid)
    print(message.status)
