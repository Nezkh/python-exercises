from functools import reduce

n = int(input("Ingrese un numero: "))

resultado = list(filter(lambda x: x % 2 !=0, range(n+1)))
print(resultado)

resultado = reduce(lambda x, y: x + y, resultado)
print(resultado)