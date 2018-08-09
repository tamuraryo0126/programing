a,b=map(str,input().split())
n=int(a+b)
if n==int(n**0.5)**2:
    print("Yes")
else:
    print("No")