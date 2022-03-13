import math


def solution(n, edges):
    nodes = [[math.inf] * n for _ in range(n)]

    for i in range(1, n):
        nodes[i][i] = 0

    for i in range(len(edges)):
        node1, node2 = edges[i][0], edges[i][1]
        nodes[node1][node2] = 1
        nodes[node2][node1] = 1

    for i in range(n):
        for j in range(n):
            for k in range(n):
                nodes[j][k] = min(nodes[j][k], nodes[j][i] + nodes[i][k])

    answer = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == j or i == k or j == k:
                    continue
                if nodes[i][j] + nodes[j][k] == nodes[i][k]:
                    answer += 1
    return answer