
import math
n = 3233
phi = 3120

# p + q 계산 (=S)
S = n - phi + 1
print("p + q =", S)


D=S*S-4*n
sqrtD=int(math.isqrt(D))

p=(S+sqrtD)//2
q=(S-sqrtD)//2

print(p,q)
