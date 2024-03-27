import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element(by=By.ID, value="cookie")

# Get upgrade item ids.
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

two_min = time.time() + 60 * 1
five_min = time.time() + 60 * 5

while True:
    start_time_inner = time.time()
    duration_inner = 3
    weights = (10,10, 20, 90, 80, 70, 20, 10)

    while time.time() - start_time_inner < duration_inner:
        cookie.click()

    if time.time() < two_min:
        weights = (0, 0, 0, 0, 0, 0, 100, 99)

    buy_list = ["buyTime machine", "buyPortal", "buyAlchemy lab", "buyShipment", "buyMine", "buyFactory", "buyGrandma",
                "buyCursor"]

    try:
        random_buy = random.choices(buy_list, weights=weights, k=1)
        print(random_buy[0])
        upgrade = driver.find_element(By.ID, value=random_buy[0])
        upgrade.click()
    except StaleElementReferenceException:
        continue
    # else:
    # continue
    # if time.time() > five_min:
    #     cookie_per_s = driver.find_element(by=By.ID, value="cps").text
    #     print(cookie_per_s)
    #     break
