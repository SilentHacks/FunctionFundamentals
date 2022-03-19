from math import comb
import random
from shutil import move

list = []
operations = ["*", "/", "+", "-"]
power = [0.5, (0), 1, 2, 3]

def moveGeneration():
    combinedList = operations + power

    randomIndex = random.randint(0, len(combinedList)-1)
    randomMove = combinedList[randomIndex]

    print(randomMove)


def questionGeneration():
    pass

moveGeneration()
