s=input()
x,y=map(int,input().split())
x_list=[];y_list=[];Fsum=0;Xsum=0;Ysum=0;d="x"
for c in s:
    if c=='F':
        Fsum+=1
    elif c=="T":
        if d=="x":
            x_list.append(Fsum)
            Fsum=0;d="y"
        elif d=="y":
            y_list.append(Fsum)
            Fsum=0;d="x"
print(x_list,y_list)
for num in x_list:
    if x>=Xsum:
        Xsum+=num
    else:
        Xsum-=num
for num in y_list:
    if y>=Ysum:
        Ysum+=num
    else:
        Ysum-=num
if x==Xsum and y==Ysum:
    print("Yes")
else:
    print("No")
# わからん