i = int(input("Введите номер четверти плоскости: "))
if i == 1:
    for x in list(range(1, 10, 1)):
        for y in list(range(1, 10, 1)):
            print("({},{})".format(x, y))
elif i == 2:
    for x in list(range(-1, -10, -1)):
        for y in list(range(1, 10, 1)):
            print("({},{})".format(x, y))
elif i == 3:
    for x in list(range(-1, -10, -1)):
        for y in list(range(-1, -10, -1)):
            print("({},{})".format(x, y))
elif i == 4:
    for x in list(range(1, 10, 1)):
        for y in list(range(-1, -10, -1)):
            print("({},{})".format(x, y))