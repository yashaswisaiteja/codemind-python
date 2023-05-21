n=int(input())
s=0
pro=1
while n>0:
    rem=n%10
    s=s+rem
    pro=pro*rem
    n=n//10
if s==pro:
    print("Spy Number")
else:
    print("Not Spy Number");