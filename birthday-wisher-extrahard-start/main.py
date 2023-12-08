##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import smtplib
import pandas
import random
import os

now = dt.datetime.now()
year = now.year
day = now.day
month = now.month

today = year, month, day
email= "put in email"
password = "put in app password"

birthdays = pandas.read_csv('birthdays.csv')

for (index,row) in birthdays.iterrows():
    if row.year == year and row.day == day and row.month == month:
        rand_letter = random.choice(os.listdir("letter_templates/"))
        with open(f"letter_templates/{rand_letter}",'r') as file:
            letter = file.readlines()
            letter[0] = letter[0].replace("[NAME]", row['name'])
            letter = "".join(letter)
            # put in smtp here default is gmail. errbody uses gmail
        with smtplib.SMTP_SSL('smtp.gmail.com') as connection:
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=row.email, msg=f"Subject:Happy Birthday, {row['name']}\n\n{letter}")

