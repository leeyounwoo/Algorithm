import sys
sys.stdin = open('input.txt')


def monotone_increasing(num):
    num_list = list(map(int, str(num)))
    for i in range(len(num_list)-1):
        if num_list[i] > num_list[i+1]:
            return False
    return True


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = -1
    for i in range(N):
        for j in range(i+1, N):
            tmp = arr[i] * arr[j]
            if result < tmp and monotone_increasing(tmp):
                result = tmp

    print('#{} {}'.format(tc, result))