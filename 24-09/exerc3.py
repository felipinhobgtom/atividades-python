import random


def receba(lista):
    for i in range(1, 11):
        lista.append(random.randint(100, 200))
        print(lista)


print(receba([1, 2, 3]))
