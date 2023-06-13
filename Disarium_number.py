n=int(input())
length=len(str(n))
t=n
s=0
rem=0
while t>0:
    rem=t%10
    s=s+int(rem**length)
    t=t//10
    length=length-1
if s==n:
    print("True")
else:
    print("False")