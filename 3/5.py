k = 8


def fib(n):
    if n == -2:
        return -1
    if n == -1:
        return 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 0:
        return fib(n-1) + fib(n-2)
    elif n < 0:
        return fib(n+2) - fib(n+1)


result_list = [fib(x) for x in range(-k, k + 1)]
print(f'для k = {k} список будет выглядеть так: {result_list}')
