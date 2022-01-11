import sys
sys.stdin = open('input.txt')


def binary(number):
    number = int(number)
    result = ''
    while number:
        result += str(number % 2)
        number = number // 2
    if len(result) < 4:
        for i in range(4-len(result)):
            result += '0'
    return result[::-1]


def change(j):
    result = ''
    num_list = {'A': 10,
                'B': 11,
                'C': 12,
                'D': 13,
                'E': 14,
                'F': 15}
    for arr in j:
        if arr.isdigit():
            result += binary(arr)
        else:
            arr = num_list[arr]
            result += binary(arr)
    return result


T = int(input())
for tc in range(T):
    num, case = map(str, input().split())
    a = change(case)
    print('#{} {}'.format(tc+1, a))
