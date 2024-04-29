import requests
from bs4 import BeautifulSoup
import json


url = "https://www.amazon.in/s?k=sd+card"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
def scrape_sd_card_prices():
    url = "https://www.amazon.in/s?k=sd+card"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

#     products = []
#     for product in soup.find_all('div', class_='s-result-item'):
#         print(product)
#         name = product.find('span', class_='a-size-medium a-color-base a-text-normal').text.strip()
#         price = product.find('span', class_='a-price-whole').text.strip()
#         products.append({'name': name, 'price': price})
        
#     for product in soup.find_all('span', class_='a-size-medium a-color-base a-text-normal'):
#         print(product)
#         # name = product.find('span', class_='a-size-medium a-color-base a-text-normal').text.strip()
#         # price = product.find('span', class_='a-price-whole').text.strip()
#         # products.append({'name': name, 'price': price})

#     return products

# if __name__ == "__main__":
#     sd_card_prices = scrape_sd_card_prices()
#     print(json.dumps(sd_card_prices, indent=4))


for product in soup.find_all('span', class_='a-size-medium a-color-base a-text-normal'):
    print('a' + product)