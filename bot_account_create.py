from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from fake_useragent import UserAgent
import undetected_chromedriver as uc
import get_email
import multi_proxies
from faker import Faker
import time
import random






user_agent = UserAgent().random

#proxies = multi_proxies.fetch_proxies()
#selected_proxy = random.choice(proxies)
#print(f"Proxy scelto: {selected_proxy}")

chrome_options = Options()
#chrome_options.add_argument(f'--proxy-server={selected_proxy}')
chrome_options.add_argument("--disable-search-engine-choice-screen")  
chrome_options.add_argument(f'user-agent={user_agent}')  


driver = uc.Chrome(options=chrome_options)
driver.delete_all_cookies()
driver.execute_cdp_cmd('Network.clearBrowserCache', {})

fake = Faker("it_IT")


url = "https://www.instagram.com/accounts/emailsignup/"


driver.get(url)


time.sleep(3)


try:
    pulsante_cookie = WebDriverWait(
        driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Consenti tutti i cookie')]"))
    )

    pulsante_cookie.click()
    print("Pulsante cookie cliccato :)")

except Exception as e:
    print("Impossibile cliccare il pulsante dei cookie :(", e)


time.sleep(random.randint(0, 3))


try:
    generated_email = get_email.generate_email()
    
    email_field = WebDriverWait(
        driver, 5).until(
            EC.element_to_be_clickable(
                (By.NAME, "emailOrPhone"))
    )
    
    email_field.send_keys(generated_email)
    print("Email inserita:", generated_email)
    
except Exception as e:
    print(f"Operazione email non riuscita: {e}")


time.sleep(random.randint(0, 3))


try:
    generated_password = fake.password()
    
    password_field = WebDriverWait(
        driver, 5).until(
            EC.element_to_be_clickable(
                (By.NAME, "password"))
    )

    password_field.send_keys(generated_password)
    print(f"Password inserita: {generated_password}")

except Exception as e:
    print(f"Operazione password non riuscita: {e}")


time.sleep(random.randint(0, 3))


try:
    generated_name = f"{fake.first_name()} {fake.last_name()}"

    name_field = WebDriverWait(
        driver, 5).until(
            EC.element_to_be_clickable(
                (By.NAME, "fullName"))
    )

    name_field.send_keys(generated_name)
    print(f"Nome inserito: {generated_name}")

except Exception as e:
    print(f"Operazione nome non riuscita: {e}")


time.sleep(random.randint(0, 3))


try:
    username_field = WebDriverWait(
        driver, 5).until(
            EC.element_to_be_clickable(
                (By.NAME, "username"))
    )

    generated_username = fake.user_name()

    username_field.clear()
    username_field.send_keys(generated_username)

    print(f"Username inserito: {generated_username}")



except Exception as e:
    print(f"Operazione username non riuscita: {e}")

time.sleep(5)

suggerimento = WebDriverWait(
    driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, f"//*[@tabindex='{0}']"))
    )

if suggerimento:
    suggerimento.click()

    time.sleep(random.randint(1.5, 3.5))


    try:
        credential_button = WebDriverWait(
            driver, 5).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(text(), 'Avanti')]"))
        )

        credential_button.click()
        print(f"Pulsante avanti cliccato")

    except Exception as e:
        print(f"Operazione cliccare pulsante avanti non riuscita: {e}")
        time.sleep(1000)
else:
    try:
        credential_button = WebDriverWait(
            driver, 5).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(text(), 'Avanti')]"))
        )

        time.sleep(random.randint(1.5, 3.5))


        credential_button.click()
        print(f"Pulsante avanti cliccato")

    except Exception as e:
        print(f"Operazione cliccare pulsante avanti non riuscita: {e}")
        time.sleep(1000)




time.sleep(1000)
