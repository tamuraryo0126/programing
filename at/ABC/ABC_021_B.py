N=int(input())
s,g=map(int, input().split())
M=int(input())
numlist=[int(i) for i in input().split()]
res=set(numlist)

if max(numlist)>N:
    print("NO")
elif (s or g) in numlist:
    print("NO")
elif len(numlist)!=len(res):
    print("NO")
else:
    print("YES")
    