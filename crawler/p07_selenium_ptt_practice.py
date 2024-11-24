from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import requests

service = Service("./chromedriver.exe")
driver = Chrome(service=service)

driver.get("https://www.ptt.cc/bbs/index.html")

# Xpath
# //*[@id="main-container"]/div[2]/a
# /html/body/div[2]/div[2]/a
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/a").click()
driver.find_element(By.XPATH, "/html/body/div[2]/form/div[1]/button").click()

print(driver.get_cookies())
# Each cookie_dict be like: {'domain': 'www.ptt.cc', 'httpOnly': False, 'name': 'over18', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'}

cookies = {cookie_dict["name"]: cookie_dict["value"]
           for cookie_dict in driver.get_cookies()}

# 把抓到的cookies丟到request裡面 確認能爬到ptt的文
res = requests.get(
    "https://www.ptt.cc/bbs/Gossiping/index.html",
    cookies=cookies,
)

print(res.text)

time.sleep(10)
