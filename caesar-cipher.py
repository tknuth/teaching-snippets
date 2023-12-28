from string import ascii_lowercase
import itertools as it

def rotate_letter(c, n):
    i = ascii_lowercase.find(c)
    if i == -1:
        return c
    alphabet = it.cycle(ascii_lowercase)
    for j in range(n+i+1):
        c = next(alphabet)
    return c

def rotate(m, n=13):
    return "".join([rotate_letter(c, n) for c in m])

rotate(rotate("Hallo, wie geht es dir?"))
