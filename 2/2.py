import math

N = int(input("Введите целое число N: "))
values = range(1, N + 1)
print(
    f"пусть N = {N}, тогда {[math.prod(range(1, x + 1)) for x in values]} {tuple([f'*'.join([f'{y}' for y in range(1, x + 1)]) for x in values])}")
