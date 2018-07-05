N=int(input())
numlist=[int(i) for i in input().split(" ")]
numlist_n=sorted(numlist,reverse=True)
for i in numlist_n:
    print(numlist.index(i)+1)
