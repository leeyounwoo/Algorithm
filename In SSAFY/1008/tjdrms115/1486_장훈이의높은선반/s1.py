import sys
sys.stdin = open('input.txt')


def exhaustive_search(N, B, heights, i, tot):
    global result

    if i == N:
        if tot >= B:
            if result > tot - B:
                result = tot - B
        return
    elif tot >= B:
        if result > tot - B:
            result = tot - B
        return

    exhaustive_search(N, B, heights, i + 1, tot + heights[i])
    exhaustive_search(N, B, heights, i + 1, tot)


T = int(input())

answer = []
for tc in range(1, T + 1):
    N, B = map(int, input().split())

    heights = list(map(int, input().split()))

    picked = [0]

    result = sum(heights)

    exhaustive_search(N, B, heights, 0, 0)

    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')