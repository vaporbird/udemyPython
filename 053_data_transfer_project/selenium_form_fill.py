from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#  from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#  from selenium.common.exceptions import NoSuchElementException
#  from selenium.common.exceptions import ElementClickInterceptedException
#  from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
#  from selenium.webdriver.common.action_chains import ActionChains
#  import undetected_chromedriver as uc
#  import os
import time
from bs_get_data import Scraper


class AutoFill():
    def __init__(self):

        self.offers = Scraper().get_data()

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install())) 
        self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLScixOYkVyyrNaSYCcmoo0r4kZnTHY0WlgkQTPxo4Oh3Fx2naA/viewform") 
        self.driver.delete_all_cookies()

    def FillForm(self):
        for o in self.offers:
            address = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
            price = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
            link = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
            send_btn = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span")

            address.send_keys(o["address"])
            price.send_keys(o["price"])
            link.send_keys(o["link"])
            time.sleep(2)
            send_btn.click()
            self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLScixOYkVyyrNaSYCcmoo0r4kZnTHY0WlgkQTPxo4Oh3Fx2naA/viewform") 
            time.sleep(2)


#  test = AutoFill()
#  test.FillForm()
