N=input()
numlist=list(N)
numsum=0
for num in numlist:
    numsum+=int(num)
if int(N)%numsum==0:
    print('Yes')
else:
    print('No')