from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class FlightData:
    # This class is responsible for structuring the flight data.

    def __init__(self):
        self.data = {}


    def get_data(self, data: dict):
        self.data = data

    def turn_into_msg(self):
        gbp_symbol = '£'
        msg_list = []
        for city, value in self.data.items():
            if len(value) >= 1:
                msg = MIMEMultipart()
                body = (f"Low price alert! Only {gbp_symbol}{value['price']} to fly"
                        f" from {value['city_from']}-{value['flyFrom']} "
                        f"to {city}-{value['flyTo']}, from {value['local_departure'][:10]} "
                        f"to {value['local_arrival'][:10]}.\n"
                        f"Go get your ticket now: {value['link']}")
                msg['Subject'] = f"Low Price For Trip To {city}"
                msg.attach(MIMEText(body, 'plain', 'utf-8'))
                msg_list.append(msg)
        return msg_list

