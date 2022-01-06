import sys


def input():
    return sys.stdin.readline().rstrip()


def dfs(a, b):
    graph[a] = graph[a].union(graph[b])
    # print(graph[a])
    temp = list(graph[a])
    for i in range(len(temp)):
        if not check[temp[i]]:
            check[temp[i]] = True
            dfs(a, temp[i])
    #     print(i)
    #     dfs(a, i)

sys.stdin = open('input.txt')
n = int(input())
graph = []
for i in range(n):
    set_temp = set()
    temp = list(map(int, input().split()))
    for idx in range(len(temp)):
        if temp[idx]:
            set_temp.add(idx)
    graph.append(set_temp)
# print(graph)

for i in range(len(graph)):
    temp = list(graph[i])
    check = [False] * n
    for j in range(len(temp)):
        # if temp[j] not in graph[i]:
        #     print('temp')
        check[temp[j]] = True
        dfs(i, temp[j])

ans = []
for i in range(n):
    list_1 = []
    temp = sorted(list(graph[i]))
    for j in range(n):
        if j in temp:
            list_1.append('1')
        else:
            list_1.append('0')
    ans.append(list_1)

# print(ans)
for i in range(len(ans)):
    # print()
    print(' '.join(ans[i]))
