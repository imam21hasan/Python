x = {1, 2, 3, 4, 5}
y = {4, 5, 6, 7, 8}
z = {1, 2, 3}

print(x | y)    # union
print(x.union(y))

print(x & y)    # intersection
print(x.intersection(y))

print(x-y)  # difference
print(x.difference(y))
print(y.difference(x))

print(x^y)  # symmetric difference
print(x.symmetric_difference(y))

print(z.issubset(x))

print(x.issuperset(z))
