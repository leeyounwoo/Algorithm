import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time = []
    checked = [0 for _ in range(25)]
    total = 0
    for _ in range(N):
        s, e = map(int, input().split())
        time.append((e-s, s, e))
    time.sort()
    for j in time:
        check = 0
        for i in range(j[1], j[2]):
            if checked[i] == 0:
                checked[i] = 1
                check += 1
            else:
                break
        if check == j[0]:
            total += 1
    print('#{} {}'.format(tc, total))

