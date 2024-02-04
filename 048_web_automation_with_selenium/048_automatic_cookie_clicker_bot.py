from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from threading import Thread
import time

TOTAL_RUN_TIME = 300
BUY_INTERVAL = 5
thread_run = True


def thread1(threadname):
    global thread_run
    while thread_run:
        cookie.click()


def thread3(threadname):
    global thread_run
    while thread_run:
        cookie.click()


def thread4(threadname):
    global thread_run
    while thread_run:
        cookie.click()


def thread5(threadname):
    global thread_run
    while thread_run:
        cookie.click()


def thread6(threadname):
    global thread_run
    while thread_run:
        cookie.click()


def thread2(threadname, driver, sleep_timer):
    global thread_run
    while thread_run:
        time.sleep(sleep_timer)
        buy_items(driver)


def get_money(driver):
    return int(driver.find_element(By.ID, "money").text.replace(",", ""))


def buy_items(driver):
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
    money = get_money(driver)
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
thread3 = Thread(target=thread3, args=("Thread-3", ))
thread4 = Thread(target=thread4, args=("Thread-4", ))
thread5 = Thread(target=thread5, args=("Thread-5", ))
thread6 = Thread(target=thread6, args=("Thread-5", ))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()

time.sleep(TOTAL_RUN_TIME)
thread_run = False
thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()
exit(1)
