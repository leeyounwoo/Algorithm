import sys


def input():
    return sys.stdin.readline().rstrip()

sys.stdin = open('input.txt')
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
# print(graph)
ans = 0
for i in range(n):
    for j in range(m):
        temp_1_1 = 0
        if j <= m-4:
            temp_1_1 = graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i][j+3]
        temp_1_2 = 0
        if i <= n-4:
            temp_1_2 = graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+3][j]
        temp_1 = max(temp_1_1, temp_1_2)

        temp_2 = 0
        if i <= n-2 and j <= m-2:
            temp_2 = graph[i][j] + graph[i + 1][j] + graph[i][j+1] + graph[i+1][j+1]

        temp_3_1 = 0
        if i <= n-3 and j <= m-2:
            temp_3_1 = graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+2][j+1]

        temp_3_2 = 0
        if i <= n - 2 and j <= m - 3:
            temp_3_2 = graph[i+1][j] + graph[i][j] + graph[i][j+1] + graph[i][j + 2]

        temp_3_3 = 0
        if i <= n - 3 and j <= m - 2:
            temp_3_3 = graph[i][j] + graph[i][j+1] + graph[i+1][j+1] + graph[i + 2][j + 1]

        temp_3_4 = 0
        if i <= n - 2 and j <= m - 3:
            temp_3_4 = graph[i+1][j] + graph[i+1][j+1] + graph[i+1][j+2] + graph[i][j + 2]

        temp_3_5 = 0
        if i <= n - 3 and j <= m - 2:
            temp_3_5 = graph[i+2][j] + graph[i+2][j+1] + graph[i+1][j+1] + graph[i][j+1]

        temp_3_6 = 0
        if i <= n - 2 and j <= m - 3:
            temp_3_6 = graph[i][j] + graph[i + 1][j] + graph[i + 1][j+1] + graph[i + 1][j + 2]

        temp_3_7 = 0
        if i <= n - 3 and j <= m - 2:
            temp_3_7 = graph[i+2][j] + graph[i+1][j] + graph[i][j] + graph[i][j+1]

        temp_3_8 = 0
        if i <= n - 2 and j <= m - 3:
            temp_3_8 = graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i+1][j + 2]

        temp_3 = max(temp_3_1, temp_3_2, temp_3_3, temp_3_4, temp_3_5, temp_3_6, temp_3_7, temp_3_8)

        temp_4_1 = 0
        if i <= n-3 and j <= m-2:
            temp_4_1 = graph[i][j] + graph[i+1][j] + graph[i+1][j+1] + graph[i+2][j+1]

        temp_4_2 = 0
        if i <= n - 2 and j <= m - 3:
            temp_4_2 = graph[i+1][j] + graph[i + 1][j+1] + graph[i][j + 1] + graph[i][j + 2]

        temp_4_3 = 0
        if i <= n - 3 and j <= m - 2:
            temp_4_3 = graph[i+2][j] + graph[i + 1][j] + graph[i + 1][j + 1] + graph[i][j + 1]

        temp_4_4 = 0
        if i <= n - 2 and j <= m - 3:
            temp_4_4 = graph[i][j] + graph[i][j+1] + graph[i + 1][j + 1] + graph[i + 1][j + 2]

        temp_4 = max(temp_4_1, temp_4_2, temp_4_3, temp_4_4)

        temp_5_1 = 0
        if i <= n - 2 and j <= m-3:
            temp_5_1 = graph[i][j] + graph[i][j+1] + graph[i][j + 2] + graph[i + 1][j + 1]

        temp_5_2 = 0
        if i <= n - 3 and j <= m - 2:
            temp_5_2 = graph[i][j+1] + graph[i+1][j + 1] + graph[i+2][j + 1] + graph[i + 1][j]

        temp_5_3 = 0
        if i <= n - 2 and j <= m - 3:
            temp_5_3 = graph[i+1][j] + graph[i+1][j + 1] + graph[i+1][j + 2] + graph[i][j + 1]

        temp_5_4 = 0
        if i <= n - 3 and j <= m - 2:
            temp_5_4 = graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i + 1][j + 1]

        temp_5 = max(temp_5_1, temp_5_2, temp_5_3, temp_5_4)

        flag = max(temp_1, temp_2, temp_3, temp_4, temp_5)
        if flag > ans:
            ans = flag

print(ans)