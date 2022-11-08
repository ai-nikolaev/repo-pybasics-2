n = int(input("Введите N: "))
result = [x for x in range(0, n + 1) if (x == 0 or x % 2 != 0) and (x*x < 200)]
print(f'{result}')
