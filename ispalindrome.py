menu=["code","books","likes","hello","donar"]

def find_cofee(coffee):
    if(coffee[0]=="c"):
        return coffee
map_ans=map(find_cofee,menu)
filter_ans=filter(find_cofee,menu)
print(map_ans)
for x in map_ans:
    print(x)
for y in filter_ans:
    print(y)

a = [[96], [69]]

print(''.join(list(map(str, a))))