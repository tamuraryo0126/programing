S=input()
str_list=list(S)
count=0
c_count=0
for st in str_list:
    if st=="+":
        count+=1
    else:
        c_count+=1
print(count-c_count)