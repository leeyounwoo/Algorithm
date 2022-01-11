from os import path
import sys
sys.stdin = open('input.txt')

def check_code(code):
    even = 0
    odd = 0

    for i in range(0, 7):
        if i%2:
            even += int(code[i])
        else:
            odd += int(code[i])
    
    even += int(code[-1])

    check = odd*3 + even

    if check%10:
        return 0
    else:
        total = 0
        for j in range(8):
            total += int(code[j])

        return total


def find_number(code):
    pw_to_num = {
        '0' : '0001101', '1' : '0011001', '2' : '0010011',
        '3' : '0111101', '4' : '0100011', '5' : '0110001',
        '6' : '0101111', '7' : '0111011', '8' : '0110111',
        '9' : '0001011'}

    pw_num = []
    for i in range(0, 50, 7):
        number = code[i:i+7]
        for key, value in pw_to_num.items():
            if value == number:
                pw_num.append(key)
                break
        else:
            return False
    
    return pw_num


def hex_to_bin(string):
    change = {
        '0' : '0000', '1' : '0001', '2' : '0010', '3' : '0011',
        '4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111',
        '8' : '1000', '9' : '1001', 'A' : '1010', 'B' : '1011',
        'C' : '1100', 'D' : '1101', 'E' : '1110', 'F' : '1111'
    }

    return change[string]


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    # 16진수 암호 코드 찾기
    password_lines = []
    for _ in range(N):
        hex_str = input()
        for i in range(M):
            if hex_str[i] != '0':
                password_lines.append(hex_str[i:])
                break

    # print(list(set(password_lines)))
    multi = len(bin_str)//14

    answer = 0
    for password_line in list(set(password_lines)):
        # 이진수 변환
        bin_str = ''
        for x in password_line:
            bin_str += hex_to_bin(x)

        print(bin_str)

        if len(bin_str) > 56:
            if sum(int(bin_str[56:])) == 0:
                bin_str = bin_str[:56]
        
        while len(bin_str)%56:
            bin_str += '0'
        
        print(bin_str)

        # 암호코드 숫자로 변환
        code = ''
        for i in range(0, len(bin_str)-multi+1, multi):
            code += bin_str[i]
        
        print('-')
        print(code)

        numbers = find_number(code)
        while not numbers:
            code = '0' + code[:55]
            numbers = find_number(code)

        # print(numbers)

        answer += check_code(numbers)

    print('#{} {}'.format(t, answer))