N=int(input())
sum=0
a=0
b=1
for i in range(N):
    if i==0:
        sum+=1
    else:
        a,b=b,a+b
        sum+=(b**2)%1000000007
print(sum)

