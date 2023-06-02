n=int(input())
s=0
pro=1
while n:
    s+=n%10
    pro*=n%10
    n//=10
print(pro-s)