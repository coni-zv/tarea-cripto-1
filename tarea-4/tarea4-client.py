# CLIENTE

from time import *
import os
import hashlib
import socket

def dehash():
    #OJO: cambiar directorio para probar
    cd = "cd C:\\Users\\RV\\Documents\\Jun\\universidad\\2020-2\\cripto\\tarea4\\tarea4"
    p0 = os.system(cd)
    # los archivos hash y dict se dejaron en la carpeta de hashcat

    #archivo 1: hash MD5 --> -m 0 
    cmd1 = "hashcat.exe -m 0 -a 0 -o out1.txt --outfile-format=2 archivo_1 diccionario_2.dict"
    start_time = time()
    p1 = os.system(cmd1)
    tiempo1 = time()-start_time
    f1_t = open("archivo1-de-t.txt","w")
    f1_t.write(str(tiempo1))
    f1_t.close()
    os.system("del hashcat.potfile")

    #archivo 2: hash md5($plaintext.$salt) --> -m 10
    cmd2 = "hashcat.exe -m 10 -a 0 -o out2.txt --outfile-format=2 archivo_2 diccionario_2.dict"
    start_time = time()
    p2 = os.system(cmd2)
    tiempo2 = time()-start_time
    f2_t = open("archivo2-de-t.txt","w")
    f2_t.write(str(tiempo2))
    f2_t.close()
    os.system("del hashcat.potfile")

    #archivo 3: hash md5($plaintext.$salt) --> -m 10
    cmd3 = "hashcat.exe -m 10 -a 0 -o out3.txt --outfile-format=2 archivo_3 diccionario_2.dict"
    start_time = time()
    p3 = os.system(cmd3)
    tiempo3 = time()-start_time
    f3_t = open("archivo3-de-t.txt","w")
    f3_t.write(str(tiempo3))
    f3_t.close()
    os.system("del hashcat.potfile")

    #archivo 4: NTLM --> -m 1000
    cmd4 = "hashcat.exe -m 1000 -a 0 -o out4.txt --outfile-format=2 archivo_4 diccionario_2.dict"
    start_time = time()
    p4 = os.system(cmd4)
    tiempo4 = time()-start_time
    f4_t = open("archivo4-de-t.txt","w")
    f4_t.write(str(tiempo4))
    f4_t.close()
    os.system("del hashcat.potfile")

    #archivo 5: SHA-512 Crypt UNIX --> -m 1800
    cmd5 = "hashcat.exe -m 1800 -a 0 -o out5.txt --outfile-format=2 archivo_5 diccionario_2.dict"
    start_time = time()
    p5 = os.system(cmd5)
    tiempo5 = time()-start_time
    f5_t = open("archivo5-de-t.txt","w")
    f5_t.write(str(tiempo5))
    f5_t.close()
    os.system("del hashcat.potfile")

    return


def hashing():
    start_time = time()
    for i in range(0,5):
        out = open("out"+str(i+1)+".txt","r")
        for x in out:
            hashed = open("hashed"+str(i+1)+".txt","a")
            #h = hashlib.sha3_224(x.encode())
            h = hashlib.blake2b(digest_size=8)
            h.update(x.encode())
            hashed.write(h.hexdigest()+"\n")
    tiempo = time()-start_time
    hash_t = open("hashed_t.txt","w")
    hash_t.write(str(tiempo))


            
dehash()
    
hashing()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 12000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    # Send data
    message1 = b'Llave publica?'
    print('sending {!r}'.format(message1))
    sock.sendall(message1)
    # Look for the response
    amount_received = 0
    amount_expected = 1024

    while amount_received < amount_expected:
        data = sock.recv(1024) #el nombre del archivo de llave publica
        amount_received += len(data)
        print('received {!r}'.format(data))
        pubkey = data.decode()
        # se encriptan archivos con la llave publica. 
        print("encriptando archivos (puede demorar un par de horas...)")
        for i in range(0,5):
            hashed = open("hashed"+str(i+1)+".txt","r")
            for x in hashed:
                # esta biblioteca funciona bien si encripta strings de 16 caracteres como maximo
                hash_temp = open("hash_temp.txt","w")
                hash_temp.write(x)
                hash_temp.close()
                e = os.system('ntru.py -o enc '+str(pubkey)+' hash_temp.txt>> encrypt.txt')
            print("encriptado archivo "+str(i+1))
        break
    message2 = b'encrypt.txt'
    print('sending {!r}'.format(message2))
    sock.sendall(message2)
    amount_received = 0
    amount_expected = 1024
    while amount_received < amount_expected:
        data = sock.recv(1024)
        amount_received += len(data)
        print('received {!r}'.format(data))
        break
        
    
finally:
    print('closing socket')
    sock.close()
