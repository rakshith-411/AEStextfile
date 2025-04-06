# 🔐 Text File Encryption & Decryption using AES (Fernet)

This  project demonstrates how to encrypt and decrypt text files using Python's `cryptography` library and AES-based Fernet encryption.
# Video Demo
[![YouTube](https://github.com/rakshith-411/AEStextfile/issues/5#issue-2975076329)](https://www.youtube.com/watch?v=qu23scdH_Z8)

## 🚀 Features

- Encrypt a `.txt` file to secure sensitive data
- Decrypt encrypted files using a secret key
- Easy-to-use Python script
- Implements AES encryption (via Fernet)

## 🛠️ Technologies Used

- Python 3.x
- cryptography (Fernet) module

## 📂 Project Structure

```
📁 TextFileEncryption
├── text_file_encrypt_decrypt.py  # Main script
├── message.txt                   # Original message
├── message.enc                   # Encrypted file
├── message_decrypted.txt        # Decrypted result
├── secret.key                    # Encryption key
```

## 💻 How to Run

1. Make sure Python is installed on your system.
2. Install the required library:
   ```
   pip install cryptography
   ```
3. Run the script:
   ```
   python text_file_encrypt_decrypt.py
   ```

The script will:
- Create an encrypted version of the file (`message.enc`)
- Then decrypt it and save as `message_decrypted.txt`

## 📌 Example Use Case

Use this for:
- Protecting logs or private notes
- Securing password files
- Practicing cryptography and cybersecurity basics

## 📃 License

This project is open for learning and educational use.
