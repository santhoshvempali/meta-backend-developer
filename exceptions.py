def divide(a,b):
    return a/b

try:
    ans=divide(40,0)
    print(ans)
except Exception as e:
    print("Something went Wrong",e)