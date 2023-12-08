import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 0   # type in your latitude
MY_LONG = 0  # type in your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.


def position():
    if abs(iss_latitude - MY_LAT) < 5 and abs(iss_longitude - MY_LONG) < 5:
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
current_hour = time_now.hour

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
user = 'type in email'
password = 'type in app password'


def confirm_time():
    if sunset < current_hour > sunrise:
        return True
    else:
        return False


dark = confirm_time()

while dark:
    pos_confirmation = position()
    print(pos_confirmation)
    if pos_confirmation is True:
        with smtplib.SMTP_SSL('smtp.gmail.com') as connection:
            connection.login(user=user, password=password)
            connection.sendmail(from_addr=user,
                                to_addrs='email u want to send to',
                                msg="Subject:ISS is Above You\n\n Look Up!")
    dark = confirm_time()
    print(dark)
    time.sleep(60)


