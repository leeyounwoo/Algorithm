import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    char_dict = {}

    for i in str1:
        char_dict[i] = 0

    for i in str2:
        if i in str1:
            char_dict[i] += 1

    result = 0
    for value in char_dict.values():
        if result < value:
            result = value

    print('#{} {}'.format(tc, result))