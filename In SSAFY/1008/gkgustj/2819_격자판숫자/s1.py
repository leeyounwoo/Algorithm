import sys
sys.stdin = open('input.txt')

def dfs(x, y, path):
    global numbers

    if len(path) == 7:
        number = ''
        for i, j in path:
            number += arr[i][j]
            
        numbers.append(number)
        return

    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dx, dy in dxy:
        nx, ny = x+dx, y+dy

        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, path+[(nx, ny)])


T = int(input())

for t in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    numbers = []

    for i in range(4):
        for j in range(4):
            dfs(i, j, [(i, j)])
    
    print('#{} {}'.format(t, len(set(numbers))))