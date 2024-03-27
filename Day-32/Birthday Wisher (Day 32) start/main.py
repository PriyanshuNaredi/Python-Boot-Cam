import random
import smtplib
import datetime as dt

MY_EMAIL = "linuxrdb007@gmail.com"
MY_PASSWORD = "cuzm rset fwpn ytxe"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    with open("Day-32\Birthday Wisher (Day 32) start\quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg=f"Subject:Sunday Motivation\n\n {quote}")
