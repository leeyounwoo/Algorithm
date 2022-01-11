import sys
sys.stdin = open('input.txt')

def hap(x, path):

    if x == N:
        print(path)
        return
    else:
        for i in range(N):
            if check[i] == 0:
                check[i]
                hap(x + 1, i, path + [[x, i]])
                # check[i] = 0

T = int(input())
for tc in range(1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N

    hap(0, [[0, 0]])

# def sol(N, k, s):
#     global res
#     if N == k:
#         if res > s:
#             res = s
#
#     if res < s:
#         return
#
#     else:
#         for i in range(N):
#             if visited[i] == 0:
#                 visited[i] = 1
#                 sol(N, k + 1, s + data[k][i])
#                 visited[i] = 0
#
#
# TC = int(input())
# for tc in range(1, TC + 1):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     visited = [0] * N
#
#     k = 0
#     res = 10 * N # 최대값
#
#     sol(N, 0, 0)
#     print("#%d %d" % (tc, res))