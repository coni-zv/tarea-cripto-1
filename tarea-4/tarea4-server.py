# SERVIDOR
from time import *
import os
import socket
import sys
import socket
import sqlite3

def decrypt():
    enc = open("encrypt.txt","r")
    for x in enc:
        temp = open("enc_temp.txt","w")
        temp.write(x)
        temp.close()
        de = os.system('ntru.py dec -i myKey.priv.npz enc_temp.txt>> decrypt.txt')
    print("desencriptado y guardado")

def saveDB():
    conn = sqlite3.connect('dec.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE hashes (id INTEGER PRIMARY KEY AUTOINCREMENT, hashval VARCHAR(255))''')
    d = open("decrypt.txt","r")
    for x in d:
        c.execute("INSERT INTO hashes(hashval) VALUES (?);",(x,))
        conn.commit()
    conn.close()



#NTRU: la libreria funciona mediante comandos por consola, es necesario que ntru.py este
#en la misma carpeta
print("generando llaves...")
keys = os.system("ntru.py gen 167 3 128 myKey.priv myKey.pub")
print("llaves creadas y guardadas")


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 12000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(100)
            msg1 = ("Llave publica?").encode()
            msg2 = ("encrypt.txt").encode()
            msg2_ok = ("desencriptado y guardado!").encode()
            print('received {!r}'.format(data))
            if data:
                if data==msg1:
                    file = 'myKey.pub.npz'
                    connection.sendall(file.encode())
                if data==msg2:                  
                    decrypt()
                    saveDB()
                    connection.sendall(msg2_ok)
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()

