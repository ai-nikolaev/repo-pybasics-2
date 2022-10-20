all_values = [x for x in range(1, 11)]
values = all_values[::-2]
values.reverse()
print(
    f'{all_values} -> на нечётных позициях элементы {values}, ответ: {sum(values)}')
