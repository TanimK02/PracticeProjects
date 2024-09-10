from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

# make instances of classes
data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification_manager = NotificationManager()

# get program running
# get cities from sheets

cities = data_manager.get_cities()

# add cities to flight search list

flight_search.get_cities(cities)

# search for iatas of cities

iata = flight_search.search_for_iata()

# add iatas of cities onto sheets
data_manager.add_iata(iata)

# grabs the info from the sheets
flight_list = data_manager.grab_all_info()

# takes the sheet info and does the search for the flight and puts results
# into dictionary with the necessary info of the flight
discount_dict = flight_search.search_for_flights(flight_list)

# puts discount dict into flight data, so it can set up the data in a way where it could be more readable in user email
flight_data.get_data(discount_dict)


msg_list = flight_data.turn_into_msg()

email_list = data_manager.grab_emails()

notification_manager.send_mail(msg_list,email_list)



