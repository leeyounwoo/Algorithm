import sys
sys.stdin = open('input.txt')


def minsum(idx, flag):
    global ans
    if idx == n:
        if flag < ans:
            ans = flag

    if flag >= ans:
        return

    for i in range(n):
        if not check[i]:
            check[i] = True
            minsum(idx+1, flag + arrays[idx][i])
            check[i] = False


for T in range(1, 1+int(input())):
    n = int(input())
    arrays = [list(map(int, input().split())) for _ in range(n)]
    check = [0] * n
    ans = 100 * n
    minsum(0, 0)
    print('#{} {}'.format(T, ans))