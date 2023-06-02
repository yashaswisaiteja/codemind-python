n=int(input())
s=n*n
k=0
for i in str(s):
    k=k+int(i)
if(k==n):
    print("Neon Number")
else:
    print("Not Neon Number")