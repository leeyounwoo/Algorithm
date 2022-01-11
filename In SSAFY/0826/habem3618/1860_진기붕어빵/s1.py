import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    human = sorted(list(map(int, input().split())))
    flag = True

    for i in range(len(human)):
        fish = (human[i] // M) * K  # 사람이 올 때 붕어빵 개수

        if fish < i + 1:
            flag = False
            break

    if flag:
        print('#{} Possible'.format(tc))
    else:
        print('#{} Impossible'.format(tc))
