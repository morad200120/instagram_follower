# guerrillamail_utils.py

from guerrillamail import GuerrillaMailSession
import time
import re

# Crea una nuova sessione GuerrillaMail
session = GuerrillaMailSession()

# Funzione che genera una nuova email
def generate_email():
    email_address = session.get_session_state()['email_address']
    print(f"Email generata: {email_address}")
    return email_address

# Funzione per ottenere il codice dall'email
def ottieni_codice():
    # Controlla la lista delle email ricevute
    emails = session.get_email_list()
    if emails:
        for email in emails:
            # Verifica se il mittente è Instagram
            if email.sender == "no-reply@mail.instagram.com":
                print(f"Oggetto: {email.subject}")
                
                # Cerca un codice numerico nell'oggetto dell'email
                match = re.search(r'\d{6}', email.subject)
                if match:
                    code = match.group(0)
                    print(f"Codice estratto dall'oggetto: {code}")
                    return code
                else:
                    print("Nessun codice trovato nell'oggetto.")
    else:
        print("Nessun messaggio ricevuto.")
