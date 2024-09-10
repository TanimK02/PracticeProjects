import requests
import datetime
from data_manager import DataManager

Kiwi_Api = 'kMV7N6r5IcIRNNIUYOe1RjyBj9apTSY9'


def cheapest(e):
    return e['price']


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.cities = []
        self.header = {
            'Content-Type': 'application/json',
            'Content-Encoding': 'gzip',
            'apikey': Kiwi_Api
        }
        self.search_endpoint = 'https://api.tequila.kiwi.com/locations/query'

    def search_for_iata(self):
        iata = {}
        for city in self.cities:
            parameters = {
                'term': city,
                'name': city,
                'locale': 'en-US',
                'location_types': "airport",
                'limit': 5
            }

            response = requests.get(url=self.search_endpoint, params=parameters, headers=self.header)
            iata[city] = (response.json()['locations'][0]['city']['code'])
        return iata

    def get_cities(self, cities):
        self.cities = cities

    def search_for_flights(self, cities):
        discount_list = {}
        for city in cities:
            search_flight_endpoint = 'https://api.tequila.kiwi.com/v2/search'
            tmr = (datetime.date.today() + datetime.timedelta(days=1))
            tommorow = tmr.strftime("%d/%m/%Y")
            six_mnths = (datetime.date.today() + datetime.timedelta(days=30 * 6))
            six_months = six_mnths.strftime("%d/%m/%Y")
            parameters = {
                'fly_from': 'LON',
                'fly_to': city[1],
                'date_from': tommorow,
                'date_to': six_months,
                'price_to': city[2],
                'curr': 'GBP',
                'nights_in_dst_from': 7,
                'nights_in_dst_to': 28,
                'stop_overs': 0

            }
            response = requests.get(url=search_flight_endpoint, params=parameters, headers=self.header)
            discount_list[city[0]] = [
                dict(link=i["deep_link"], price=i['price'], flyFrom=i['flyFrom'], flyTo=i['flyTo'],
                     local_departure=i['local_departure'], local_arrival=i['route'][1]['local_arrival'],
                     city_from=i["cityFrom"])
                for i in response.json()['data']]
            discount_list[city[0]].sort(key=cheapest)
            if len(discount_list[city[0]]) >= 1:
                discount_list[city[0]] = discount_list[city[0]][0]
        cities = [city for city in cities if len(discount_list[city[0]]) == 0]
        for city in cities:
            search_flight_endpoint = 'https://api.tequila.kiwi.com/v2/search'
            tmr = (datetime.date.today() + datetime.timedelta(days=1))
            tommorow = tmr.strftime("%d/%m/%Y")
            six_mnths = (datetime.date.today() + datetime.timedelta(days=30 * 6))
            six_months = six_mnths.strftime("%d/%m/%Y")
            parameters = {
                'fly_from': 'LON',
                'fly_to': city[1],
                'date_from': tommorow,
                'date_to': six_months,
                'price_to': city[2],
                'curr': 'GBP',
                'nights_in_dst_from': 7,
                'nights_in_dst_to': 28,
                'stop_overs': 1,
                'limit': 1

            }
            response2 = requests.get(url=search_flight_endpoint, params=parameters, headers=self.header)
            discount_list[city[0]] = [
                dict(link=i["deep_link"], price=i['price'], flyFrom=i['flyFrom'], flyTo=i['flyTo'],
                     local_departure=i['local_departure'], local_arrival=i['route'][1]['local_arrival'],
                     city_from=i["cityFrom"])
                for i in response2.json()['data']]
            discount_list[city[0]].sort(key=cheapest)
            if len(discount_list[city[0]]) >= 1:
                discount_list[city[0]] = discount_list[city[0]][0]
        return discount_list
