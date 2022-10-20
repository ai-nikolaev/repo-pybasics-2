input_items = [2, 3, 4, 5, 6]
len_items = len(input_items)
result_items = []
for i in range(0, len_items // 2):
    result_items.append(input_items[i] * input_items[-1 - i])
if len_items % 2 != 0:
    i = (len_items // 2)
    result_items.append(input_items[i] * input_items[i])
print(f'{input_items} => {result_items}')
