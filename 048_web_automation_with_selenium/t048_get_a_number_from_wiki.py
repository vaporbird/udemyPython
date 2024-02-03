from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

number = driver.find_element(By.ID, "articlecount").find_element(By.CSS_SELECTOR, "[title='Special:Statistics']")
print(number.text)
