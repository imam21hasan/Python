n = input("Enter a text of numbers : ")   # "10 20 30 40"
list = n.split()
sum = 0

for i in list:
    sum += int(i)

print(list)
print(sum)
