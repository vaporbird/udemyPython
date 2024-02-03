from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.python.org/")
donate = driver.find_elements(By.CSS_SELECTOR, ".donate-button")
print(donate[0].text)

events_dict = {}
for i in range(1, 6):
    d = driver.find_element(By.XPATH, f"/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[{i}]/time").text
    #  use innerText here for some reason (something with the visible and invisible elements and how .text, innerText, innerHTML and textContent work)
    y = driver.find_element(By.XPATH, f"/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[{i}]/time/span").get_attribute("innerText")
    t = driver.find_element(By.XPATH, f"/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[{i}]/a").text
    events_dict[t] = y + d


print(events_dict)
driver.quit()
