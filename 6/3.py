src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [x[1] for x in enumerate(src) if src[x[0]] > src[x[0] - 1]]
print(f'src = {src}')
print(f'result = {result}')
