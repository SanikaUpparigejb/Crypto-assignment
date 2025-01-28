def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclidean(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def rsa_encrypt_decrypt():
    p, q = 61, 53  # Example primes
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17  # Public key exponent
    _, d, _ = extended_euclidean(e, phi)
    d = d % phi

    plaintext = input("Enter plaintext for RSA encryption: ")
    encrypted = [pow(ord(char), e, n) for char in plaintext]
    decrypted = "".join([chr(pow(char, d, n)) for char in encrypted])

    return plaintext, encrypted, decrypted

if __name__ == "__main__":
    plaintext, encrypted, decrypted = rsa_encrypt_decrypt()
    print("Plaintext:", plaintext)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
