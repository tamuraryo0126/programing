N=int(input())
count=0
con_num=[]
while N>0:
    if N>=8:
        count+=1
        N-=8
        con_num.append(8)
    if N>=4:
        count+=1
        N-=4
        con_num.append(4)
    if N>=2:
        count+=1
        N-=2
        con_num.append(2)
    if N>=1:
        count+=1
        N-=1
        con_num.append(1)
print(count)
for num in con_num:
    print(num)
        
    
        
          