import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    count = 1
    while True:
        num_pop = num_list.pop(0)
        num_list.append(num_pop)
        count += 1

        if count > M:
            break

    print('#{} {}'.format(tc, num_list[0]))
