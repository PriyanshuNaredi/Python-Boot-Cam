# list nested in a dictionary
travel_log = {
    "India": ["Indore", "Delhi"]
}

# dictionary nested in a dictionary

travel_log = {
    "India": {"cities_visited": ["Indore", "Delhi"],
              "total_visits": 12
              },
    "Bharat": {"cities_visited": ["Ayodiya", "Delhi"],
              "total_visits": 12
              }
}

# dictionary nested in a list

travel_log = [
    {"country": "India",
     "cities_visited": ["Indore", "Delhi"],
     "total_visits": 12
     },
    {"country": "Bharat",
     "cities_visited": ["Ayodiya","Indore", "Delhi"],
     "total_visits": 12
     }
]
print(travel_log[1])
print(travel_log[1]["cities_visited"])
print(travel_log[1]["total_visits"])
print(travel_log[1]["cities_visited"][0])