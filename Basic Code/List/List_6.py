letter = 0
word = 0
digit = 0

item = input("Enter a text : ")

for x in item:
    if (x >= 'a' and x <= 'z') or (x >= "A" and x <= 'Z'):
        letter += 1
    if x >= '0' and x <= '9':
        digit += 1
    if x == " ":
        word += 1

print("Number of letters : ", letter)
print("Number of words : ", word+1)
print("Number of digits : ", digit)
