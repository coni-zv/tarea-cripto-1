import imaplib
import re

#obtiene arreglo con valores en archivo de texto
def load_vals(filename):
    f = open(filename,"r")
    x = (f.read())
    l = re.split(",",x)
    return l

#formato de valores.txt: mail del emisor(entre ""),expresion regular,fecha
L = load_vals("valores.txt")
sender = L[0]
regex = L[1]
date = L[2]

#formato de login.txt: mail,contraseña
login = load_vals("login.txt")
imap_host = 'imap.gmail.com'
imap_user = login[0]
imap_pass = login[1]
print("Iniciaste sesion")

# conectar al host usando SSL
imap = imaplib.IMAP4_SSL(imap_host)

## login al server
imap.login(imap_user, imap_pass)

imap.select('Inbox')

status, response =  imap.search(None, 'FROM',sender, '(SINCE "'+date+'")')

print("regex: ",regex)
matches = 0
falsos = 0
for num in response[0].split():
    print(num)
    status, raw_mail = imap.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
    data = raw_mail[0][1].decode()
    clean = re.sub("\r\n\r\n","",data)
    print(clean)
    mid = re.sub("Message-ID: <","",clean)
    mid = re.sub(">","",mid)
    match = re.fullmatch(regex,mid)
    if match:
        print(num,": Match!\n")
        matches+=1
    else:
        print(num,": No match. Correo falso.\n")
        falsos+=1
print("Tienes ",falsos+matches," mensajes, de los cuales ",falsos," son correos falsos")

imap.close()
