# Tuples are unchangeable

emptyTuple = ()    # Empty tuple
if len(emptyTuple) == 0:
    print("The tuple is empty !!!")

singleItem = (5,)  # Tuple with one item (note the comma)

multiItem = (1, 2, 3)

mixedItem = (1, "hello", True, 3.14)
print(mixedItem[1])

tuplePacking = 1, 2, 3     # Tuple without parentheses
print(tuplePacking[2])

info = (10, 20, 30, 40)

print(info[1])
print(info[2:4])

for item in info:
    print(item)
print("\n")

info2 = (1, 2, 3, 4, 5)
a, *b = info2
print(a)
print(b)


info3 = (1, 2, 2, 3, 4, 2)   # count duplicate item
print(info3.count(2))

info4 = (10, 20, 30, 40, 50)    # find index
print(info4.index(20))

info5 = (
    ("Imam hasan", 28, 3.5),
    "Imam Hossain",
    "Shwadheen"
)
print(info5[0])
print(info5[0:])