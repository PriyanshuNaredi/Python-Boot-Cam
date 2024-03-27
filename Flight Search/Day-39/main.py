#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


data_manager = DataManager()
sheet_data = data_manager.get_destinations()
flight_search = FlightSearch()
notification_manager = NotificationManager()


ORIGIN_CITY_IATA = "DEL"

print(sheet_data)

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_dest_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_dest_codes()
    
# Date & Time

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))


# Flight Search

for destinations in sheet_data:
    flight = flight_search.check_flight(
        ORIGIN_CITY_IATA,
        destinations["iataCode"],
        from_day= tomorrow,
        to_day= six_month_from_today        
    )
    if flight.price < destinations["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
    