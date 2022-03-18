import random


list = ["x"]
operations = ["*", "/", "+", "-"]
power = [0.5, (0), 1, 2, 3]

def moveGeneration():
    combinedList = operations + power

    randomIndex = random.randint(0, len(combinedList)-1)
    randomMove = combinedList[randomIndex]

    return randomMove

# 

def questionGeneration(randomMove):
    if randomMove in power:
        list.append(randomMove)
    else:
        list.insert(0, randomMove)

for x in range(0,5):
    questionGeneration(moveGeneration())

print(list)
