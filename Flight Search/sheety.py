import requests
import sheety

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/1976f4a69865ccc81fec7e1a97c8843d/copyOfFlightDeals/users"
BEARER = "Pn"


print("Welcome to Flight Club.\nWe find the best flight deals and email them to you.")

first_name = input("What is your first name? ").title()
last_name = input("What is your last name? ").title()

email1 = "email1"
email2 = "email2"
while email1 != email2:
    email1 = input("What is your email? ")
    if email1.lower() == "quit" \
            or email1.lower() == "exit":
        exit()
    email2 = input("Please verify your email : ")
    if email2.lower() == "quit" \
            or email2.lower() == "exit":
        exit()

print("OK. You're in the club!")

headers = {
    "Authorization": f"Bearer {BEARER}",
    # "Content-Type": "application/json",
}

body = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email1,
    }
}

response = requests.post(url=SHEETY_PRICES_ENDPOINT,
                         headers=headers, json=body)
response.raise_for_status()
print(response.text)

