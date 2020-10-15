from Crypto.Cipher import DES3
from Crypto import Random
from Crypto.Util.Padding import pad
#from Crypto.Util.Padding import unpad
from base64 import b64encode, b64decode
import binascii

def pad(data):
    length = 16 - (len(data) % 16)
    data = data.decode() + chr(length)*length
    return data.encode()

def unpad(data):
    return data[:-ord(data[-1])]

'''
def encrypt(message, passphrase):
    IV = Random.new().read(BLOCK_SIZE)
    cipher_enc = DES3.new(passphrase, DES3.MODE_OFB, IV)
    return b64encode(IV + cipher_enc.encrypt(pad(message)))

def decrypt(enc,key):
    iv = enc[:BLOCK_SIZE]
    cipher_dec = DES3.new(key,DES3.MODE_OFB,iv)
    dec = cipher_dec.decrypt(enc)
    return unpad(b64decode(dec[BLOCK_SIZE:]))
'''
'''
def encrypt(msg,key):
    iv = Random.new().read(BLOCK_SIZE)
    cipher_enc = DES3.new(key,DES3.MODE_OFB,iv)
    enc = cipher_enc.encrypt(pad(text))
    return iv+enc
'''
def encrypt(message, passphrase):
    IV = Random.new().read(BLOCK_SIZE)
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
    if len(key)==16 or len(key)==24:
        msg = msg.encode()
        key = key.encode()
        e = encrypt(msg,key)
        create_html(e,key)
        print("mensaje encriptado: ",e)
        return e
    else:
        print(len(key))
        print("Error: ingrese llave de nuevo")
        programa()


def create_html(enc,key):
    text = """
    <p>Este sitio contiene un mensaje secreto</p>
    <div class="tripledes" id='"""+enc.decode()+"""'></div>
    <div class="key" id='"""+key.decode()+"""'></div>
    <div class="mensaje" id="mensaje"></div>    """
    with open(r"archivo_tarea.html", 'w') as html:
        html.write(text)


BLOCK_SIZE=8
'''
key = b'sixteen byte key'
text = b"que tengas un buen dia! "
e = encrypt(text,key)
hex_e =binascii.hexlify(e).upper()
hex_key=binascii.hexlify(key).upper()
b64_e = b64encode(e)
de=decrypt(e,key)
print("encrypt:")
print(e)
print("hex enc:")
print(hex_e)
print("b64 enc:")
print(b64_e)
print("hex key:")
print(hex_key)
#print("dec:")
#print(de)
'''
'''
text = """
<p>Este sitio contiene un mensaje secreto</p>
<div class="3DES" id='"""+e.decode()+"""'></div>
<div class="key" id='"""+key.decode()+"""'></div>
<div class="hex_key" id='"""+hex_key.decode()+"""'></div>
<div class="mensaje" id="mensaje"></div>
"""
with open(r"archivo3.html", 'w') as html:
    html.write(text)
'''
