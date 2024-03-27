import time
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

MY_EMAIL = "linuxrdb007@gmail.com"
MY_PASSWORD = "cuzm rset fwpn ytxe"

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
url = "https://www.amazon.in/dp/B0CRL4R2DN?psc=1&ref_=cm_sw_r_cp_ud_dp_3HVQCBS55RZR64DGVJB6"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8,en-IN;q=0.7"
}
response = requests.get(url, headers= header)

# print(response)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(name="span",class_="a-price-whole")
try:
    price_without_currency = price.get_text()
except AttributeError:
    price_without_currency = price.get_text()
else:
    price_without_currency = price_without_currency.rstrip(".")
    price_without_expressions = ""

    for i in price_without_currency:
        if i != ",":
            price_without_expressions += i

    price_as_float = float(price_without_expressions)
    print(price_as_float)


title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 11000

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
                                )