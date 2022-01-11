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


def find_number(numbers):
    pw_to_num = {
        '0' : '0001101', '1' : '0011001', '2' : '0010011',
        '3' : '0111101', '4' : '0100011', '5' : '0110001',
        '6' : '0101111', '7' : '0111011', '8' : '0110111',
        '9' : '0001011'}

    pw_num = []
    for i in range(0, 50, 7):
        number = numbers[i:i+7]
        for key, value in pw_to_num.items():
            if value == number:
                pw_num.append(key)
                break
        else:
            return False
    
    return pw_num


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    password_line = ''
    for _ in range(N):
        temp = input()
        if int(temp) > 0:
            if not password_line:
                password_line = temp
    
    for i in range(len(password_line)):
        if password_line[i] == '1':
            password = password_line[i:i+56]
            break
    
    code = find_number(password)

    while not code:
        code = find_number(password)
        password = '0' + password[:55]

    answer = check_code(code)

    print('#{} {}'.format(t, answer))