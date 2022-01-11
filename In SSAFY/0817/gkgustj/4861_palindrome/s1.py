import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    arr = []
    for _ in range(N):
        arr.append(input())

    result = ''
    # 가로 회문 찾기
    for i in range(N):
        for j in range(N-M+1):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                result = arr[i][j:j+M]

    # 세로 회문 찾기
    for j in range(N):
        if result:
            break

        for i in range(N-M+1):
            temp = ''

            for k in range(i, i+M):
                temp += arr[k][j]

            if temp == temp[::-1]:
                result = temp
                break

    print('#{} {}'.format(t, result))
