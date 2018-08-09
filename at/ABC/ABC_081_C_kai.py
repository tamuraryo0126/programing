import collections
N,K=map(int,input().split())
c=sorted(collections.Counter(list(map(str,input().split()))).values())
print(sum(c[:-K]))
# 他人のコードを参考に改良したもの