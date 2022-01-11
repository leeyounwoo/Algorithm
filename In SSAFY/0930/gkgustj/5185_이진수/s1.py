import sys
sys.stdin = open('input.txt')

def num_to_bin(number):
    result = ''

    while number:
        result += str(number%2)
        number //= 2

    while len(result) < 4:
        result += '0'

    return result[::-1]


def str_to_bin(string):
    change = {
        'A' : 10, 'B' : 11, 'C' : 12,
        'D' : 13, 'E' : 14, 'F' : 15
    }

    number = change[string]

    return num_to_bin(number)

T = int(input())

for t in range(1, T+1):
    N, hex_num = input().split()

    answer = ''
    for x in hex_num:
        if x.isnumeric():
            answer += num_to_bin(int(x))
        else:
            answer += str_to_bin(x)
    
    print('#{} {}'.format(t, answer))