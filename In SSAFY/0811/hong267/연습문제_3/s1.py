puzzle = [[0] * 5 for _ in range(5)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

n = 1
d = 0 # 0 = 오른쪽, 1 = 아래, 2 = 왼쪽, 3 = 위
i, j = 0, -1
while n <= 25:
    ni, nj = i + di[d], j + dj[d]
    if ni < len(puzzle) and nj < len(puzzle) and puzzle[ni][nj] == 0:
        puzzle[ni][nj] = n
        n += 1
        i, j = ni, nj
    else:
        d = (d + 1) % 4

print(puzzle)
