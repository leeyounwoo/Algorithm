import sys

sys.stdin = open('input.txt')


def hex_to_bin(c: str):
    if c.isdigit():
        num = ord(c) - ord('0')
    else:
        num = ord(c) - ord('A') + 10

    result = ''
    for _ in range(4):
        result = str(num % 2) + result
        num //= 2
    return result


T = int(input())

answer = []
for tc in range(1, T + 1):

    N, hex = input().split()
    N = int(N)

    result = ''
    for c in hex:
        result += hex_to_bin(c)

    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')
