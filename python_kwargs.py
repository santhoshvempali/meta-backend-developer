def sum(**kwargs):
    sum=0
    for key,values in kwargs.items():
        if key=="cofee":
            sum+=values*25
        else:
            sum+=values
    return sum
print(sum(cofee=1,milk=2,sugar=0.8))