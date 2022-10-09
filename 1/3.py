x = int(input("Введите координату x: "))
y = int(input("Введите координату y: "))
if x == 0 or y == 0:
    print("Ошибка! Координата не может быть равна [0]!")
else:
    if x > 0:
        if y > 0:
            result = 1
        elif y < 0:
            result = 4
    elif x < 0:
        if y > 0:
            result = 2
        elif y < 0:
            result = 3
    print("{}-я четверть плоскости!".format(result))