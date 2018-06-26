def jikan(a,h,m):
    if a+m>=60:
        h+=int((a+m)/60)
        m=int((a+m)%60)
    else:
        m+=a
    return h,m
def jikan_back(a,h,m):
    if a>m:
        h-=1
        m=60-a+m
    else:
        m-a
    return h,m
        
    
a,b,c=map(int,input().split())
N=int(input())
for i in range(N):
    hx,mx=map(int, input().split())
    h,m=jikan(a+b+c,hx,mx)
    if h<9:
        hb=h
        mb=m
    else:
        break
h,m=jikan_back(a,hb,mb)
print("{hour:02}:{minute:02}".format(hour=h,minute=m))

