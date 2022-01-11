import sys
sys.stdin = open('input.txt')


def minsum(idx, flag):
    global ans
    # 모든 자리수를 확인했을 때
    if idx == N:
        # 더 작다면 ans를 갱신
        if flag < ans:
            ans = flag

    # 유망하지 않은 경우엔 return
    if flag >= ans:
        return

    for i in range(N):
        if not check[i]:
            check[i] = True
            minsum(idx+1, flag+numbers[idx][i])
            check[i] = False


for T in range(1, 1+int(input())):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    check = [False] * N
    ans = 10 * N
    minsum(0, 0)
    print('#{} {}'.format(T, ans))
