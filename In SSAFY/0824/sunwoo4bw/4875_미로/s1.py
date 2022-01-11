import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T +1):
    N = int(input())
    maze = [int(input()) for _ in range(N)]
    stack = []
    x, y = 0, 0

    for i in range(N):
        # 2 위치
        if 2 in maze[i]:
            x = maze[i].index(2)
            y = i
    # 내 현 위치 알려줘
    stack.
    # 스택이 빌 때까지 계속 반복
    while stack:
