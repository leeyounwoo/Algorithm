import sys
sys.stdin = open('input.txt')
def cal(num):
    global cnt, M
    if num == N:
        return cnt
    while M > 0:
        if type(M / 2) == int and M / 2 > -10:
            M = M / 2
            cnt += 1
        elif M + 1 == N:
            M = M + 1
            cnt += 1
        elif M - 1 == N:
            M = M - 1
            cnt += 1
        elif M + 10 == N:
            M = M + 10
            cnt += 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cnt = 0
    print(cal(M))