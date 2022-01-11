def dec_to_bin(num):
    if not num:
        return [0]
    result = []
    while num:
        num, r = divmod(num, 2)
        result.append(r)
    result.reverse()
    return result


num = 0
print(bin(num))
print(dec_to_bin(num))