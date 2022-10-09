day_of_week = int(input("Пожалуйста введите день недели: "))
if day_of_week > 7:
    print("Ошибка! Значений должно быть в диапазоне [1...7].".format(day_of_week))
elif day_of_week < 1:
    print("Ошибка! Значений должно быть в диапазоне [1...7].".format(day_of_week))
elif day_of_week == 6:
    print("День недели [{}] - выходной!".format(day_of_week))
elif day_of_week == 7:
    print("День недели [{}] - выходной!".format(day_of_week))
else:
    print("День недели [{}] - будний!".format(day_of_week))