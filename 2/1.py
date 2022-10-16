from curses.ascii import isdigit


str_value = input("Введите вещественное число: ")
sum = 0
for v in str_value:
    if v.isdigit():
        sum += int(v)
    elif v == ".":
        continue
    else:
        print(f"Ошибка! Неверный символ '{v}'")
        exit(1)
print(f'Сумма цифр вещественного числа \'{str_value}\' равна \'{sum}\'')
