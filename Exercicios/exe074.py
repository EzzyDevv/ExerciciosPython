from random import randint

numbers = (randint(0,50), randint(0,50), randint(0,50), randint(0,50), randint(0,50))
print("Os números gerados são {}".format(numbers))
print("O maior valor gerado foi {} e o menor é {}".format(max(numbers), min(numbers)))