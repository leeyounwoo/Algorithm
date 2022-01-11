import sys
sys.stdin = open('input.txt')

# n개의 벽돌을 떨어트려 최대한 많은 벽돌 제거
# 남은 벽돌의 개수 구하기
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

t = int(input())
for tc in range(1, t+1):
    n, w, h = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(h)]
