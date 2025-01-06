# 1+2+3+4+5+....+n
n = int(input("Enter the value of n : "))
sum = 0
for i in range(1, n+1, 1):
    sum += i
print(sum)


# 2+4+6+8+...+n
n = int(input("Enter the value of n : "))
sum = 0
for i in range(2, n+1, 2):
    sum += i
print(sum)


# 1+3+5+7+...+n
n = int(input("Enter the value of n : "))
sum = 0
for i in range(1, n+1, 2):
    sum += i
print(sum)
