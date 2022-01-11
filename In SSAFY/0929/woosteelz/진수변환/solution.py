def dec_to_base(num, base):
    res = ''
    while num:
        res = str(num % base) + res
        num //= base
    return res


print(dec_to_base(20, 5))
