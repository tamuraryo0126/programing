n,k=map(int,input().split());ans=0
for i in range(1,n+1):
    if n%i!=0:ans+=(n-i)*(n//i)+(n%i)-1
    else: ans+=(n-i)*(n//i)
print(ans)