N=int(input())
card=list(map(int,input().split()))
card=sorted(card, reverse=True)
a=0
b=0
for i in range(N):
    if i%2==0:
        a+=card.pop(0)
    else:
        b+=card.pop(0)
print(abs(a-b))