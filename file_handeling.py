file = open("functions.py", mode="rb")
data = file.readlines()
print(data)
file.close()


with open("sets.py", "rb") as file:
    data = file.read()
    print(data)

with open("dummy.py", "w") as file:
    file.write("""def sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(sum(1,2,3))""")


try:
    with open("dummdr.py", "r") as file:
        file.write("""def sum(*args):
        sum=0
        for i in args:
            sum+=i
        return sum
    print(sum(1,2,3))""")
except Exception as e:
    print("Error occured",e)
