import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.__email__ = 'day32nim@gmail.com'
        self.__pass__ = 'ylik nkfr dwhm anmx'

    def send_mail(self,msg,emails):
        email_list = [email['email'] for email in emails['sheet1']]
        for email in email_list:
            for message in msg:
                with smtplib.SMTP_SSL('smtp.gmail.com') as connection:
                    connection.login(user=self.__email__, password=self.__pass__)
                    connection.sendmail(from_addr=self.__email__, to_addrs='kingtanim2@gmail.com',
                                        msg=message.as_string())
