import requests
import re
from bs4 import BeautifulSoup

def fetch_proxies():
    proxies = []

    regex = r"[0-9]+(?:\.[0-9]+){3}:[0-9]+"


    try:
        response_spys = requests.get("https://spys.me/proxy.txt")
        response_spys.raise_for_status()
        proxies_spys = re.findall(regex, response_spys.text, re.MULTILINE)
        proxies.extend(proxies_spys)
        print(f"Trovati {len(proxies_spys)} proxy da spys.me.")
    except requests.RequestException as e:
        print(f"Errore durante il recupero dei proxy da spys.me: {e}")

    try:
        response_free_proxy = requests.get("https://free-proxy-list.net/")
        response_free_proxy.raise_for_status()
        soup = BeautifulSoup(response_free_proxy.content, 'html.parser')
        td_elements = soup.select('.fpl-list .table tbody tr td')
        
        for j in range(0, len(td_elements), 8):
            ip = td_elements[j].text.strip()
            port = td_elements[j + 1].text.strip()
            proxy = f"{ip}:{port}"
            proxies.append(proxy)

        print(f"Trovati {len(td_elements)//8} proxy da free-proxy-list.net.")
    except requests.RequestException as e:
        print(f"Errore durante il recupero dei proxy da free-proxy-list.net: {e}")

    return proxies