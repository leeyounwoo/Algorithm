import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())

    di = [0, 1, 0, -1]               # 우 하 좌 상 순으로 턴
    dj = [1, 0, -1, 0]

    snail = [[1] * N for _ in range(N)]     # N개 만큼 배열 생성

    cnt = 1


    print('#{0}'.format(tc+1), *snail)