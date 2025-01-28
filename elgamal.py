def el_gamal():
    p = int(input("Enter a prime number p: "))
    g = int(input("Enter a generator g: "))
    d = int(input("Enter a private key d: "))
    e1 = g 
    e2 = pow(g, d, p) 

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

'''
OUTPUT:
Enter a prime number p: 43
Enter a generator g: 6
Enter a private key d: 9
Enter plaintext (as a number) for El-Gamal encryption: 789943
Enter a random number r: 4
Plaintext: 789943
Ciphertext: c1=6, c2=33
Decrypted: 33
'''
