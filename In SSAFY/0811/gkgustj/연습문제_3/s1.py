arr = [[9, 20, 2, 18, 11],
       [19, 1, 25, 3, 21],
       [8, 24, 10, 17, 7],
       [15, 4, 16, 5, 6],
       [12, 13, 22, 23, 14]]

arr_1 = []

for row in arr:
    for num in row:
        arr_1.append(num)

result = [[0]*5 for _ in range(5)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x = 0
y = 0
way = 0

for n in range(1, 26):
    result[x][y] = n
    x_ = x + dx[way]
    y_ = y + dy[way]

    if x_ not in range(5) or y_ not in range(5) or result[x_][y_] != 0:
        way = (way + 1) % 4

    x += dx[way]
    y += dy[way]

for row in result:
    print(*row)