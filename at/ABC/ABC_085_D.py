N,H=map(int, input().split())
count=0
a=[];b=[]
for _ in range(N):
    ai,bi=map(int,input().split())
    a.append(ai);b.append(bi)
amax=max(a)
for x in b:
    if x>=amax and H>0: H-=x;count+=1
count-=(-H//amax)
print(count)