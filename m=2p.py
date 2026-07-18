from math import gcd

p = 61
q = 53
n = p*q
e = 17

m = 7*p  # 메시지를 2*p로 설정
c = pow(m, e, n)

print(gcd(c, n)) #p 나옴. 탈환 성
