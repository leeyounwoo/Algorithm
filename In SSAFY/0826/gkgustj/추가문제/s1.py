import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())

    arr = []
    for _ in range(N):
        temp = []
        for s in input():
            temp.append(s)
        arr.append(temp)

    giji = {'A' : 1, 'B' : 2, 'C' : 3}

    for i in range(N):
        for j in range(N):
            if arr[i][j] in giji.keys():
                for dd in range(1, giji[arr[i][j]]+1):
                    d = [(dd, 0), (-dd,0), (0, dd), (0, -dd)]

                    for di, dj in d:
                        ni, nj = i+di, j+dj
                        if ni in range(N) and nj in range(N) and arr[ni][nj] == 'H':
                            arr[ni][nj] = 'X'

                arr[i][j] = 'X'

    total = 0
    for row in arr:
        total += row.count('H')

    print('#{} {}'.format(t, total))