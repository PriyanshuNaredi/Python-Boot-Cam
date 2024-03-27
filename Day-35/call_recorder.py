# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACaa38a9714a33546e063b885ccc1f9acc"
auth_token = "347ea8ab8687eee23764f7d281303ce5"
client = Client(account_sid, auth_token)

recording = client.calls('CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                  .recordings \
                  .create()

print(recording.sid)
