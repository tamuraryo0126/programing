import sys
n,m=map(int,input().split())
for x in range(n+1):
    for y in range(n+1):
        for z in range(n+1):
            if 10000*x+5000*y+1000*z==m and x+y+z==n:
                print(x,y,z)
                sys.exit()
print("-1 -1 -1")

# TLE 実行時間エラー