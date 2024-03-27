import pprint
import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "://-..com"
TEQUILA_API_KEY = "-eJ-IACRe54jbK"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_dest_code(self,city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code
    
    # def check_flight(self, origin_city_code, destination_city_code, from_time, to_time):
    #     print(f"Check flights triggered for {destination_city_code}")
    #     headers = {"apikey": TEQUILA_API_KEY}
    #     query = {
    #         "fly_from": origin_city_code,
    #         "fly_to": destination_city_code,
    #         "date_from": from_time.strftime("%d/%m/%Y"),
    #         "date_to": to_time.strftime("%d/%m/%Y"),
    #         "nights_in_dst_from": 7,
    #         "nights_in_dst_to": 30,
    #         "flight_type": "round",
    #         "one_for_city": 1,
    #         "max_stopovers": 0,
    #         "curr": "INR"
    #     }

    #     response = requests.get(
    #         url=f"{TEQUILA_ENDPOINT}/v2/search",
    #         headers=headers,
    #         params=query,
    #     )

    #     try:
    #         data = response.json()["data"][0]
    #     except IndexError:

    #         ##########################
    #         query["max_stopovers"] = 1
    #         response = requests.get(
    #             url=f"{TEQUILA_ENDPOINT}/v2/search",
    #             headers=headers,
    #             params=query,
    #         )
    #         data = response.json()["data"][0]
    #         pprint(data)
    #         flight_data = FlightData(
    #             price=data["price"],
    #             origin_city=data["route"][0]["cityFrom"],
    #             origin_airport=data["route"][0]["flyFrom"],
    #             destination_city=data["route"][1]["cityTo"],
    #             destination_airport=data["route"][1]["flyTo"],
    #             out_date=data["route"][0]["local_departure"].split("T")[0],
    #             return_date=data["route"][2]["local_departure"].split("T")[0],
    #             stop_overs=1,
    #             via_city=data["route"][0]["cityTo"],
    #         )
    #         return flight_data
    #         ###########################
    #     else:
    #         flight_data = FlightData(
    #             price=data["price"],
    #             origin_city=data["route"][0]["cityFrom"],
    #             origin_airport=data["route"][0]["flyFrom"],
    #             destination_city=data["route"][0]["cityTo"],
    #             destination_airport=data["route"][0]["flyTo"],
    #             out_date=data["route"][0]["local_departure"].split("T")[0],
    #             return_date=data["route"][1]["local_departure"].split("T")[0],
    #         )

    #         return flight_data

            
    def check_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        print(f"Check flights triggered for {destination_city_code}")
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 30,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        # print(response.json())
        
        try:
            data = response.json()["data"][0]
        except IndexError:

            ########################
            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=headers,
                params=query,
            )
            data = response.json()["data"][0]
            # pprint(data)
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"],
                booking_link= data["deep_link"]
            )
            return flight_data
            #########################
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                booking_link= data["deep_link"]
            )

            print(f"{flight_data.destination_city}: ₹{flight_data.price}\n{flight_data.out_date} till { flight_data.return_date}")
            return flight_data
        
        
        #####################@@@@@@@@@@@@@@@@@@@
    # def check_flight(self, origin_city, destination_city,from_day, to_day):
    #     headers = {"apikey": TEQUILA_API_KEY}
    #     query = {
    #         "fly_from": origin_city,
    #         "fly_to": destination_city,
    #         "date_from": from_day.strftime("%d/%m/%Y"),
    #         "date_to": to_day.strftime("%d/%m/%Y"),
    #         "nights_in_dst_from": 7,
    #         "nights_in_dst_to": 30,
    #         "flight_type": "round",
    #         "one_for_city": 1,
    #         "max_stopovers": 0,
    #         "curr": "INR"
    #     }
        
    #     response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search",headers=headers,params=query)
    #     # response.raise_for_status()
        
    #     try:
    #         data = response.json()["data"][0]
    #     except IndexError:   
    #         try:
    #             query["max_stopovers"] = 1
    #             data = response.json()["data"][0]
                
    #         except IndexError:
    #             query["max_stopovers"] = 3
    #             response = requests.get(
    #                 url=f"{TEQUILA_ENDPOINT}/v2/search",
    #                 headers=headers,
    #                 params=query,
    #             )
    #             data = response.json()["data"][0]
    #             # pprint(data)
    #             flight_data = FlightData(
    #                 price=data["price"],
    #                 origin_city=data["route"][0]["cityFrom"],
    #                 origin_airport=data["route"][0]["flyFrom"],
    #                 destination_city=data["route"][1]["cityTo"],
    #                 destination_airport=data["route"][1]["flyTo"],
    #                 out_date=data["route"][0]["local_departure"].split("T")[0],
    #                 return_date=data["route"][2]["local_departure"].split("T")[0],
    #                 stop_overs=1,
    #                 via_city=data["route"][0]["cityTo"]
    #             )
    #             return flight_data
            
    #         else:
    #             flight_data = FlightData(
    #                 price=data["price"],
    #                 origin_city=data["route"][0]["cityFrom"],
    #                 origin_airport=data["route"][0]["flyFrom"],
    #                 destination_city=data["route"][0]["cityTo"],
    #                 destination_airport=data["route"][0]["flyTo"],
    #                 out_date=data["route"][0]["local_departure"].split("T")[0],
    #                 return_date=data["route"][1]["local_departure"].split("T")[0]
    #             )
    #             print(f"{flight_data.destination_city}: ₹{flight_data.price}\n{flight_data.out_date} till { flight_data.return_date}")
    #             return flight_data
        
        
            

    
    
    
    
