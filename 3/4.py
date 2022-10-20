result = ""


def decToBin(n):
    global result
    if (n > 1):
        decToBin(n//2)
    result += f'{n % 2}'


value = 45
decToBin(value)
print(f"{value} -> '{result}'")
result = ""
value = 3
decToBin(value)
print(f"{value} -> '{result}'")
result = ""
value = 2
decToBin(value)
print(f"{value} -> '{result}'")
