from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')
money_path = driver.find_element(By.XPATH, '//*[@id="money"]')
items = ["buyPortal","buyAlchemy lab","buyShipment","buyMine","buyFactory","buyGrandma"]
start_time_outer = time.time()
duration_outer = 300

while time.time() - start_time_outer < duration_outer:
    start_time_inner = time.time()
    duration_inner = 5

    while time.time() - start_time_inner < duration_inner:
        cookie.click()

    money = int(money_path.text.replace(",", ""))
    for item in items:
        try:
            value = driver.find_element(By.XPATH, f'//*[@id="{item}"]/b')
            price = int(value.text.split()[-1].replace(",", ""))
            if money >= price:
                b = int(money/price)
                for i in range(b):
                    try:
                        value.click()
                    except StaleElementReferenceException:

                        value = driver.find_element(By.XPATH, f'//*[@id="{item}"]/b')
                        value.click()
        except StaleElementReferenceException:
            break