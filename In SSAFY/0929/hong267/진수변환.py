def dec_to_bin(num):
    result = []
    while True:
        num, remainder = divmod(num, 2)
        result.append(remainder)

        if num < 2:
            result.append(num)
            return result[::-1]


def dec_to_base_x(num, base):
    result = []
    while num:
        result.append(num % base)
        num = num // base

    return ''.join(map(str, result[::-1]))

num = 19
print(bin(num)) # string으로 표기 # 2진수
print(oct(num)) # 8진수
print(hex(num)) # 16진수

print(dec_to_bin(num))
print('10진법 => 2진법', dec_to_base_x(num, 2))
print('10진법 => 3진법', dec_to_base_x(num, 3))
print('10진법 => 8진법', dec_to_base_x(num, 8))
print('10진법 => 16진법', dec_to_base_x(num, 16))