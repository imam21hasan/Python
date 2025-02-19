try:
    n = int(input("Enter the first number : "))
    m = int(input("Enter the second number : "))
    rslt = n/m
    print(rslt)
    print("Result print succesfully")

except (ValueError, ZeroDivisionError):
    print("Incorrect input !!!")

finally:
    print("Final stage")
