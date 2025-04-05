
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("[+] Key generated and saved.")

def load_key():
    return open("secret.key", "rb").read()


def encrypt_file(input_file, encrypted_file):
    key = load_key()
    fernet = Fernet(key)

    with open(input_file, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(encrypted_file, "wb") as enc_file:
        enc_file.write(encrypted)

    print("[+] File encrypted successfully.")

def decrypt_file(encrypted_file, decrypted_file):
    key = load_key()
    fernet = Fernet(key)

    with open(encrypted_file, "rb") as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(decrypted_file, "wb") as dec_file:
        dec_file.write(decrypted)

    print("[+] File decrypted successfully.")


if __name__ == "__main__":
    generate_key()  

    input_text = "message.txt"         
    encrypted_text = "message.enc"
    decrypted_text = "message_decrypted.txt"

    
    encrypt_file(input_text, encrypted_text)
    decrypt_file(encrypted_text, decrypted_text)
