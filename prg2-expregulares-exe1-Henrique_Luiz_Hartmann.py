import re
email = input('Digite um Email: ')

def verifica_email(email):
    r = re.match(r'^[\w-]+@(?:[a-zA-Z0-9-])+(.com(.[a-zA-Z]{2,})*)$', email)
    if r:
        print("E-mail válido")
    else:
        print("E-mail Inválido")

verifica_email(email)
