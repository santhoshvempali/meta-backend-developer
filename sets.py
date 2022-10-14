myset={1,2,3,"hello"}
myset2={4,5,5,6,7,8}

print(type(myset))

print(myset)
myset.add(6)
print(myset)

print(myset.union(myset2))
print(myset.difference(myset2))
print(myset.intersection(myset2))
print(myset.symmetric_difference(myset2))
print(myset^myset2) # symetrical difference