# 분해 알고리즘

import random
from math import gcd

def trial_division(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return None



def pollards_rho(n): 
    if n % 2 == 0:
        return 2

    # f(x) = x^2 + 1 mod n 으로 두자.
    def f(x):
        return (x*x + 1) % n

    x = random.randrange(2, n-1)
    y = x
    d = 1

    while d == 1:
        x = f(x)          #1 step
        y = f(f(y))       #2 step
        d = gcd(abs(x - y), n)

    if d == n: #x=y(mod n) 완전히 같은 상태..
        return None       # 실패, 다시 랜덤으로 시도. 
    return d



n = 61 * 53
factor = pollards_rho(n)

print("found factor:", factor)
print("other factor:", n // factor)
