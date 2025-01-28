def el_gamal():
    p = int(input("Enter a prime number p: "))
    g = int(input("Enter a generator g: "))
    d = int(input("Enter a private key d: "))
    e1 = g  # Public key component 1
    e2 = pow(g, d, p)  # Public key component 2

    plaintext = int(input("Enter plaintext (as a number) for El-Gamal encryption: "))
    r = int(input("Enter a random number r: "))

    c1 = pow(g, r, p)
    c2 = (plaintext * pow(e2, r, p)) % p

    decrypted = (c2 * pow(c1, p - 1 - d, p)) % p

    return plaintext, (c1, c2), decrypted

if __name__ == "__main__":
    plaintext, (c1, c2), decrypted = el_gamal()
    print("Plaintext:", plaintext)
    print(f"Ciphertext: c1={c1}, c2={c2}")
    print("Decrypted:", decrypted)
