import collections
_=input();num_dict=collections.Counter(map(int,input().split()))
count=0
for k in num_dict.items():
    if k[0]>k[1]:
        count+=k[1]
    elif k[0]<=k[1]:
        count+=k[1]-k[0]
print(count)
# 自力で完成