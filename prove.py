import requests
import re
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch_proxies():
    """
    Recupera i proxy da spys.me e free-proxy-list.net e restituisce una lista di proxy.

    Returns:
        list: Una lista di proxy nel formato 'IP:Port'.
    """
    proxies = []

    # Regex per identificare gli indirizzi IP e porte
    regex = r"[0-9]+(?:\.[0-9]+){3}:[0-9]+"

    # Recupera i proxy da spys.me
    try:
        response_spys = requests.get("https://spys.me/proxy.txt")
        response_spys.raise_for_status()  # Verifica se la richiesta ha avuto successo
        proxies_spys = re.findall(regex, response_spys.text, re.MULTILINE)
        proxies.extend(proxies_spys)
        print(f"Trovati {len(proxies_spys)} proxy da spys.me.")
    except requests.RequestException as e:
        print(f"Errore durante il recupero dei proxy da spys.me: {e}")

    # Recupera i proxy da free-proxy-list.net
    try:
        response_free_proxy = requests.get("https://free-proxy-list.net/")
        response_free_proxy.raise_for_status()  # Verifica se la richiesta ha avuto successo
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

def test_proxy(proxy, test_url="http://httpbin.org/ip"):
    """
    Testa un singolo proxy per verificarne il funzionamento.

    Args:
        proxy (str): Il proxy da testare.
        test_url (str): URL di test per verificare la funzionalità del proxy.

    Returns:
        str: Il proxy se funzionante, None altrimenti.
    """
    try:
        response = requests.get(test_url, proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            return proxy
    except Exception:
        return None

def test_proxies(proxies, test_url="http://httpbin.org/ip"):
    """
    Testa i proxy per verificare se funzionano in modo concorrente.

    Args:
        proxies (list): Lista di proxy da testare.
        test_url (str): URL di test per verificare la funzionalità dei proxy.

    Returns:
        list: Una lista di proxy funzionanti.
    """
    working_proxies = []

    with ThreadPoolExecutor(max_workers=1000) as executor:
        # Submit each proxy for testing
        future_to_proxy = {executor.submit(test_proxy, proxy, test_url): proxy for proxy in proxies}

        for future in as_completed(future_to_proxy):
            proxy = future_to_proxy[future]
            try:
                result = future.result()
                if result:
                    print(f"Proxy funzionante: {result}")
                    working_proxies.append(result)
                else:
                    print(f"Proxy non funzionante: {proxy}")
            except Exception as e:
                print(f"Errore con il proxy {proxy}: {e}")

    return working_proxies

# Esempio di utilizzo
if __name__ == "__main__":
    all_proxies = fetch_proxies()
    working_proxies = test_proxies(all_proxies)
    print("Lista di proxy funzionanti:", working_proxies)
