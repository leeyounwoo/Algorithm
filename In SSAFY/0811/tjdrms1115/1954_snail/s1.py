import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T + 1):

    n = int(input())

    # 달팽이 숫자를 저장할 배열입니다.
    arr = [[0 for _ in range(n)] for _ in range(n)]

    # while문에 들어갈 값들을 초기화합니다.
    idx = 0
    i, j = 0, 0
    # 델타입니다.
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    diridx = 0
    diri, dirj = direction[diridx]
    # 달팽이 숫자를 다 채울때 까지 반복합니다.
    while idx < n * n:
        # 달팽이 숫자를 하나씩 채웁니다.
        arr[i][j] = idx + 1
        idx += 1

        # 만약에 다음 위치가 막혔다면 방향을 바꿉니다.
        if (0 <= i + diri < n) and (0 <= j + dirj < n) and arr[i + diri][j + dirj] == 0:
            pass
        else:
            diridx = (diridx + 1) % 4

        # 다음 방향을 지시합니다.
        diri, dirj = direction[diridx]

        # 다음 위치로 인덱스를 옮깁니다.
        i = i + diri
        j = j + dirj

    result = '\n'
    for i in range(n):
        result += ' '.join(map(str, arr[i])) + '\n'
    answer.append(result)

for tc in range(1, T + 1):
    print('#{0} {1}'.format(tc, answer[tc-1]))