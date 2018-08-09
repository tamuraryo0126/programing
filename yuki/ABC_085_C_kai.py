n,m=map(int,input().split())
for x in range(n+1):
    for y in range(n+1-x):
        if 10000*x+5000*y+1000*(n-x-y)==m:
            print(x,y,(n-x-y))
            exit()
print('-1 -1 -1')