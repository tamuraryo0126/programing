N=int(input())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
cmax=0
for i in range(N):
    if cmax<sum(a1[:i+1])+sum(a2[i:]):
        cmax=sum(a1[:i+1])+sum(a2[i:])
print(cmax)