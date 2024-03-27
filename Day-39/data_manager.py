import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co///"

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
                "price":{
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",json=new_data)
            
            print(response.text)