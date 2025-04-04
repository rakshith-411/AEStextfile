
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os

# Generate or load key
def load_key():
    if os.path.exists("secret.key"):
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    else:
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        return key

key = load_key()
fernet = Fernet(key)

def encrypt_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filepath:
        with open(filepath, "rb") as file:
            original = file.read()
        encrypted = fernet.encrypt(original)
        with open("message.enc", "wb") as encrypted_file:
            encrypted_file.write(encrypted)
        messagebox.showinfo("Success", "File Encrypted Successfully!")

def decrypt_file():
    filepath = filedialog.askopenfilename(filetypes=[("Encrypted files", "*.enc")])
    if filepath:
        with open(filepath, "rb") as file:
            encrypted = file.read()
        try:
            decrypted = fernet.decrypt(encrypted)
            with open("message_decrypted.txt", "wb") as decrypted_file:
                decrypted_file.write(decrypted)
            messagebox.showinfo("Success", "File Decrypted Successfully!")
        except Exception as e:
            messagebox.showerror("Error", "Decryption Failed!")

# GUI setup
app = tk.Tk()
app.title("AES Text File Encryptor")
app.geometry("300x150")
app.resizable(False, False)

encrypt_button = tk.Button(app, text="Encrypt Text File", command=encrypt_file, width=25, pady=5)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(app, text="Decrypt Encrypted File", command=decrypt_file, width=25, pady=5)
decrypt_button.pack(pady=10)

app.mainloop()
