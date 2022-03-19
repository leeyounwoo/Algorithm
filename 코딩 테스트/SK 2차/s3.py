from itertools import combinations
from copy import deepcopy

def is_same(graph_a, graph_b):
    for i in range(len(graph_a)):
        graph_a[i].sort()
        graph_b[i].sort()
        for j in range(len(graph_a[i])):
            if graph_a[i][j] != graph_b[i][j]:
                return False
    return True

def function_2(graph, index_1, index_2):
    new_graph = []
    graph_1 = deepcopy(graph)
    for i in range(len(graph_1)):
        if i == index_1:
            temp = graph_1[index_2]
            new_graph.append(temp)
        elif i == index_2:
            temp = graph_1[index_1]
            new_graph.append(temp)
        else:
            temp = graph_1[i]
            new_graph.append(temp)
    for i in range(len(new_graph)):
        flag = False
        if index_1 in new_graph[i]:
            temp = new_graph[i]
            temp.remove(index_1)
            temp.append(index_2)
            new_graph.pop(i)
            new_graph.insert(i, temp)
            flag = True

        if not flag and index_2 in new_graph[i]:
            temp = new_graph[i]
            temp.remove(index_2)
            temp.append(index_1)
            new_graph.pop(i)
            new_graph.insert(i, temp)

    return new_graph

def function_1(graph_a, graph_b, indexs, rest_m, cnt):
    # global answer
    flag = is_same(graph_a, graph_b)
    if flag:
        # answer = cnt
        return cnt

    elif rest_m:
        for com in combinations(indexs, 2):
            new_graph_a = function_2(graph_a, com[0], com[1])
            flag = is_same(new_graph_a, graph_b)
            if flag:
                return cnt
            else:
                function_1(new_graph_a, graph_b, indexs, rest_m - 1, cnt)

    new_graph = deepcopy(graph_a)
    for i in range(len(new_graph)):
        if new_graph[i]:
            temp = deepcopy(new_graph[i])
            for j in range(len(temp)):
                temp.pop(j)
                for k in range(indexs):
                    if k != i and len(new_graph[k]) != len(indexs) - 1:



def solution(a, b, m):
    # global answer
    answer = 0
    graph_a = [[] for _ in range(13)]
    graph_b = [[]  for _ in range(13)]

    indexs = []
    for i in range(len(a)):
        left, right = a[i][0], a[i][1]
        graph_a[left].append(right)
        graph_a[right].append(left)
        if left not in indexs:
            indexs.append(left)
        if right not in indexs:
            indexs.append(right)
    for i in range(len(b)):
        left, right = b[i][0], b[i][1]
        graph_b[left].append(right)
        graph_b[right].append(left)

    answer = function_1(graph_a, graph_b, indexs, m, 0)
    return answer


print(solution([[1, 2], [2, 3]], [[1, 3], [3, 2]], 1))
# print(solution())
# print(solution())