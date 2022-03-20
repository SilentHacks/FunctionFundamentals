import random


master = []
operations = ["*", "/", "+", "-"]
numbers = ["0.5", "0", "1", "2", "3"]

def tuple():
    randomIndexOperation = random.randint(0,len(operations)-1)
    indexOperation = operations[randomIndexOperation]

    randomIndexNumber = random.randint(0,len(numbers)-1)
    indexNumber = numbers[randomIndexNumber]

    list = [indexNumber, indexOperation]

    return list

def popper(list):
    randomIndexPopper = random.randint(0,len(list)-1)
    indexElement = list[randomIndexPopper]

    return indexElement

def equation(indexElement):
    ex = "x"
    power = "^"
    if indexElement in numbers:
        finalString = ex + power + indexElement
        return finalString
    else:
        randomNumber = str(random.randint(0,100))
        finalString = ex + indexElement + randomNumber
        return finalString


list = tuple()
value = popper(list)
print(equation(value))
