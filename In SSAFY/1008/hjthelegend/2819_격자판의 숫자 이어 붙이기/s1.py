dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def longlong(numbers, x, y):
    if len(numbers) >= 7:
        result.add(numbers)
        return

    for dx, dy in dxy:
        nx = dx + x
        ny = dy + y
        if -1 < nx < 4 and -1 < ny < 4:
            longlong(numbers + arr[nx][ny], nx, ny)

    return

t = int(input())

for tc in range(1, t+1):
    arr = [list(input().split()) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            longlong('', i, j)
    
    print('#{} {}'.format(tc, len(result)))