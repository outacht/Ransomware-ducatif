from cryptography.fernet import  Fernet
import socket

#generer une clé et l'afficher
key =  Fernet.generate_key()
print("votre key est: ",key)


#criation d'une socket et la mettre en écoute et accepter les clients
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 4321))
s.listen()

conn, addr = s.accept()
print(addr, "connected")


#recevoir les données
msg = conn.recv(2048).decode()
if msg == "key":
    conn.send(key)
    print("voici votre key")

