import sys

sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T + 1):

    num = float(input())

    temp = 1
    result = ''

    for _ in range(12):
        num *= 2
        if num > 1:
            result += '1'
            num -= 1
        elif num < 1:
            result += '0'
        else:
            result += '1'
            break
    else:
        result = 'overflow'

    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')
