import requests
from bs4 import BeautifulSoup

def generatore_email_fake():
    url = 'https://email-fake.com/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    mail_element = soup.find("span", {"id": "email_ch_text"})
    mail = mail_element.get_text(strip=True)  # Ottieni il testo come stringa e rimuovi spazi indesiderati
    return mail