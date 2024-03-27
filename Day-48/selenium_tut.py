from selenium import webdriver
from selenium.webdriver.common.by import By

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
} 
#keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True) 

driver = webdriver.Chrome(options=chrome_options)

driver.get(url = "https://www.python.org/")



search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button.size)

docs = driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a")
print(docs.text)

bug_link_xpath = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link_xpath.text)

events_time = driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
events_name = driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")
events = {}
for n in range(len(events_time)):
    events[n] = {
        "time" : events_time[n].text,
        "name" : events_name[n].text
    }

print(events)


# driver.close() # Close a single tab
driver.quit() # Close the chrome app in its entirety