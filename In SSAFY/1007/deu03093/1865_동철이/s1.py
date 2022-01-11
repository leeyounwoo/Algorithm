import sys
sys.stdin = open('input.txt')


def max_possibe(idx, possible):
    global ans
    if idx == N:
        if possible > ans:
            ans = possible

    if possible <= ans:
        return

    for i in range(N):
        if not check[i]:
            check[i] = 1
            max_possibe(idx+1, possible * array[idx][i]/100)
            check[i] = 0


for T in range(1, 1+int(input())):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N
    ans = 0
    max_possibe(0, 1)
    ans *= 100
    print('#{} {:.6f}'.format(T, ans))
