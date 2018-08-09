in_string=input()
st_list=list(in_string)
st_dict={"A":0,"B":0,"C":0,"D":0,"E":0,"F":0}
for st in st_list:
    st_dict[st]+=1

print(st_dict["A"],st_dict["B"],st_dict["C"],st_dict["D"],st_dict["E"],st_dict["F"])