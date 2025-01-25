rslt = (lambda a, b: a+b)(10, 20)
print("Result : ", rslt)

rslt = (lambda a, b: a % b)(10, 4)
print("Result : ", rslt)


print("Result : ", (lambda a, b: a*a+2*a*b+b*b)(5, 10))

rslt3 = (lambda a: a*a*a)(5)
print("Cube of 5 is : ", rslt3)
