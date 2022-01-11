import sys
sys.stdin = open('input.txt')
num = int(input())
maze = [list(map(int, input().split())) for _ in range(num)]
visited = [[False for _ in range(num)] for _ in range(num)]

dir_x = [0, 1, 0, -1]
dir_y = [1, 0, -1, 0]

stack = []
stack.append([0, 0])

while stack:
    curr_x, curr_y = stack[-1]
    visited[curr_x][curr_y] = True
    if [curr_x, curr_y] == [num-1, num-1]:
        break
    for i in range(4):
        next_x, next_y = curr_x + dir_x[i], curr_y + dir_y[i]
        if 0 <= next_x < num and 0 <= next_y < num and maze[next_x][next_y] == 0 and not visited[next_x][next_y]:
            stack.append([next_x, next_y])
            break
    else:
        stack.pop()
# stack.reverse()
# while stack:
#     print(stack.pop())
print(stack)