a = int(input("Enter a number : "))

for i in range(2, a):
    if a % i == 0:
        print(f"{a} is not Prime Number")
        break
else:
    print(f"{a} is Prime Number")
