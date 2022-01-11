def dec_to_base(num, base):
    result = []
    while num:
        # num, remainder = divmod(num, base)
        # result.append(remainder)
        # if num < base:
        #     result.append(num)
        #     break
        result.append(num % base)
        num //= base
    return ''.join(map(str,result[::-1]))
num = 19
print(int(hex(num),16))
print(dec_to_base(num,2))