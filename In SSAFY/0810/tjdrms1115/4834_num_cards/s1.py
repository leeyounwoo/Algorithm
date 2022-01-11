import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T+1):

    N = int(input())
    card = list(map(int, input()))

    digits = [0] * 10

    for num in card:
        digits[num] += 1

    idx = 9
    for i in range(9,-1,-1):
        if digits[idx] < digits[i]:
            idx = i

    result = str(idx) + ' ' + str(digits[idx])
    answer.append(result)

for tc in range(1, T+1):
    print('#{0} {1}'.format(tc, answer[tc-1]))
