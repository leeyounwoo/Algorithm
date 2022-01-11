import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    result = 0
    for i in range(N):
        for j in range(i+1, N):
            mult = numbers[i] * numbers[j]
            digits = str(mult)
            for k in range(len(digits)-1):
                if int(digits[k]) > int(digits[k+1]):
                    break
            else:
                if result < mult:
                    result = mult

    if result == 0:
        result = -1
    answer.append(result)

for tc in range(1, T+1):
    print('#{} {}'.format(tc, answer[tc-1]))
