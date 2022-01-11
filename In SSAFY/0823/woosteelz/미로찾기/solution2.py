import sys
sys.stdin = open('input.txt')

def dfs_recursion(x, y, path):
    maze[x][y] = 1
    dir_x = [0, 1, 0, -1]
    dir_y = [1, 0, -1, 0]
    if [x, y] == [num-1, num-1]:
        print(path)
        return
    for i in range(4):
        next_x, next_y = x + dir_x[i], y + dir_y[i]
        if 0 <= next_x < num and 0 <= next_y < num and maze[next_x][next_y] == 0:
            dfs_recursion(next_x, next_y, path + [[next_x, next_y]])


num = int(input())
maze = [list(map(int, input().split())) for _ in range(num)]
start_x, start_y = 0, 0
dfs_recursion(start_x, start_y, [])
