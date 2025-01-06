# 1^2+2^2+3^2+4^2+...+n^2
n = int(input("Enter the value of n : "))
sum = 0
for i in range(1, n+1, 1):
    sum += pow(i,2)
print(sum)


# 1^1+2^2+3^3+4^4+...+n^n
n = int(input("Enter the value of n : "))
sum = 0
for i in range(1, n+1, 1):
    sum += pow(i,i)
print(sum)

# 1/2+2/2+3/2+4/2+5/2+....+n/2
n = int(input("Enter the value of n : "))
sum = 0
for i in range(1, n+1, 1):
    sum += (i/2)
print(sum)