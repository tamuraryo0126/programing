N=int(input())
a=N//4;b=N//7
for i in range(a+1):
    for j in range(b+1):
        if i*4+j*7==N:
            print("Yes")
            quit()
print("No")