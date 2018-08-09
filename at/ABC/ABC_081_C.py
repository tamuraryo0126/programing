import collections
from collections import OrderedDict
count=0
N,K=map(int,input().split())
ball=list(map(str,input().split()))
c=sorted(collections.Counter(ball).values())
n=len(c)-K
if n==0:
    print(count)
else:
    for i in range(n):
        count+=c[i]
    print(count)
# 自力で解いたもの