import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

if response.status_code != 200:
    raise Exception("Bad Response from API")

data = response.json()
print(data)

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

print(f"{latitude}, {longitude}")