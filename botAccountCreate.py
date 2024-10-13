from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import fakeMail
import accountInfoGenerator
from fake_useragent import UserAgent
import time
from selenium_recaptcha_solver import RecaptchaSolver
import undetected_chromedriver as uc
from getVerifCode import getInstVeriCode
import random


user_agent = UserAgent().random

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
chrome_options.add_argument(f'user-agent={user_agent}')

driver = uc.Chrome(options=chrome_options)

driver.delete_all_cookies()
driver.execute_cdp_cmd('Network.clearBrowserCache', {})

url = "https://www.instagram.com/accounts/emailsignup/"

driver.get(url)

solver = RecaptchaSolver(driver=driver)

time.sleep(5)

try:
    pulsante_cookie = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button._a9--._ap36._a9_0")))
    pulsante_cookie.click()
    time.sleep(1)
    pulsante_cookie.click()
    time.sleep(1)
    pulsante_cookie.click()
    time.sleep(1)
    pulsante_cookie.click()

except TimeoutException:
    print("Non è stato possibile trovare o cliccare il pulsante dei cookie.")

time.sleep(5)

try:
    email_generata = fakeMail.generatore_email_fake()
    nome_cognome_generati = accountInfoGenerator.generatore_nome_cognome()
    username_generato = accountInfoGenerator.generatore_username()
    password_generata = accountInfoGenerator.generatore_password()


    campoemail = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, "emailOrPhone")))
    compilazione_campo_email = campoemail.send_keys(email_generata)
    print(email_generata)

    time.sleep(1)

    campo_nome_cognome = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, "fullName")))
    compilazione_campo_nome_cognome = campo_nome_cognome.send_keys(nome_cognome_generati)
    print(nome_cognome_generati)

    time.sleep(1)

    campo_username =  WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, "username")))
    compilazione_campo_username = campo_username.send_keys(username_generato)
    print(username_generato)

    time.sleep(1)

    campo_password = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, "password")))
    compilazione_campo_password = campo_password.send_keys(password_generata)

    time.sleep(1)

    while True:
        try:
            elemento = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[6]/div/div/span")))
            print(f"username non disponibile")
            nuovo_username = accountInfoGenerator.generatore_username()
            time.sleep(3)
            compilazione_campo_username = campo_username.send_keys(nuovo_username)
        except:
            print("username disponibile")
            break
    
    time.sleep(1)

    pulsante_avanti_credenziali = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1xmf6yo x1e56ztr x540dpk x1m39q7l x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1')]/button[text()='Avanti']")))
    cliccare_pulsante_avanti_credenziali = pulsante_avanti_credenziali.click()                           
    print(password_generata)

except Exception as errore:
    print(f"C'é stato un errore nella compilazone del modulo delle credenziali {errore}")


time.sleep(3)



try:
    menu_tendina_mese = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[1]/div/div[4]/div/div/span/span[1]/select")))
    scelta_mese = Select(menu_tendina_mese)
    mese_casuale = random.choice([opzione.get_attribute("value") for opzione in scelta_mese.options])
    scelta_mese.select_by_value(mese_casuale)
    print(f"Mese scelto: {mese_casuale}")

    time.sleep(1)

    menu_tendina_giorno = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[1]/div/div[4]/div/div/span/span[2]/select")))
    scelta_giorno = Select(menu_tendina_giorno)
    giorno_casuale = random.choice([opzione.get_attribute("value") for opzione in scelta_giorno.options])
    scelta_giorno.select_by_value(giorno_casuale)
    print(f"Giorno scelto: {giorno_casuale}")

    time.sleep(1)

    menu_tendina_anno = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[1]/div/div[4]/div/div/span/span[3]/select")))
    scelta_anno = Select(menu_tendina_anno)
    anno_casuale = random.choice([opzione.get_attribute("value") for opzione in scelta_anno.options if 1960 <= int(opzione.get_attribute("value")) <= 2005])
    scelta_anno.select_by_value(anno_casuale)
    print(f"Anno scelto: {anno_casuale}")

    time.sleep(1000000000000)
       
    pulsante_avanti_finale = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[1]/div/div[6]/button")))
    pulsante_avanti_finale.click()

except Exception as e:
    print(f"Errore durante la selezione della data di nascita o nel cliccare il pulsante avanti finale: {e}")

#time.sleep(6)

#recaptcha_iframe = driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')
#solver.click_recaptcha_v2(iframe=recaptcha_iframe)

time.sleep(3)


try:
    email_generata_divisa = email_generata.split("@")
    nomemail = email_generata_divisa[0]
    dominio_email = email_generata_divisa[1]

    codice_di_verifica = getInstVeriCode(mailName=nomemail, domain=dominio_email, driver=driver)
    print(f"Codice di verifica: {codice_di_verifica}")

    time.sleep(1)

    campo_codice_verifica = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[1]/div[2]/form/div/div[1]/input")))
    campo_codice_verifica.send_keys(codice_di_verifica)

    time.sleep(1)

    pulsante_avanti_codice_verifica = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[1]/div[2]/form/div/div[2]/div")))
    pulsante_avanti_codice_verifica.click()

    time.sleep(1000000000000)

except Exception as e:
    print(f"Errore nella compilazione del codice di verifica: {e}")

time.sleep(10)

with open("credenziali_instagram.txt", "a") as foglio_credenziali:
    foglio_credenziali.write(f"{email_generata}\n{password_generata}\n\n\n")
    print("Credenziali salvate con successo")


