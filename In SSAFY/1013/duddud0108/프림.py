'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
def find_MST(s):
    key[0] = 0

    for _ in range(V):
        min_idx = -1
        min_val = float('inf')
        for i in range(V+1):
            if not visited[i] and key[i] < min_val:
                min_idx = i
                min_val = key[i]

        visited[min_idx] = 1

        for i in range(V+1):
            if adj_mat[min_idx][i] and not visited[i]:
                weight = adj_mat[min_idx][i]
                if weight < key[i]:
                    key[i] = weight
                    parents[i] = min_idx


V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]

# 인접 행렬
adj_mat = [[0 for _ in range(V+1)] for _ in range(V+1)]
for n1, n2, w in edges:
    adj_mat[n1][n2] = w
    adj_mat[n2][n1] = w

key = [float('inf')] * (V+1)
parents = [None] * (V+1)
visited = [0] * (V+1)

s = 0
find_MST(s)

# parents가 이루는 트리가 결국 MST가 됨
# ex) MST의 가중치의 합을 구하시오.
print(sum(key))