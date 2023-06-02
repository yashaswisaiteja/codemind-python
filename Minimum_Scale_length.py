def GCD(x,y):
    i=1
    gcd=0
    while i<=x and i<=y:
        if x%i==0 and y%i==0:
            gcd=i
        i+=1
    return gcd
n=int(input())
a=list(map(int,input().split()))
n1=a[0]
n2=a[1]
gcd=GCD(n1,n2)
for i in range(2,len(a)):
    gcd=GCD(gcd,a[i])
print(gcd)