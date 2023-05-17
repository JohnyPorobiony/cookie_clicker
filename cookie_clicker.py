from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

start = time.time()
end = start + 5*60
check_in_secs = 4
checks_done = 0

def get_list_of_affordable_items():
    "Return the list of all affordable items"
    list = []
    store = driver.find_elements(By.CSS_SELECTOR, "#store b")
    for item in store:
        # If elements parents class is not 'grayed' add the element to the list
        if item.find_element(By.XPATH, "..").get_attribute('class') != "grayed":
            list.append(item)
    return list

def buy_item(list):
    "Buy the most expensive affordable item in the store"
    if len(list) > 0:
        list[-1].click()

while time.time() < end:
    cookie.click()
    if time.time() >= start + (check_in_secs * checks_done):
        available_items = get_list_of_affordable_items()
        buy_item(available_items)
        checks_done += 1
