import sys
sys.stdin = open('input.txt')

def DFS(y, sum):
    global result

    if y == N:
        if result > sum:
            result = sum
        return

    if result < sum:
        return

    for x in range(N):
        if not visited[x]:
            visited[x] = True
            DFS(y+1, sum + Data[y][x])
            visited[x] = False

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Data = [list(map(int, input().split())) for _ in range(N)]
    print(Data)
    visited = [0]*N
    result = 987654321

    DFS(0, 0)
    print('#{} {}'.format(tc, result))

# def min_sum(arr, number):
#     if number != N:
#         for i in range(N):
#             if i not in used_column:
#                 for j in range(N):
#                     if j not in used_row:
#                         a = arr[i][j]
#                         used_row.append(j)
#                         used_column.append(i)
#
#     else:
#         b = min_sum(arr, number-1)
#     print(b)

#
# T = int(input())
# for tc in range(1):
#     N = int(input())
#     case = [list(map(int, input().split())) for _ in range(N)]
#     print(case)
#     used_column = []
#     total = 0
#     flag = 0
#     for i in range(N):
#         for j in range(N):
#             total += case[i][j]
#             flag = 1
#
