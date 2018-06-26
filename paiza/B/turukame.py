
def turukame(a,b,c,d):
    kame=(c*b-a)/(c-d)
    turu=b-kame
    if kame.is_integer()==True and turu.is_integer()==True:
        if turu>0 and kame>0:
            print(int(turu),int(kame))
        else:
            print("miss")
    else:
        print("miss")

a,b,c,d=map(int, input().split())
if a==b and c==d:
    if a==c+d:
        print("1 1")
    else:
        print("miss")
elif c==d:
    print("miss")
else:
    turukame(a,b,c,d)