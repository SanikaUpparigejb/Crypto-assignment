from math import gcd

def modular_inverse(a, m):
    gcd, x, _ = extended_euclidean(a, m)
    if gcd != 1:
        raise ValueError(f"Modular inverse does not exist for a={a}, m={m}")
    return x % m

def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclidean(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def affine_encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr(((a * (ord(char) - offset) + b) % 26) + offset)
        else:
            result += char
    return result

def affine_decrypt(cipher, a, b):
    result = ""
    a_inv = modular_inverse(a, 26)
    for char in cipher:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr(((a_inv * ((ord(char) - offset) - b)) % 26) + offset)
        else:
            result += char
    return result

if __name__ == "__main__":
    a = int(input("Enter value for a (must be coprime with 26): "))
    b = int(input("Enter value for b: "))
    text = input("Enter text to encrypt: ")
    cipher = affine_encrypt(text, a, b)
    print("Encrypted:", cipher)
    print("Decrypted:", affine_decrypt(cipher, a, b))

'''  
OUTPUT:
Enter value for a (must be coprime with 26): 67
Enter value for b: 23
Enter text to encrypt: have a good day
Encrypted: yxaf x jzzq qxt
Decrypted: have a good day
'''
