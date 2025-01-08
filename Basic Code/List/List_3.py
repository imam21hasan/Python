name = ["Shwadheen", "Shawon", "Nayon", "Mohan", "Tuhin", "Araf"]

print(len(name))

pos = name.index("Nayon")
print(pos)

name.append("Ayash")  # add item
print(len(name))
print(name)

name.insert(5, "Fabiya")  # insert at index
print(name)

name.remove("Shawon")
print(name)

name.sort()
print(name)

name.reverse()
print(name)

name.pop()
print(name)
print("\n")

name2 = name.copy()
print(name2)

num = [5, 7, 6, 5, 1, 4, 5, 3, 5]
count = num.count(5)
print(count)