import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):
    munjatic = []
    result = []
    count = 0
    cross, find = list(map(int, input().split()))
    for push in range(cross):
        munja = list(map(str, input()))
        munjatic.append(munja)
        # 가로
    for y in range(cross):
        for x in range(cross):
            if x+find-1  cross:
                pass
            if munjatic[y][x] == munjatic[y][x+find-1]:
                count += 1
                result.append(munjatic[y][x])
                if count == (find // 2):
                    print(result)
            else:
                count = 0
                result = []
        # 새로
    for x in range(cross):
        for y in range(cross):
            if y <= cross-1:
                pass
            if munjatic[y][x] == munjatic[cross-1-y][x]:
                count += 1
                result.append(munjatic[y][x])

                if count == (find // 2):
                    print(result)
            else:
                count = 0
                result = []

    # for sero in range(y):
    #     munja = list(map(str, input()))
    #     munjatic.append(munja)
    #     for garo in range(x):
    #         if munjatic[sero][garo] == munjatic[sero][len(garo)-garo]:
    #             garo += 1
    #             count += 1
    #             if count >= len(x / 2):
    # print(munjatic)


# 교수님 코드
# import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(input()) for _ in range(N)]
#
#     행방향
# #     for i in range(N):
# #         for j in range(N - M+1):
# #             flag = 1
# #             for k in range(M // 2):
# #                 if arr[i][j + k] != arr[i][j + M - 1 - k]:
# #                     flag = 0
# #                     break
# #                 if flag == 1:
# #                     for k in range(M):
# #                         print('{}'.format(arr[i][j + k], end =''))
# #                     print()
#     열방향
#     for i in range(N):
#         for j in range(N - M+1):
#             flag = 1
#             for k in range(M // 2):
#                 if arr[j + k][i] != arr[j + M - 1 - k][i]:
#                     flag = 0
#                     break
#                 if flag == 1:
#                     for k in range(M):
#                         print('{}'.format(arr[j + k][i], end =''))
#                     print()