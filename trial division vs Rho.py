from sympy import randprime
import time
from math import gcd
import random

def gen_n(bits):
    p = randprime(2**(bits//2 - 1), 2**(bits//2))
    q = randprime(2**(bits//2 - 1), 2**(bits//2))
    return p * q

def trial_division(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return None

def pollards_rho(n):
    if n % 2 == 0:
        return 2
    def f(x): return (x*x + 1) % n
    x = random.randrange(2, n-1)
    y = x
    d = 1
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
    return None if d == n else d

def measure(func, n):
    start = time.time()
    func(n)
    return time.time() - start

#실험 루프
bits_list = [30, 35, 40, 45]

results = []

for bits in bits_list:
    n = gen_n(bits)

    t_trial = measure(trial_division, n)
    t_rho   = measure(pollards_rho, n)

    results.append((bits, t_trial, t_rho))

for r in results:
    print(r)
