from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from threading import Thread
import time

TOTAL_RUN_TIME = 600
BUY_INTERVAL = 20


def thread1(threadname):
    while True:
        cookie.click()


def thread2(threadname, driver, sleep_timer):
    while True:
        buy_items(driver)
        time.sleep(sleep_timer)


def get_money(driver):
    return int(driver.find_element(By.ID, "money").text.replace(",", ""))


def buy_items(driver):
    money = get_money(driver)
    items = [
            "buyCursor",
            "buyGrandma",
            "buyFactory",
            "buyMine",
            "buyShipment",
            "buyAlchemy\ lab",
            "buyPortal",
            "buyTime\ machine",
             ]

    for item in reversed(items):
        while True:
            curr_item = driver.find_element(By.CSS_SELECTOR, f"#{item} b")
            cost = int(curr_item.text.split(" ")[-1].replace(",", ""))

            if cost > money:
                break

            curr_item.click()
            money = get_money(driver)


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
items_list = []

thread1 = Thread(target=thread1, args=("Thread-1", ))
thread2 = Thread(target=thread2, args=("Thread-2", driver, BUY_INTERVAL, ))
thread1.start()
thread2.start()

time.sleep(TOTAL_RUN_TIME)

should_stop = True
thread1.join()
thread2.join()
