from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc
import os
import time

options = webdriver.ChromeOptions()
driver = uc.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.delete_all_cookies()
driver.get("https://tinder.com/")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='c1606223767']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='c-1684014328']/div").click()
time.sleep(1)

base_window = driver.window_handles[0]
login_window = driver.window_handles[1]
driver.switch_to.window(login_window)

driver.find_element(By.XPATH, "//*[@id='identifierId']").send_keys(os.environ.get("STANDARD_EMAIL"))
driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button").click()
time.sleep(2)

driver.find_element(By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input").send_keys(os.environ.get("STANDARD_PASS"))
driver.find_element(By.XPATH, "//*[@id='passwordNext']/div/button").click()
time.sleep(50)

driver.switch_to.window(base_window)
driver.find_element(By.XPATH,"//*[@id='c1827564203']/main/div[1]/div/div/div[3]/button[1]").click()
time.sleep(5)

driver.find_element(By.XPATH, "//*[@id='c1827564203']/main/div[1]/div/div/div[3]/button[2]").click()
time.sleep(1)
for i in range(3, 8):
    try:
        print(i)
        time.sleep(5)
        driver.find_element(By.XPATH, f"//*[@id='c1606223767']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[{i}]/div/div[4]/button").click()
    except webdriver.common.exceptions.lementClickInterceptedException:
        driver.find_element(By.XPATH, "//*[@id='c1062691574']/main/div[1]/div[1]/div/div[4]/button").click()
        time.sleep(1)
    finally:
        driver.find_element(By.XPATH, f"//*[@id='c1606223767']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[{i}]/div/div[4]/button").click()
        

