import sys
sys.stdin = open('input.txt')

# 오른쪽, 아래, 왼쪽, 위
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dir_stat = 0  # 초기 방향 오른쪽
x, y = 0, 0  # 나의 위치 세팅


# 반복문 돌면서...
# 내가 바로 다음으로 갈 위치
new_x = x + dx[dir_stat]
new_y = y + dy[dir_stat]
