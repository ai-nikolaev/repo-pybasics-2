import math

xa = int(input("Введите координату Xa: "))
ya = int(input("Введите координату Ya: "))
xb = int(input("Введите координату Xb: "))
yb = int(input("Введите координату Yb: "))
result = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
print("Расстояние между ({},{}) и ({},{}) равно {:.2f}!".format(xa, xb, ya, yb, result))