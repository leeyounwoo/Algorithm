import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T + 1):

    N = int(input())

    divisor = [2, 3, 5, 7, 11]
    divide_count = [0] * len(divisor)

    for i in range(len(divisor)):
        cur_divisor = divisor[i]
        while not N % cur_divisor:
            N = N // cur_divisor
            divide_count[i] += 1

    result = ' '.join(map(str, divide_count))
    answer.append(result)

for tc in range(1, T+1):
    print('#{0} {1}'.format(tc, answer[tc-1]))