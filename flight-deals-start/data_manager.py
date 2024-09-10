import os

import requests

api_key = 'https://api.sheety.co/4c87b2db24ecd155681a853f1b9ea33b/flightDeals/prices'
email_api = os.environ["EMAIL_API"]

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = None
        self.iata_logger = {}

    def get_cities(self):
        response = requests.get(url=api_key)
        self.data = response.json()
        cities = [city['city'] for city in self.data['prices'] if city['iataCode'] == '']
        self.iata_logger = {city['city']: str(city['id']) for city in self.data['prices']}
        return cities


    def add_iata(self, iata):
        for key, value in iata.items():
            edit = {
                'price': {
                    'city': key,
                    'iataCode': value
                }
            }
            api_edit = 'https://api.sheety.co/4c87b2db24ecd155681a853f1b9ea33b/flightDeals/prices/[Object ID]'
            api_edit = api_edit.replace('[Object ID]', self.iata_logger[key])
            response = requests.put(url=api_edit, json=edit)
            response.raise_for_status()

    def grab_all_info(self):
        info_list = [[city['city'], city['iataCode'], city['lowestPrice']] for city in self.data['prices']]
        return info_list


    def grab_emails(self):
        response = requests.get(url=email_api)
        return response.json()
