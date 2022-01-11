import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]

    time.sort(key=lambda x:x[1])

    s = 0
    e = 0
    cnt = 0

    for ns, ne in time:
        if e <= ns:
            cnt += 1
            s = ns
            e = ne
        else:
            pass
    
    print('#{} {}'.format(t, cnt))