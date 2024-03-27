
import requests
import csv

def get_all_airports():
    url = "https://api.tequila.kiwi.com/locations/query"

    headers = {
        "apikey": "rlrl7n4xnoKEl56C9g-eJ-IACRe54jbK"
    }

    params = {
        "term": "",
        "location_types": "airport",
        "limit": 10000  # Set a high limit to ensure retrieval of all airports
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        airports = {}

        # Extract airport information
        for location in data["locations"]:
            airport_iata = location["code"]
            airport_name = location["name"]
            airport_city = location["city"]["name"]
            airport_country = location["country"]["name"]

            airports[airport_iata] = {
                'name': airport_name,
                'city': airport_city,
                'country': airport_country
            }

        return airports
    else:
        print("Error fetching airport data:", response.text)
        return None

def export_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["IATA Code", "Name", "City", "Country"])
        for iata, info in data.items():
            writer.writerow([iata, info['name'], info['city'], info['country']])

if __name__ == "__main__":
    airports = get_all_airports()
    if airports:
        export_to_csv(airports, "airports.csv")
        print("Airports data exported to airports.csv successfully!")
    else:
        print("Failed to fetch airports data.")


# import requests
# import csv

# def get_airports():
#     url = "http://api.aviationstack.com/v1/airports"

#     params = {
#         "access_key": "YOUR_ACCESS_KEY_HERE",
#         "limit": 10000  # Set a high limit to ensure retrieval of all airports
#     }

#     response = requests.get(url, params=params)

#     if response.status_code == 200:
#         data = response.json()
#         airports = {}

#         # Extract city information for each airport
#         for airport in data["data"]:
#             airport_iata = airport["iata_code"]
#             airport_city = airport["city"]

#             if airport_iata:
#                 airports[airport_iata] = {'city': airport_city}

#         return airports
#     else:
#         print("Error fetching airport data:", response.text)
#         return None

# def export_to_csv(data, filename):
#     with open(filename, 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(["IATA Code", "City"])
#         for iata, info in data.items():
#             writer.writerow([iata, info['city']])

# if __name__ == "__main__":
#     airports = get_airports()
#     if airports:
#         export_to_csv(airports, "airports.csv")
#         print("Airports data exported to airports.csv successfully!")
#     else:
#         print("Failed to fetch airports data.")



# import requests
# import csv

# def get_airports():
#     url = "https://tequila-api.kiwi.com/locations/query"

#     headers = {
#         "apikey": "rlrl7n4xnoKEl56C9g-eJ-IACRe54jbK"
#     }

#     params = {
#         "term": "",
#         "location_types": "airport",
#         "limit": 1000  # Increase the limit to ensure retrieval of all airports
#     }

#     response = requests.get(url, headers=headers, params=params)

#     if response.status_code == 200:
#         data = response.json()
#         airports = {}

#         # Extract city information for each airport
#         for location in data["locations"]:
#             airport_iata = location["code"]
#             airport_city = location["city"]["name"]

#             if airport_iata:
#                 airports[airport_iata] = {'city': airport_city}

#         return airports
#     else:
#         print("Error fetching airport data:", response.text)
#         return None

# def export_to_csv(data, filename):
#     with open(filename, 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(["IATA Code", "City"])
#         for iata, info in data.items():
#             writer.writerow([iata, info['city']])

# if __name__ == "__main__":
#     airports = get_airports()
#     if airports:
#         export_to_csv(airports, "airports.csv")
#         print("Airports data exported to airports.csv successfully!")
#     else:
#         print("Failed to fetch airports data.")
        
        
        

# # import requests

# # def get_lowest_fare_from_DEL():
# #     url = "https://tequila-api.kiwi.com/locations/query"

# #     headers = {
# #         "apikey": "rlrl7n4xnoKEl56C9g-eJ-IACRe54jbK"
# #     }

# #     params = {
# #         "term": "DEL",
# #         "location_types": "airport",
# #         "limit": 100
# #     }

# #     response = requests.get(url, headers=headers, params=params)
# #     data = response.json()

# #     if response.status_code == 200:
# #         airports = data["locations"]
# #         del_airport = airports[0]
# #         del_id = del_airport["id"]

# #         url = f"https://tequila-api.kiwi.com/v2/search"
# #         params = {
# #             "fly_from": del_id,
# #             "limit": 100
# #         }

# #         response = requests.get(url, headers=headers, params=params)
# #         data = response.json()

# #         if response.status_code == 200:
# #             flights = data["data"]
# #             lowest_fares = {}

# #             for flight in flights:
# #                 dest_airport = flight["cityTo"]
# #                 fare = flight["price"]

# #                 if dest_airport not in lowest_fares:
# #                     lowest_fares[dest_airport] = fare
# #                 else:
# #                     if fare < lowest_fares[dest_airport]:
# #                         lowest_fares[dest_airport] = fare

# #             return lowest_fares
# #         else:
# #             print("Error fetching flight data:", data.get("error"))
# #     else:
# #         print("Error fetching airport data:", data.get("error"))

# # if __name__ == "__main__":
# #     lowest_fares = get_lowest_fare_from_DEL()
# #     if lowest_fares:
# #         print("Lowest fares from DEL airport:")
# #         for airport, fare in lowest_fares.items():
# #             print(f"IATA Code: {airport}, Lowest Fare: {fare}")
# #     else:
# #         print("No data available.")
