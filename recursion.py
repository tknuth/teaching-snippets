# %%
def rsum(l):
    if not l:
        return 0
    return l[0] + rsum(l[1:])


rsum([1, 2, 3, 4])


# %%
def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)


factorial(5)


# %%
def fib(n):
    if n in [0, 1]:
        return n
    return fib(n - 1) + fib(n - 2)


fib(10)
