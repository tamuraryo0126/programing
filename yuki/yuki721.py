import calendar
days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
y,m,d=map(int,input().split("/"))
if calendar.isleap(y):
    days[2]=29
d+=2
if d>days[m]:
    d-=days[m]
    m+=1
if m>12:
    m=1
    y+=1
print(f"{y:04}/{m:02}/{d:02}")