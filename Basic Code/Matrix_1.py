matrix = [
    [10, 20, 30],
    [40, 50, 60]
]

print(matrix[1][1])
print(matrix[1][2])

matrix[1][2] = 100
print(matrix[1][2])

for row in matrix:
    print(row)
print("\n")

for row in matrix:
    for col in row:
        print(col, end="  ")
    print("\n")
