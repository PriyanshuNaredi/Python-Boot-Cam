import requests
from bs4 import BeautifulSoup

# URL = 'http://www.league321.com/austria-footbalsadasl.html'

URL = 'https://en.wikipedia.org/wiki/2._Liga_(Austria)'

response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
a = soup.find_all('a')
# print(a[0].get_text())
for link in a:
    
    try:
        link_check = requests.get(link.get("href"))
    except Exception as e:
        print(str(e))
    else:
        print("Link:", link.get("href"))
        print(response.status_code)

# print("Link:", link.get("href"), "Text:", link.string)