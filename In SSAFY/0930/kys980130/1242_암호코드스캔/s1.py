import sys
sys.stdin = open('input.txt')
key = {'211': 0, '221': 1, '122': 2, '411': 3, '132': 4, '231':5,
       '114': 6, '312': 7, '213': 8, '112': 9}
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num = [input() for _ in range(N)]
    result = []
    total = 0
    ans = 0
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if n

    for m in range(1, 8):
        if m % 2:
            total += 3 * result[m-1]
        else:
            total += result[m-1]
    total += result[7]
    if total % 10 == 0:
        for n in range(len(result)):
            ans += result[n]
    else:
        ans = 0
    print('#{} {}'.format(tc, ans))