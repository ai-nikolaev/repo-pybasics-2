items = [1.1, 1.2, 3.1, 5, 10.01, 12.00]
result = [x for x in [round(x % 1, len(str(x).split('.')[:]))
                      for x in items] if x > 0]
print(f'{items} => {max(result) - min(result)}')
