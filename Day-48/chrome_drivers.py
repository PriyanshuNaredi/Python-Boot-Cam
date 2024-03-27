from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# import from webdriver_manager (using underscore)
from webdriver_manager.chrome import ChromeDriverManager 
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True) 