N,a,b,c,d=map(int,input().split())

def fprice(n,p):
    count=0
    price=0
    while N>count:
        count+=n
        price+=p
    return price
if fprice(a,b)>=fprice(c,d):
    print(fprice(c,d))
else:
    print(fprice(a,b))