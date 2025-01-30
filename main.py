import requests
from datetime import datetime



pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH,
    "name": "Days Coding",
    "unit": "commit",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

#response = requests.post(url = graph_endpoint, json= graph_config, headers=headers)
#print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"
today = datetime(year=2025, month=1, day=29)
pixel_config ={
    "date": today.strftime("%Y%m%d"),
    "quantity": "20"
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)
