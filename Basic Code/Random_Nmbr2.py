import random

randomInt = random.randint(1, 10)   # a random integer between 1 and 10
print(randomInt)


randomFloat = random.random()   # a random float between 0.0 and 1.0
print(round(randomFloat, 2))


randomFloat = random.uniform(1.1, 15.5)   # a random float between 1.5 and 10.5
print(round(randomFloat, 2))


myList = [10, 20, 30, 40, 50]   # randomly select an element from the list
randomElement = random.choice(myList)
print(randomElement)


myList2 = [1, 2, 3, 4, 5]   # shuffle the list
random.shuffle(myList2)
print(myList2)


myList3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]   # get 4 unique random elements from the list
randomSample = random.sample(myList3, 4)
print(randomSample)


mySet = {10, 20, 30, 40, 50}
randomValue = random.choice(list(mySet))    # Convert the set to a list and select a random value
print(randomValue)