square = lambda x: pow(x, 2)


def cuadrado(x):
    return pow(x, 2)

#print(cuadrado(3))

numbers = 1, 2, 3, 4, 5, 6, 7, 8

#print(list(map(cuadrado, numbers)))

print(list(filter(lambda n: n % 2 == 1, numbers)))