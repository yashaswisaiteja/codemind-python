n=int(input())
a=list(map(int,input().split()))
b=max(a)
for j in range(b,0,-1):
    c=0
    for i in range(n):
        if(a[i]%j==0):
            c+=1
    if(c==n):
        print(j)
        break