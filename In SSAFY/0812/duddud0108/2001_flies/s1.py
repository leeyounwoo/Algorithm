import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N, target_num = map(int, input().split())
    area = [list(map(int, input().split())) for i in range(N)]

    result_list = []
    for i in range(N - target_num + 1):
        for j in range(N - target_num + 1):
            result = 0
            for k in range(target_num):
                result += sum(area[i + k][j:j + target_num])
            result_list.append(result)

    print('#{0} {1}'.format(tc+1, max(result_list)))

