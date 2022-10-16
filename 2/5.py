import random


def shuffler(values):
    for i in range(len(values)):
        random_index = random.randint(0, len(values)-1)
        values[random_index], values[i] = values[i], values[random_index]
    return values


N = int(input("Введите N: "))
print(f'N={N}')
values = [x for x in range(-N, N + 1)]
print(f'original values={values}')
print(f'shuffled values={shuffler(values)}')
