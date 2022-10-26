import random


def random_polinom(k):
    polinom_dict = {}
    for x in reversed(range(k+1)):
        polinom_dict[x] = random.randint(1, 100)
    return polinom_dict


def polinom_to_string(p_dict):
    result = ""
    for p_key in p_dict:
        p_value = p_dict[p_key]
        if p_value != 0:
            if p_key == 0:
                result += f'{p_value}'
            elif p_key == 1:
                result += f'{p_value}*x'
            else:
                result += f'{p_value}*x^{p_key}'
            if p_key != 0:
                result += ' + '
    return result


def string_to_file(name, polinom):
    with open(f"{name}", "w") as file:
        file.write(polinom)


def read_polinom_from_file(name):
    p_dict = {}
    with open(name) as file:
        for line in file:
            for sum_parts in line.split(' + '):
                multiply_parts = sum_parts.split('*')
                if len(multiply_parts) == 2:
                    sub_parts = multiply_parts[1].split('^')
                    if len(sub_parts) == 2:
                        p_dict[int(sub_parts[1])] = int(multiply_parts[0])
                    else:
                        p_dict[1] = int(multiply_parts[0])
                else:
                    p_dict[0] = int(multiply_parts[0])
    return p_dict


def sum_polinoms(p_dict_1, p_dict_2):
    result = {}
    for key in p_dict_1:
        result[key] = p_dict_1[key] + p_dict_2[key]
    return result
