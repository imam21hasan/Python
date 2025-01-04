name = input("Enter your name : ")
print(name)
print("Name : "+name)

age = input("\nEnter your age : ")   # Always returns a string
print("Age : "+age)

a = input("\nEnter first num : ")
b = input("Enter second num : ")
print(a+b)

a = int(input("\nEnter first num : "))  # type casting
b = int(input("Enter second num : "))
print(a+b)
print("a + b = ", a+b)


m, n = input("Enter two values : ").split()   # Taking two inputs
print(m)
print(n)

w, x, y, z = input("Enter four values : ").split()
print(w, x, y, z)
print(w+x+y+z)
