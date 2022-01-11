import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]
    time.sort(key=lambda x: (x[1], x[0]))

    start1, end1 = time.pop(0)
    cnt = 1
    while time:
        start2, end2 = time.pop(0)
        if end1 <= start2:
            start1, end1 = start2, end2
            cnt += 1

    print("#{} {}".format(tc, cnt))
