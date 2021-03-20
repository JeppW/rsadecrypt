from Crypto.Util.number import *
from math import gcd

# change these below values
# leave unknown values as 0, the program will do the calculations

# ciphertext
c = 0
# product of primes p and q (part of public key and private key)
n = 0
# public exponent e (part of public key)
e = 65537

# we need one of the below prime numbers to get the other part of the private key (private exponent d)
# first prime number
p = 0
# second prime number
q = 0

# the private exponent
# we usually don't have this one, but in case we do, put it here
d = 0


def solve(p, q, n, d):
    if not p and not q and not d:
        print("We don't have enough information to get the private key. We need one of the two primes, q or p, or the private exponent d.\n")
        exit()

    if not p and q:
        p = n // q
    elif not q and p:
        q = n // p
    if not n and p and q:
        n = p * q  # in case we have both p and q, but not n (unlikely)

    return p,q,n


def lcm(x, y):
    return (x * y) // gcd(x, y)


def ex_euclid(x, y):
    c0, c1 = x, y
    a0, a1 = 1, 0
    b0, b1 = 0, 1

    while c1 != 0:
        m = c0 % c1
        q = c0 // c1

        c0, c1 = c1, m
        a0, a1 = a1, (a0 - q * a1)
        b0, b1 = b1, (b0 - q * b1)
    return a0, b0


def decrypt(c, d, n):
    m = pow(c, d, n)
    print("Decrypted text: " + long_to_bytes(m).decode('utf8'))
    exit()


p,q,n = solve(p, q, n, d)

if d and n:
    decrypt(c, d, n)

t = lcm(p - 1, q - 1)   # "t" for totient function
a, b = ex_euclid(e, t)
d = a % t   # get secret value "d"
print(d)

decrypt(c, d, n)
