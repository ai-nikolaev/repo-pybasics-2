input_data = "WWJJJHDDDDDPPGRRR"


def encode(data):
    result = ""
    temp = ""
    prev_symbol = ""
    for pair in enumerate(data):
        if pair[0] == 0:
            temp += pair[1]
            prev_symbol = pair[1]
            continue
        if pair[1] == prev_symbol:
            temp += pair[1]
        else:
            result += f'{len(temp)}' + temp[0]
            temp = pair[1]
        prev_symbol = pair[1]
    result += f'{len(temp)}' + temp[0]
    return result


def decode(data):
    result = ""
    for x in range(1, len(data) + 1):
        if x % 2 == 0:
            continue
        for y in range(1, int(data[x-1]) + 1):
            result += data[x]
    return result


encoded_data = encode(input_data)
decoded_data = decode(encoded_data)
print(f'{input_data} -> {encoded_data} -> {decoded_data}')
