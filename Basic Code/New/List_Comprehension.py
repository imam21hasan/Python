info = [1, 2, 3, 4, 5, 6]

rslt = [x for x in info]
print(rslt)

rslt2 = ["Python" for x in info]
print(rslt2)

rslt3 = ["Saon" for x in range(1, 5)]
print(rslt3)


rslt4 = [x for x in info if x % 2 == 0]
print(rslt4)

rslt5 = ["Yes" if x % 2 == 0 else "No" for x in info]
print(rslt5)

rslt6 = [x for x in range(20) if x < 11 and x % 2 == 0]
print(rslt6)
