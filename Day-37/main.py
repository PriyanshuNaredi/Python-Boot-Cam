import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = ""
TOKEN = ""

GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
# # response.raise_for_status()

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding",
    "unit": "hr",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(graph_response.text)

today = datetime.now()
yesterday = datetime(year=2024, month=2, day=8)

# post_config = {
#     "date": yesterday.strftime("%Y%m%d"),
#     "quantity": "2"
# }

post_config = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How many hours did you study ")
}

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
post_response = requests.post(url=post_endpoint,json=post_config,headers=headers)
print(post_response.text)

update_endpoint = f"{
    pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"
    
new_pixel = {
    "quantity": "1"
}

# update_response = requests.put(
#     url=update_endpoint, json=new_pixel, headers=headers)
# print(update_response.text)


# delete_endpoint = f"{
#     pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"
    
# delete_response = requests.delete(url=delete_endpoint,headers=headers)    
# print(delete_response.text)