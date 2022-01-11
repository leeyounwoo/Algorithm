import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    barcode = [list(map(int, input())) for _ in range(N)]

    passwords = []
    for i in range(N):
        for j in range(M-1, -1, -1):
            if barcode[i][j] == 1:
                passwords = barcode[i][j-55:j+1]
                break

    decode_password = ''
    for i in range(0, len(passwords), 7):
        password = ''.join(map(str, passwords[i:i+7]))
        if password == '0001101':
            decode_password += '0'
        elif password == '0011001':
            decode_password += '1'
        elif password == '0010011':
            decode_password += '2'
        elif password == '0111101':
            decode_password += '3'
        elif password == '0100011':
            decode_password += '4'
        elif password == '0110001':
            decode_password += '5'
        elif password == '0101111':
            decode_password += '6'
        elif password == '0111011':
            decode_password += '7'
        elif password == '0110111':
            decode_password += '8'
        elif password == '0001011':
            decode_password += '9'

    total = 0
    for i in range(len(decode_password)):
        num = int(decode_password[i])
        if i % 2:
            total += num
        else:
            total += num * 3

    result = 0
    if total % 10 == 0:
        result = sum(list(map(int, decode_password)))

    print('#{} {}'.format(tc, result))
