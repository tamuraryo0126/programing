import math
N=int(input())
numlist=[int(input()) for i in range(N)]
numlist.sort(reverse=True)
ans=0.0
for i in range(N):
    if i%2==0:
        ans+=numlist[i]**2
    else:
        ans-=numlist[i]**2
print(ans*math.pi)
