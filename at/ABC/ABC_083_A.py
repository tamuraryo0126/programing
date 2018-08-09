n,a,b=map(int,input().split())
ans=0
for i in range(n+1):
    if a<=sum(list(map(int,list(str(i)))))<=b:
        # 数字iを文字列に変換して、それをマップで一文字ずつリストに入れていく。
        # sumでリストの合計を出し、条件に一致するならば、足す。
        ans+=i
print(ans)