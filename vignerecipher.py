def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    key_len = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            key_char = ord(key[i % key_len]) - 65
            result += chr(((ord(char) - offset + key_char) % 26) + offset)
        else:
            result += char
    return result

def vigenere_decrypt(cipher, key):
    result = ""
    key = key.upper()
    key_len = len(key)
    for i, char in enumerate(cipher):
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            key_char = ord(key[i % key_len]) - 65
            result += chr(((ord(char) - offset - key_char) % 26) + offset)
        else:
            result += char
    return result

if __name__ == "__main__":
    text = input("Enter text to encrypt: ")
    key = input("Enter key: ")
    cipher = vigenere_encrypt(text, key)
    print("Encrypted:", cipher)
    print("Decrypted:", vigenere_decrypt(cipher, key))

'''
OUTPUT:
Enter text to encrypt: have a good day
Enter key: star
Encrypted: ztvv t xghd vty
Decrypted: have a good day
'''
