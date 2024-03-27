import smtplib
import requests
from twilio.rest import Client

STOCK = "HDFC BANK"
COMPANY_NAME = "HDFC BANK"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = ""

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = ""

TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""

MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
PORT = 587
MY_EMAIL = "@gmail.com"
MY_PASSWORD = ""

# Stock:
# stock_prams = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": "IBM",
#     "apikey": "demo"
# }

stock_prams = {
    "function":"TIME_SERIES_DAILY",
    "symbol" : "HDFCBANK.BSE",
    "apikey" : STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_prams)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]


daybefore_yesterday_data = data_list[1]
daybefore_yesterday_closing_price = daybefore_yesterday_data["4. close"]


difference = float(yesterday_closing_price) - float(daybefore_yesterday_closing_price)

up_down = None
if difference > 0:
    up_down = "📈"
else:
    up_down = "📉"

diff_percent = round(difference/float(yesterday_closing_price) * 100)

if abs(diff_percent) > 0.2:
    news_parms = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME

    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parms)
    article = news_response.json()["articles"]

    three_articles = article[:3]

    formatted_articles_list = [f"{STOCK}:{up_down}{diff_percent}% \nHeadlines:{article['title']}. \nBrief: {
        article['description']}" for article in three_articles]

    print(formatted_articles_list)
    
    with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS,port=PORT) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            # for article in formatted_articles_list:
            connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs="timapple3343@gmail.com",
                    msg=f"Subject:{STOCK}:{up_down}{diff_percent}% \n\n".encode('utf-8')
                )

    # client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    # for article in formatted_articles_list:
    #     message = client.messages.create(
    #         body=article,
    #         from_='+12404340466',
    #         to='+919340587377')
