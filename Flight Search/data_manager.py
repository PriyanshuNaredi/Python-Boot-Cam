import requests
from pprint import pprint






class DataManager:
    
    def __init__(self):
        self.destination_data = {}
    
    def get_destinations(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_dest_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
    
    def get_customer_emails(self):
        customers_endpoint = SHEET_USERS_ENDPOINT
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data    
    
    

