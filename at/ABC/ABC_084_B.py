a,b=map(int, input().split())
s=input()
if len(s)!=a+b+1: print("No"); quit()
for i in range(a+b+1):
    if i==a:
        if s[i]!="-": print("No"); quit()
    else:
        if "0">s[i] or s[i]>"9": print("No"); quit()
print("Yes")