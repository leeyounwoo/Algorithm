import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T+1):
    N = int(input())
    words = list(input().split())

    m = (N-1) // 2

    result = []
    for i in range((N-m-1)):
        result.append(words[i])
        result.append(words[m+1+i])
    if N % 2:
        result.append(words[m])
    result = ' '.join(map(str, result))
    answer.append(result)

for tc in range(1, T+1):
    print('#{} {}'.format(tc, answer[tc-1]))
