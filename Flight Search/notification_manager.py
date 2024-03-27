import smtplib
from twilio.rest import Client

TWILIO_SID = "ACaa38a9714a33546e063b885ccc1f9acc"
TWILIO_AUTH_TOKEN = "347ea8ab8687eee23764f7d281303ce5"
TWILIO_VIRTUAL_NUMBER = "+12404340466"
TWILIO_VERIFIED_NUMBER = "+919340587377"

MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
PORT = 587
MY_EMAIL = "linuxrdb007@gmail.com"
MY_PASSWORD = "cuzm rset fwpn ytxe"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS,port=PORT) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )