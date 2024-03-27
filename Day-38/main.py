from datetime import datetime
import requests
from websockets import basic_auth_protocol_factory


APP_ID = "94388bd5"
API_KEY = "04fbc0383adeb8b04b8b8ee89fd3d994"

SHEETY_API = "https://api.sheety.co/username/projectName/sheetName"
sheet_endpoint= "https://api.sheety.co/1976f4a69865ccc81fec7e1a97c8843d/myWorkouts/workouts"

SHEETY_USERNAME: "Priyanshu"
SHEETY_PASSWORD: "SBICA20240121000859969154"
SHEETY_TOKEN: "basic_auth_protocol_factory UHJpeWFuc2h1OlNCSUNBMjAyNDAxMjEwMDA4NTk5NjkxNTQ="


GENDER = "male"
WEIGHT_KG = "95"
HEIGHT_CM = "155"
AGE = "24"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

#
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    
    bearer_headers = {
        "Authorization": "Basic UHJpeWFuc2h1OlNCSUNBMjAyNDAxMjEwMDA4NTk5NjkxNTQ="
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )    

    print(sheet_response.text)
    
    

