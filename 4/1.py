import math

MAX_ITERATIONS = 2 * 4096 * 4096


def vallis(d):
    valid_values = [10**-x for x in range(1, 11)]
    if d not in valid_values:
        raise Exception(f'Invalid argument {d}! Must be in {valid_values}')
    pi = 0
    iters = 0
    for x in enumerate(range(1, 2 * MAX_ITERATIONS, 2), 1):
        iters += 1
        if x[0] % 2 == 0:
            pi -= 4/x[1]
        else:
            pi += 4/x[1]
        if abs(math.pi - abs(pi)) < d:
            break
    return (pi, iters, math.pi - pi)


print(vallis(1e-10))
