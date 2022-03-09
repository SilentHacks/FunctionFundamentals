import random

list = ["x"]

operations = ["*", "/", "+", "-"]

power = [0.5, (0), 1, 2, 3]

random_operation = random.randint(0, len(operations)-1)

print(operations[random_operation])