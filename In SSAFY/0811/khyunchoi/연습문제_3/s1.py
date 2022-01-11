arr = [
    [9, 20, 2, 18, 11],
    [19, 1, 25, 3, 21],
    [8, 24, 10, 17, 7],
    [15, 6, 16, 5, 6],
    [12, 13, 22, 23, 14],
]

tmp_arr = []
for i in range(len(arr)):
    for j in range(len(arr[0])):
        tmp_arr.append(arr[i][j])
tmp_arr.sort()

new_arr = [[0]*5 for _ in range(5)]

cnt = 0
i, j = 0, -1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
k = 0
while cnt < 25:
    x, y = i+dx[k], j+dy[k]
    if x < 5 and y < 5 and new_arr[x][y] == 0:
        new_arr[x][y] = tmp_arr[cnt]
        i, j = x, y
        cnt += 1
    else:
        k = (k+1) % 4

for i in new_arr:
    print(*i)