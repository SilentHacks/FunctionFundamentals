import random

operations = ["*", "/", "+", "-"]
numbers = ["0.5", "1", "2", "3"]


def randomElement():
    # chooses random element from each list
    randomIndexOperation = random.randint(0, len(operations) - 1)
    indexOperation = operations[randomIndexOperation]

    randomIndexNumber = random.randint(0, len(numbers) - 1)
    indexNumber = numbers[randomIndexNumber]

    # pops one out from list
    list = [indexNumber, indexOperation]
    randomIndexPopper = random.randint(0, len(list) - 1)
    indexElement = list[randomIndexPopper]

    return indexElement


def equation(finalString):
    indexElement = randomElement()
    # brackets around equation if necessary
    if (len(finalString)) > 1:
        finalString = "(" + finalString + ")"

    # force power to equation
    if (len(finalString)) > 1:
        if (finalString[2] or finalString[1]) in operations:
            randomIndexNumber = random.randint(0, len(numbers) - 1)
            indexNumber = numbers[randomIndexNumber]

            finalString = finalString + "^" + indexNumber

            return finalString
            # power
    if indexElement in numbers:
        finalString = finalString + "^" + indexElement
        return finalString

        # basic arithmetic
    else:
        randomNumber = str(random.randint(0, 100))
        finalString = finalString + indexElement + randomNumber
        return finalString


def get_equation():
    equation_str = "x"
    for _ in range(3):
        equation_str = equation(equation_str)

    return equation_str
