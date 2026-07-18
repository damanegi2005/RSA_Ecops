def factor(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return i, n//i
    return None


n=31*73
p, q = factor(n)
print("p, q =", p, q)
