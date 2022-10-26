
k = int(input("Введите целое число: "))


def simple_numbers(n):
    r = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            r.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        r.append(n)
    return r


print(f'simple_number({k}) => {simple_numbers(k)};')
