x = 10
y = 55
z = 15
if x > y and x > z:
    print(x)
elif y > x and y > z:
    print(y)
else:
    print(z)


ch = input("Enter a character : ")
if ch == 'a' or ch == "e" or ch == 'i' or ch == 'o' or ch == 'u':
    print(f"{ch} is Vowel")
else:
    print(f"{ch} is Consonent")
