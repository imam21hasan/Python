def adult(age):
    if age < 18:
        raise ValueError("You are not adult !!!")
    return "You are adult."


try:
    a = int(input("Enter your age : "))
    print(adult(a))

except ValueError as e:
    print(e)