N=int(input())
mousyo=0
manatu=0
natu=0
nettaiya=0
huyubi=0
mahuubi=0
        
for i in range(N):
    a,b=map(float,input().split())
    if a>=35:
        mousyo+=1
    elif 30<=a<35:
        manatu+=1
    elif 25<=a<30:
        natu+=1
    if a<0:
        mahuubi+=1
    if b>=25:
        nettaiya+=1
    if b<0 and a>=0:
        huyubi+=1
print(mousyo,manatu,natu,nettaiya,huyubi,mahuubi)
