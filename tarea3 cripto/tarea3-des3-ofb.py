from Crypto.Cipher import DES3
from Crypto import Random
from base64 import b64encode, b64decode

def encrypt(message, passphrase,IV):
    cipher_enc = DES3.new(passphrase, DES3.MODE_OFB, IV)
    return b64encode(IV + cipher_enc.encrypt(message))

def decrypt(encrypted, passphrase):
    encrypted = b64decode(encrypted)
    IV = encrypted[:BLOCK_SIZE]
    cipher_dec = DES3.new(passphrase, DES3.MODE_OFB, IV)
    return cipher_dec.decrypt(encrypted[BLOCK_SIZE:])

def programa():
    msg = input("Ingrese mensaje a encriptar: ")
    key = input("Ingrese llave (debe tener 16 o 24 caracteres!): ")
    iv = input("Ingrese IV (debe tener 8 caracteres!): ")
    if (len(key)==16 or len(key)==24) and len(iv)==8:
        msg = msg.encode()
        key = key.encode()
        iv = iv.encode()
        e = encrypt(msg,key,iv)
        create_html(e,key,iv)
        print("mensaje encriptado: ",e)
        de = decrypt(e,key).decode()
        print("mensaje desencriptado: ",de)
        return e
    else:
        print(len(key))
        print("Error: cantidad de caracteres incorrecta")
        print("largo key: ",len(key))
        print("largo iv: ",len(iv))
        programa()


def create_html(enc,key,iv):
    text = """
    <p>Este sitio contiene un mensaje secreto</p>
    <div class="tripledes" id='"""+str(enc.decode())+"""'></div>
    <div class="iv" id='"""+str(iv.decode())+"""'></div>
    <div class="key" id='"""+str(key.decode())+"""'></div>
    <div class="mensaje" id="mensaje"></div>    """
    with open(r"archivo_tarea.html", 'w') as html:
        html.write(text)

BLOCK_SIZE=8
programa()

