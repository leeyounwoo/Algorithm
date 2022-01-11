import sys
sys.stdin = open('input.txt')
di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dessert = [0 for _ in range(101)]
