import sys
sys.stdin = open('input.txt')

def check(result):
    result = str(result)
    for i in range(len(result) - 1):
        if result[i] > result[i + 1]:
            return False
    return True

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    number = list(map(int, input().split()))

    answer = []
    for i in range(n-1):
        for j in range(i+1, n):
            result = number[i] * number[j]
            if check(result):
                answer.append(result)

    if answer:
        answer = max(answer)
    else:
        answer = -1

    print('#{} {}'.format(tc, answer))