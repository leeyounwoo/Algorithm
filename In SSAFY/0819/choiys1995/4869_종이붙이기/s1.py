import sys
sys.stdin = open('input.txt')

T = int(input())

def stick(N):
    # dp 10, 20의 값을 구함
    if N == 10:
        return 1
    elif N == 20:
        return 3
    return stick(N - 10) + 2 * stick(N - 20)

def stick_dp(N):
    paper = [1, 3]
    n = N // 10
    for i in range(2, n):
        paper.append(paper[i - 1] + paper[i - 2] * 2)
    return paper[n - 1]

for tc in range(1, T+1):
    N = int(input())
    result = stick(N)
    result2 = stick_dp(N)
    print("#{} {}".format(tc, result2))