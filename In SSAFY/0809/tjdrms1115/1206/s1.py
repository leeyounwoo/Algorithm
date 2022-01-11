import sys
sys.stdin = open('input.txt')

T = 10

answer = []
for tc in range(1, T + 1):

    N = int(input())
    buildings = list(map(int, input().split()))

    result = 0
    for i in range(0, N):
        a = 0
        if i-2 >= 0:
            a = buildings[i-2]
        b = 0
        if i-1 >= 0:
            b = buildings[i-1]
        c = 0
        if i+1 < N:
            c = buildings[i+1]
        d = 0
        if i+2 < N:
            d = buildings[i+2]
        max_building = max(a, b, c, d)
        result += max(0, buildings[i]-max_building)

    answer.append(result)

for tc in range(1, T+1):
    print(f'#{tc} {answer[tc-1]}')