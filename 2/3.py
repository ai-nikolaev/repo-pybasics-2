n = int(input("Введите целое число n для формирования последовательности: "))
values = [round((1+1/n)**n, 2) for n in range(1, n + 1)]
print(f'Для n={n} {values}')
print(f'Сумма {sum(values)}')
