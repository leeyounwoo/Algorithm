import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T + 1):

    N, M = map(int, input().split())

    code = []
    for _ in range(N):
        code.append(list(map(int, input())))

    realcode = []
    for i in range(N):
        j = M - 1
        check = 0
        while j >= 55:
            if code[i][j] == 1:
                check = 1
                break
            j -= 1
        if check:
            realcode = code[i][j - 55:j + 1]
            break

    segments = []
    for i in range(8):
        segments.append(realcode[i * 7:i * 7 + 7])

    digit = []
    for segment in segments:
        if segment[1:6] == [0, 0, 1, 1, 0]:
            digit.append(0)
        elif segment[1:6] == [0, 1, 1, 0, 0]:
            digit.append(1)
        elif segment[1:6] == [0, 1, 0, 0, 1]:
            digit.append(2)
        elif segment[1:6] == [1, 1, 1, 1, 0]:
            digit.append(3)
        elif segment[1:6] == [1, 0, 0, 0, 1]:
            digit.append(4)
        elif segment[1:6] == [1, 1, 0, 0, 0]:
            digit.append(5)
        elif segment[1:6] == [1, 0, 1, 1, 1]:
            digit.append(6)
        elif segment[1:6] == [1, 1, 1, 0, 1]:
            digit.append(7)
        elif segment[1:6] == [1, 1, 0, 1, 1]:
            digit.append(8)
        elif segment[1:6] == [0, 0, 1, 0, 1]:
            digit.append(9)

    check = ((sum(digit[::2]) * 3) + sum(digit[1::2]))

    result = 0
    if check % 10 == 0:
        result = sum(digit)

    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')