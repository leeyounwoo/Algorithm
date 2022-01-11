import sys
sys.stdin = open('input.txt')

def fly(area, N, target):
    max_total = 0
    for i in range(N - target + 1):
        for j in range(N - target + 1):
            total = 0
            for k in range(i, i + target):
                for l in range(j, j + target):
                    total += area[k][l]

            if total > max_total:
                max_total = total
    return max_total

T = int(input())

for tc in range(T):
    N, target = map(int, input().split())
    area = [list(map(int, input().split())) for i in range(N)]

    print('#{0} {1}'.format(tc+1, fly(area, N, target)))
