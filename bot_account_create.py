from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from fake_useragent import UserAgent
import undetected_chromedriver as uc
import get_email
import random
import time
import requests



user_agent = UserAgent().random

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
chrome_options.add_argument(f'user-agent={user_agent}')

driver = uc.Chrome(options=chrome_options)

driver.delete_all_cookies()
driver.execute_cdp_cmd('Network.clearBrowserCache', {})

url = "https://www.instagram.com/accounts/emailsignup/"

driver.get(url)

time.sleep(3)

pulsante_cookie = WebDriverWait(
    driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Consenti tutti i cookie')]"))
)

try:
    pulsante_cookie.click()
    print("Pulsante cookie cliicato :)")
except:
    print("Impossibile cliccare il pulsante dei cookie :(")

time.sleep(5)