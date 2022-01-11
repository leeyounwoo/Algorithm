import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    case = list(map(int, input().split()))

    now = case[0]
    able_stop = []
    cnt = 0
    while True:
        if now == 1:
            cnt -= 1
            break
        for j in range(now-1, 0, -1):
            if now - j <= case[j]:
                able_stop.append(j)
        now = able_stop[-1]
        cnt += 1
    print('#{} {}'.format(tc+1, cnt))