# value_if_true if condition else value_if_false
a = 5
b = 10

rslt = "a is max" if a > b else "b is max"
print(rslt)

x = 5
y = 15
z = 10

rslt2 = "x is max" if x > y and x > z else "y is max" if y > z else "z is max"
print(rslt2)
