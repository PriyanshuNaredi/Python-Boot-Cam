from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import html


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
    
destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)

for destination_code in destinations:
    flight = flight_search.check_flight(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    print(flight.price)
    if flight is None:
        continue

    if flight.price < destinations[destination_code]["price"]:

        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = f"Low price alert! Only ₹{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        message += f"Link: {flight.booking_link}"
        
        notification_manager.send_emails(emails, message)



    
# # Date & Time

# tomorrow = datetime.now() + timedelta(days=1)
# six_month_from_today = datetime.now() + timedelta(days=(6 * 30))


# # Flight Search

# for destinations in sheet_data:
#     flight = flight_search.check_flight(
#         ORIGIN_CITY_IATA,
#         destinations["iataCode"],
#         tomorrow,
#         six_month_from_today        
#     )
#     print(flight.price)
#     if flight is None:
#         continue

#     if flight.price < destinations["price"]:

#         users = data_manager.get_customer_emails()
#         emails = [row["email"] for row in users]
#         names = [row["firstName"] for row in users]

#         message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

#         if flight.stop_overs > 0:
#             message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

       
#         notification_manager.send_emails(emails, message)


    #
    
    # if flight is None:
    #     continue
    
    # if flight.price < destinations["lowestPrice"]:
    #     message = f"Low price alert! Only ₹{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

    #     if flight.stop_overs > 0:
    #         message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
    #         print(message)

    #     # notification_manager.send_sms(message)
    #     # print(message)
    