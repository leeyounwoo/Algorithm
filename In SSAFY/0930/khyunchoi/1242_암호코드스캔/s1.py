import sys
sys.stdin = open('input2.txt')


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
    N, M = map(int, input().split()) # N: 세로 M: 가로
    barcode = [input() for _ in range(N)]

    hex_passwords_tmp = [] # 16진법 수가 들어있는 라인 전체
    for i in range(N):
        for j in range(M-1, -1, -1):
            if barcode[i][j] != '0':
                if barcode[i] not in hex_passwords_tmp:
                    hex_passwords_tmp.append(barcode[i])
                break

    hex_passwords = []
    for chars in hex_passwords_tmp:
        pass



    '''
    bin_passwords_tmp = [] # 2진법 수가 들어있는 라인 전체

    for hex_password in hex_passwords:
        tmp = ''
        for char in hex_password:
            tmp += dec_hex_to_bin(char)

        bin_passwords_tmp.append(tmp)

    bin_passwords = [] # 가공된 2진법 수
    for numbers in bin_passwords_tmp:
        for i in range(len(numbers)-1, -1, -1):
            if numbers[i] == 1:
                pass
    '''
