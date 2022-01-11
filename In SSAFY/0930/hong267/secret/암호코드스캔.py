hex_to_bin = [[0, 0, 0, 0],  # 0
              [0, 0, 0, 1],  # 1
              [0, 0, 1, 0],  # 2
              [0, 0, 1, 1],  # 3
              [0, 1, 0, 0],  # 4
              [0, 1, 0, 1],  # 5
              [0, 1, 1, 0],  # 6
              [0, 1, 1, 1],  # 7
              [1, 0, 0, 0],  # 8
              [1, 0, 0, 1],  # 9
              [1, 0, 1, 0],  # A
              [1, 0, 1, 1],  # B
              [1, 1, 0, 0],  # C
              [1, 1, 0, 1],  # D
              [1, 1, 1, 0],  # E
              [1, 1, 1, 1]]  # F

scode = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
scode[2][1][1] = 0
scode[2][2][1] = 1
scode[1][2][2] = 2
scode[4][1][1] = 3
scode[1][3][2] = 4
scode[2][3][1] = 5
scode[1][1][4] = 6
scode[3][1][2] = 7
scode[2][1][3] = 8
scode[1][1][2] = 9


def solve():
    result = 0
    for i in range(N):
        j = M * 4 - 1  # x축 좌표 == 16진법으로 바꾼 2차원 배열의 x축 길이
        while j > 0:
            # 맨 오른쪽에서부터 시작

            # 두께에 상관없이 암호코드가 시작되는 첫번째 줄만 계산
            # 즉, 다음 줄에 똑같은 암호코드가 나와도 두번째 조건 때문에 확인 X
            if arr[i][j] == 1 and arr[i - 1][j] == 0:
                code = [0 for _ in range(8)]
                for k in range(7, -1, -1):
                    # 각 자릿수 비율 계산을 위해 설정
                    # ex) 1 : 1 : 2 == 9
                    #     4 : 4 : 8 == 9 (가장 작은 값으로 나누기)
                    x = y = z = 0
                    while arr[i][j] == 1:  # 1의 개수
                        z += 1
                        j -= 1
                    while arr[i][j] == 0:  # 0의 개수
                        y += 1
                        j -= 1
                    while arr[i][j] == 1:  # 1의 개수
                        x += 1
                        j -= 1
                    while arr[i][j] == 0:  # 0의 개수
                        j -= 1

                    d = min(x, y, z)
                    x //= d
                    y //= d
                    z //= d

                    code[k] = scode[x][y][z]

                t = (code[0] + code[2] + code[4] + code[6]) * 3 + code[1] + code[3] + code[5] + code[7]
                if t % 10 == 0:
                    result += code[0] + code[2] + code[4] + code[6] + code[1] + code[3] + code[5] + code[7]
                j += 1

            # 왼쪽으로 한 칸 이동 후 다시 탐색
            j -= 1
    return result


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [[0 for _ in range(M * 4)] for _ in range(N)]
    for i in range(N):
        temp = input()
        for j in range(M):
            t = temp[j]
            if t <= '9':
                t = ord(t) - ord('0')
            else:
                t = ord(t) - ord('A') + 10
            for k in range(4):
                # 기존: 0, 1, 2, 3
                # 변경: 0 1 2 3 => 4 5 6 7 => 8 9 10 11
                # 즉...
                # 0 => 0,
                # 1 => 4,
                # 2 => 8
                arr[i][j * 4 + k] = hex_to_bin[t][k]

    ans = solve()
    print("#{} {}".format(tc + 1, ans))

