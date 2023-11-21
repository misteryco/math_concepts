a = 'AABCCCDEEEE'


def encode(a):
    res = dict()
    i = 0

    while True:
        current_letter = a[i]
        current_letter_count = 1
        while True:
            next_index = i + 1
            if next_index > len(a) - 1:
                i = next_index
                res[current_letter] = current_letter_count
                break
            if a[next_index] == current_letter:
                current_letter_count += 1
                i = next_index
            else:
                res[current_letter] = current_letter_count
                i = next_index
                break
        if i > len(a) - 1:
            break
    encoded_string = ''
    for k, v in res.items():
        if v > 1:
            encoded_string += f"{k}{v}"
        else:
            encoded_string += k
    return encoded_string


def decode(a_res):
    a = a_res
    res = ''
    i = 0

    while True:
        current_letter = a[i]
        num = ''
        while True:
            next_index = i + 1
            if next_index > len(a) - 1:
                i = next_index
                if not num:
                    res += current_letter
                    break
                else:
                    res += current_letter * int(num)
                    break
            if a[next_index] in '123456789':
                num += a[next_index]
                i = next_index
            else:
                i = next_index
                if not num:
                    res += current_letter
                    break
                else:
                    res += current_letter * int(num)
                    break
        if i > len(a) - 1:
            break
    return res

# Test:

assert decode(encode("AABCCCDEEEE")) == "AABCCCDEEEE"
