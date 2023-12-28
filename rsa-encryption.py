import collections
import random


def generate_prime(a, b):
    primes = [2]
    i = 3
    while primes[-1] < b:
        is_prime = all(i % prime != 0 for prime in primes)
        if is_prime:
            primes.append(i)
        i += 1
    return random.choice([p for p in primes if p >= a and p <= b])


def sample_coprime(n):
    return random.choice([i for i in range(1, n) if gcd(n, i) == 1])


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def are_coprime(a, b):
    return gcd(a, b) == 1


def transform(m, key):
    n, x = key
    return m**x % n


def encrypt(m, key):
    return hex(transform(m, key))


def decrypt(m, key):
    return transform(int(m, 16), key)


p = generate_prime(100, 151) # zufällige Primzahl
q = generate_prime(150, 200) # zufällige Primzahl
n = p * q
phi_n = (p - 1) * (q - 1)
e = sample_coprime(phi_n) # relativ prim zu phi_n
d = pow(e, -1, phi_n) # (d * e) mod phi_n = 1

private_key = (n, d)
public_key = (n, e)

m = 1000 # m < n

transform(transform(m, private_key), public_key)
decrypt(encrypt(m, private_key), public_key)
