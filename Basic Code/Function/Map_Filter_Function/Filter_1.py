def num(x):
    if x % 2 == 0:
        return x

info = [1, 2, 3, 4, 5, 6]
rslt = list(filter(num, info))

print(rslt)


info2 = [10, 15, 20, 25, 30]
result = list(filter(lambda x: x % 2 != 0, info2))

print(result)
