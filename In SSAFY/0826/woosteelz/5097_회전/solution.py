import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    permt = list(map(int, input().split()))

    M %= N

    for _ in range(M):
        permt.append(permt.pop(0))

    print('#{} {}'.format(tc+1, permt[0]))