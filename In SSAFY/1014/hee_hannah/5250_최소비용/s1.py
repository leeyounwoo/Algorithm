import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    s = li[0][0]
    e = li[n-1][n-1]