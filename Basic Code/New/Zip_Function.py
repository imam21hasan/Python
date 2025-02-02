id = [1, 2, 3]
name = ['Shwadheen', 'Shawon', 'Nayon']

print(list(zip(id, name)))
print(list(zip(id, name, 'ABC')))

rslt = zip(id, name)
print(list(rslt))

id2 = [4, 5]
rslt2 = zip(id2, name)
print(list(rslt2))

zipped = [(1, 'Imam'), (2, 'Hasan'), (3, 'Shawon')]

unzipped = zip(*zipped)
list1, list2 = list(unzipped)
print(list1)
print(list2)


for i, n in zip(id, name):
    print(f"{i} : {n}")
