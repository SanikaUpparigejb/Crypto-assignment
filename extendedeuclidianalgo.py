def extended_euclidean(a, b):
    
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclidean(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modular_inverse(a, m):
   
    gcd, x, _ = extended_euclidean(a, m)
    if gcd != 1:
        raise ValueError(f"Modular inverse does not exist for a={a} and m={m} (not coprime).")
    return x % m

if __name__ == "__main__":
    print("Modular Multiplicative Inverse Finder")
    a = int(input("Enter the number (a): "))
    m = int(input("Enter the modulo (m): "))
    try:
        mod_inverse = modular_inverse(a, m)
        print(f"The modular multiplicative inverse of {a} modulo {m} is: {mod_inverse}")
        print(f"Verification: ({a} * {mod_inverse}) % {m} = {(a * mod_inverse) % m}")
    except ValueError as e:
        print(e)

'''
OUTPUT:
1. Modular Multiplicative Inverse Finder
   Enter the number (a): 13
   Enter the modulo (m): 26
   Modular inverse does not exist for a=13 and m=26 (not coprime).
2. Modular Multiplicative Inverse Finder
   Enter the number (a): 11
   Enter the modulo (m): 26
   The modular multiplicative inverse of 11 modulo 26 is: 19
   Verification: (11 * 19) % 26 = 1
 '''  


