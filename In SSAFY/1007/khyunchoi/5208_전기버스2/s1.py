import sys
sys.stdin = open('input.txt')


def move(idx, battery, cnt):
    global result
    if result <= cnt:
        return

    if idx + battery >= len(stations):
        result = min(result, cnt)
        return

    for i in range(idx+1, idx+battery+1):
        if i < len(stations):
            move(i, stations[i], cnt+1)


T = int(input())
for tc in range(1, T+1):
    tmp = list(map(int, input().split()))
    N = tmp[0]
    stations = tmp[1:]

    result = 100
    move(0, stations[0], 0)

    print('#{} {}'.format(tc, result))
