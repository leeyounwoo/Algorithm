import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T + 1):

    N = int(input())
    request = []
    for _ in range(N):
        s, e = map(int, input().split())
        request.append([s, e])

    request.sort(key=lambda x: x[1])
    idx = 0
    start = -1
    while idx < len(request):
        if start <= request[idx][0]:
            start = request[idx][1]
            idx += 1
        else:
            request.pop(idx)

    result = len(request)
    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')
