import math
import random


N = int(input("Введите N: "))
print(f'N={N}')
all_values = [random.randint(-N, N) for x in range(-N, N + 1)]
print(f'Пример списка чисел: {all_values}')
left_index = int(input("Введите индекс левой границы массива: "))
if left_index < 0 or left_index > len(all_values):
    print(
        f'Ошибка! Левая граница [{left_index}] должна быть в диапазоне [0, {len(all_values) - 1}]!')
    exit(1)
right_index = int(input("Введите индекс правой границы массива: "))
if right_index < left_index or right_index > len(all_values):
    print(
        f'Ошибка! Правая граница [{right_index}] должна быть в диапазоне [{left_index}, {len(all_values) - 1}]!')
    exit(1)
print(f'Границы диапазона: {left_index}, {right_index}')
slice_values = all_values[left_index:right_index + 1]
print(f'Произведение для {slice_values} равно {math.prod(slice_values)}')
