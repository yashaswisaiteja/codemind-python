n=int(input())
s=0
k=1
while(n):
    d=n%10
    s=s+d
    k=k*d
    n=n//10
if s==k:
    print("Spy Number")
else:
    print("Not Spy Number")