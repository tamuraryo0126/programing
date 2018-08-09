num_list=list(int(i) for i in input().split())
N=int(len(num_list))
ans_list=[]
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            ans=num_list[i]+num_list[j]+num_list[k]
            ans_list.append(ans)
ans_list.sort(reverse=True)
print(ans_list[2])
