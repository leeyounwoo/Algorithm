import sys
sys.stdin = open('input.txt')

TC = int(input())
tele = {
    'A' : 1,
    'B' : 2,
    'C' : 3
}

for tc in range(TC):
    n = int(input())
    info = [list(input()) for _ in range(n)]
    base_station = []
    for i in range(n):
        for j in range(n):
            if info[i][j] in tele:
                base_station.append([i, j])

    for base in base_station: 
        k = tele[info[base[0]][base[1]]]
        i = 1
        while i <= k:
            # 상
            if 0 <= base[0] - i and info[base[0] - i][base[1]] == 'H':
                info[base[0] - i][base[1]] = 'X'
            # 우
            if base[1] + i < n and info[base[0]][base[1] + i] == 'H':
                info[base[0]][base[1] + i] = 'X'
            # 하
            if base[0] + i < n and info[base[0] + i][base[1]] == 'H':
                info[base[0] + i][base[1]] = 'X'
            # 좌
            if 0 <= base[1] - i and info[base[0]][base[1] - i] == 'H':
                info[base[0]][base[1] - i] = 'X'
            i += 1

    cnt = 0
    for i in range(n):
        for j in range(n):
            if info[i][j] == 'H':
                cnt += 1

    print('#{} {}'.format(tc+1, cnt))
