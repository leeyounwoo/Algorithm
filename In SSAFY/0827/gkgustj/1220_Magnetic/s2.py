import sys
sys.stdin = open('input.txt')

def magnetic(lst):
    global cnt
    # 1 : N극(->) / 2: S극(<-)
    # N극 테이블 S극

    stack = []
    i = 0

    while i < 100:
        if lst[i] == 1:
            stack.append(lst[i])

        elif lst[i] == 2 and stack:
            cnt += 1
            stack = []

        i += 1


for t in range(1, 11):
    N = int(input())

    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))

    # 전치행렬 : N극 테이블 S극
    for i in range(100):
        for j in range(100):
            if i > j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    cnt = 0
    for row in arr:
        magnetic(row)

    print('#{} {}'.format(t, cnt))