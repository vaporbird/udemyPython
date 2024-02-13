from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#  from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
#  from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
#  from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc
import os
import time

PROMISED_DOWN = 1000.0
PROMISED_UP = 200.0


class InternetSpeedTwitterBot():
    def __init__(self):
        options = webdriver.ChromeOptions()
        self.driver = uc.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        self.driver.delete_all_cookies()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a").click()
        time.sleep(50)
        self.up = float(self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text)
        self.down = float(self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text)

        print("up ", self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text)
        print("down ", self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text)

    def tweet_at_provider(self):
        if (self.up >= PROMISED_UP and self.down >= PROMISED_DOWN):
            return

        message = f"JUST GOT SCAMED @SOMERANDOMTAG !!!\nI am paying for {PROMISED_UP} upload and {PROMISED_DOWN} download, but getting {self.up} upload and {self.down} download\nask me how I feel :((("

        self.driver.get("https://twitter.com/")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input").send_keys(os.environ.get("STANDARD_EMAIL"))
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]").click()
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label").send_keys("@vaporbirdo99878")
            self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div").click()
        except Exception:
            pass
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label").send_keys(os.environ.get("STANDARD_PASS"))
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div/span/br").send_keys(message)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]").click()


itb = InternetSpeedTwitterBot()
itb.get_internet_speed()
itb.tweet_at_provider()
