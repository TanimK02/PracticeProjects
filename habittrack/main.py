import requests
from datetime import datetime


TOKEN = 'insert token here'
USERNAME = 'insert usernmae'
pixela_endpoint = 'https://pixe.la/v1/users'
graphid = 'add in graph id of your choice'
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

graph_config = {
    'id': graphid,
    'name': 'insert graph name',
    'unit': 'insert what you want to measure',
    'type': "put int/float here depending on what you're going to measure",
    'color': 'sora(color is in japanaese)'

}

headers = {
    'X-USER-TOKEN': TOKEN
}

today = datetime(year=, month=, day=)

pixel_add = {
    'date': today.strftime("%Y%m%d"),
    'quantity': 'insert quanitity',

}
pixel_update = {
    'quantity':input('can ask question of how much here too?')
}
print(today.strftime("%Y%m%d"))

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graphid}/{today.strftime("%Y%m%d")}"
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# response = requests.post(url= pixela_endpoint, json=user_params)
response = requests.put(url=graph_endpoint, json=pixel_update, headers=headers)
print(response.text)

