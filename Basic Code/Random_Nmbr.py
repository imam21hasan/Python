from random import randint
n = int(input("Guess a number : "))

randomNmbr = randint(1, 5)
if (n == randomNmbr):
    print("Guess Successful")
else:
    print("Guess Failed !!!")
    print(f"The random number was {randomNmbr}")
