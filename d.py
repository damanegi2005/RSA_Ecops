#egcd, modinv, keygen 구현. rsa가 왜 factoring 문제로 귀결되는지, pi 값 알면 왜 ㅈ되는지. 

def egcd(a,b): #역원 존재성 판단, ax+by=gcd(a,b) 만족하는 계수 반환
    if b==0:
        return a,1,0
    g,x1,y1=egcd(b,a%b)
    return g,y1,x1-(a//b)*y1 #x=y1, y=x1-(a//b)&y1

def modinv(a,phi):
    #역원계산
    #위에서 gcd가 1이면 x가 역원임.
    g,x,c=egcd(a,phi)
    if g!=1:
        raise Exception("inverse 존재안함")
    else:
        return x%phi

def keygen(p,q):
    n=p*q
    phi=(p-1)*(q-1)

    e=65537
    if egcd(e,phi)[0]!=1:
        raise Exception("e와 phi 서로소 아님")

    d=modinv(e,phi)
    return (n,e), (n,d)

def encrypt(m,e,n):
    return pow(m,e,n) #m의 e승 mod n (r중간중간 %n 해줌)

def decrypt(c,d,n):
    return pow(c,d,n) #c의 d승 mod n

p=61
q=53
(pub,priv)=keygen(p,q) #공개키, 개인키 생성해서 넣기
n,e=703,11 #각각 대입
n,d=703,59

m=122

enc=689
dec=decrypt(enc,d,n)


print("m:",dec)
