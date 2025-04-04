
from cryptography.fernet import Fernet

# Step 1: Generate and save a secret key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("[+] Key generated and saved.")

# Step 2: Load the secret key
def load_key():
    return open("secret.key", "rb").read()

# Step 3: Encrypt the text file
def encrypt_file(input_file, encrypted_file):
    key = load_key()
    fernet = Fernet(key)

    with open(input_file, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(encrypted_file, "wb") as enc_file:
        enc_file.write(encrypted)

    print("[+] File encrypted successfully.")

# Step 4: Decrypt the text file
def decrypt_file(encrypted_file, decrypted_file):
    key = load_key()
    fernet = Fernet(key)

    with open(encrypted_file, "rb") as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(decrypted_file, "wb") as dec_file:
        dec_file.write(decrypted)

    print("[+] File decrypted successfully.")

# Driver code
if __name__ == "__main__":
    generate_key()  # Run once to generate the key

    input_text = "message.txt"         # Original text file
    encrypted_text = "message.enc"
    decrypted_text = "message_decrypted.txt"

    # Make sure you have message.txt in the same folder
    encrypt_file(input_text, encrypted_text)
    decrypt_file(encrypted_text, decrypted_text)
