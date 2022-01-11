import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    len_num = int(input())
    case = list(input().split())

    mid = 0
    if len_num % 2:
        mid = len_num//2 + 1
    else:
        mid = len_num//2

    i = 0
    k = 0
    j = mid
    result = [''] * len_num
    while k != len_num:
        if k % 2:
            result[k] = case[j]
            j += 1
        else:
            result[k] = case[i]
            i += 1
        k += 1

    print('#{} {}'.format(tc+1, ' '.join(result)))