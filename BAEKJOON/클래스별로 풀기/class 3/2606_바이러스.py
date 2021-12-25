import sys

sys.stdin = open('input.txt')
def bfs(index):
    for now in node[index]:
        if not visited[now]:
            visited[now] = 1
            bfs(now)

n = int(input())
node = [[] for _ in range(n+1)]
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)
# print(node)
check = [0] * (n + 1)
visited = [0] * (n+1)
# print(check)
visited[1] = 1
bfs(1)
print(sum(visited)-1)