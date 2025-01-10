from src.core.encryption import caesar_cipher_decrypt
from src.core.utils import read_file

def level1():
    print("Level 1: Password Retrieval")
    data = read_file("assets/levels/level1_data.txt")
    print(data)

    encrypted_password = "Sdfwlydwh"
    print("Decrypting password...")
    password = caesar_cipher_decrypt(encrypted_password, 3)
    print(f"Decrypted Password: {password}")

    return password
