import sys
sys.stdin = open('input.txt')

dx = [0, 1]
dy = [1, 0]

def find(n):
    start = li[0][0]
    total = 0
    visited = [[0]*n for _ in range(n)]




t = int(input())
for tc in range(1, t+1):
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]

    start = li[0][0]

