# 1*2*3*4*....*n
n = int(input("Enter the value of n : "))
sum = 1
for i in range(1, n+1, 1):
    sum *= i
print(sum)