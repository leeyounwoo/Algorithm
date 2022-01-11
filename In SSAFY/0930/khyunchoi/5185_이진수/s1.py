import sys
sys.stdin = open('input.txt')


def dec_hex_to_bin(num):
    if not num.isdigit():
        int_num = ord(num) - 55
    else:
        int_num = int(num)

    bin_num = ''
    while int_num > 0 or len(bin_num) < 4:
        bin_num = str((int_num % 2)) + bin_num
        int_num //= 2

    return bin_num


T = int(input())
for tc in range(1, T+1):
    N, hex_number = input().split()

    result = ''
    for char in hex_number:
        result += dec_hex_to_bin(char)

    print('#{} {}'.format(tc, result))
