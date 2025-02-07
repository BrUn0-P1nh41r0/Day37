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
today = datetime.now()
today_format = today.strftime("%Y%m%d")
pixel_config ={
    "date": today,
    "quantity": input("How many days of the challenge did you completed today? ")
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

pixel_alter_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today_format}"
pixel_alter_config = {
    "quantity": "7"
}
#response = requests.put(url = pixel_alter_endpoint, json=pixel_alter_config, headers=headers)
#print(response.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today_format}"
#response = requests.delete(url= pixel_delete_endpoint, headers=headers)
#print(response.text)
