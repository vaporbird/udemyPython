from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.action_chains import ActionChains
import os
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
driver.maximize_window()

sign_in = driver.find_element(By.CSS_SELECTOR, ".btn-secondary-emphasis")
sign_in.click()

username = driver.find_element(By.ID, "username")
username.send_keys(os.environ.get("STANDARD_EMAIL"))
password = driver.find_element(By.ID, "password")
password.send_keys(os.environ.get("STANDARD_PASS"))
sign_in = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button")
sign_in.click()

time.sleep(40)  # because of capcha
jobs = []
scroller = driver.find_element(By.CSS_SELECTOR, ".jobs-search-results-list")

for i in range(1, 26):  # can also not hardcode this but I've spent too much time on this project by now
    job = driver.find_element(By.XPATH, f"/html/body/div[6]/div[3]/div[4]/div/div/main/div[2]/div[1]/div/ul/li[{i}]/div/div[1]")
    print(job.text)
    job.click()
    time.sleep(5)

    apply_btn = driver.find_element(By.XPATH, "html/body/div[6]/div[3]/div[4]/div/div/main/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/div/div/button")
    print(apply_btn.text)
    apply_btn.click()
    time.sleep(5)

    # will just close it, no point of registering, and also there are no easy applies with just one click currently
    close_btn = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/button")
    print(close_btn.text)
    close_btn.click()
    time.sleep(5)

    discard_btn = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[3]/button[1]")
    discard_btn.click()
    time.sleep(5)

    try:
        delta_y = int(job.rect['y'])
    except TypeError:
        delta_y = 135
    jobs.append(job)
    scroll_origin = ScrollOrigin.from_element(scroller)
    ActionChains(driver).scroll_from_origin(scroll_origin, 0, delta_y).perform()
#  driver.quit()
