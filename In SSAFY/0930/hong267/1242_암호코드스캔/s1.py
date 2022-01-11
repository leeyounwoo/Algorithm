import sys

sys.stdin = open('input.txt')

def change_binary(num):
    temp = ''
    if num == 1:
        temp = '1000'
    elif num == 0:
        temp = '0000'
    else:
        while True:
            temp += str(num % 2)
            num //= 2
            if num == 1:
                temp += str(num)
                break

        while len(temp) < 4:
            temp += '0'

    return temp[::-1]

def decode(c, n):
    global code_list
    temp_code_list = []
    for i in code_list:
        temp = ''
        for j in i:
            temp += j*n
        temp_code_list.append(temp)

    k = 0
    flag = False
    for i in range(len(c)):
        for j in range(len(temp_code_list)):
            if c[::-1][i:i+7*n][::-1] == temp_code_list[j]:
                k = i
                flag = True
                break
        if flag:
            break

    result = []
    while k < len(c):
        for j in range(len(temp_code_list)):
            if c[::-1][k:k+7*n][::-1] == temp_code_list[j]:
                result.append(j)
                break
        k += 7*n

    return result



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    codes = [[i for i in input()] for _ in range(N)]
    x_dict = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    code_list = ['0001101', '0011001', '0010011', '0111101', '0100011',
                 '0110001', '0101111', '0111011', '0110111', '0001011']

    codes_out = []
    for i in codes:
        temp = ''
        for j in i:
            if j != '0':
                temp += j
        if temp:
            codes_out.append(temp)

    codes_out = list(set(codes_out))
    binary_codes = []
    for i in codes_out:
        temp = ''
        for j in i:
            if j.isdigit():
                temp += change_binary(int(j))
            else:
                temp += change_binary(int(x_dict[j]))
        binary_codes.append(temp)

    first_result = []
    for i in binary_codes:
        m = len(i) // 56
        first_result.append(decode(i, m))

    print(first_result)
