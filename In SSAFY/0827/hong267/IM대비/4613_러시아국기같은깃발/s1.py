import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    string = []
    for _ in range(N):
        tmp = []
        for i in input():
            tmp.append(i)
        string.append(tmp)

    cnt = 0
    cnt += (M - string[0].count('W'))
    cnt += (M - string[-1].count('R'))
    # ~ing