from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#  from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
#  from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc
import os
import time

INSTA_ACC = "https://www.instagram.com/pyrrha._.nikos/"
#  INSTA_ACC = "https://www.instagram.com/pacificabanda"

options = webdriver.ChromeOptions()
driver = uc.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.delete_all_cookies()
driver.get("https://www.instagram.com/")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input").send_keys(os.environ.get("STANDARD_EMAIL"))
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input").send_keys(os.environ.get("STANDARD_PASS"))
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]").click()
time.sleep(4)
#  Dismiss popups
try:
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div").click()
    time.sleep(2)
except NoSuchElementException:
    print("no save login popup")

try:
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
    time.sleep(2)
except NoSuchElementException:
    print("no notifications pop up")

driver.get(INSTA_ACC)
time.sleep(2)
follower_label = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a").text
follower_count = int(follower_label.split(" ")[0].replace("K", "999"))
print(follower_label, follower_count)
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a").click()
time.sleep(3)

#  Some spaghetti code here, it's needed bacause for big accounts instagram hides some followers and changes the structure
try:
    follower_popup = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
    acc_prompt = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/"
except NoSuchElementException:
    follower_popup = driver.find_element(By.CSS_SELECTOR, "._aano")
    acc_prompt = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/"

flag = False
for i in range(1, follower_count):
    try:
        acc = driver.find_element(By.XPATH, acc_prompt + f"div[{i}]/div/div/div/div[3]/div/button")
        #  Uncomment the line below to follow accounts
        #  acc.click()
        delta_y = acc.rect['y']
        scroll_origin = ScrollOrigin.from_element(follower_popup)
        ActionChains(driver).scroll_from_origin(scroll_origin, 0, delta_y).perform()
        time.sleep(0.1)
        flag = False

    except NoSuchElementException:
        if flag:
            print("cannot find another element")
            break
        time.sleep(3)
        flag = True
