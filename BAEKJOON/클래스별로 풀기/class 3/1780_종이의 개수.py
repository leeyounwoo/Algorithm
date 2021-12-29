import sys

sys.stdin = open('input.txt')
def haveNotZero(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] != 0:
                return False
    return True

def makeNewGraph(graph):
    flag_1 = len(graph) // 3
    flag_2 = flag_1 * 2
    graph1 = []
    graph2 = []
    graph3 = []
    graph4 = []
    graph5 = []
    graph6 = []
    graph7 = []
    graph8 = []
    graph9 = []
    for i in range(len(graph)):
        if i < flag_1:
            graph1.append(graph[i][:flag_1])
            graph2.append(graph[i][flag_1:flag_2])
            graph3.append(graph[i][flag_2:])
        elif flag_1 <= i < flag_2:
            graph4.append(graph[i][:flag_1])
            graph5.append(graph[i][flag_1:flag_2])
            graph6.append(graph[i][flag_2:])
        else:
            graph7.append(graph[i][:flag_1])
            graph8.append(graph[i][flag_1:flag_2])
            graph9.append(graph[i][flag_2:])
    return [graph1, graph2, graph3, graph4, graph5, graph6, graph7, graph8, graph9]


def cut(graph):
    global ans_minus, ans_zero, ans_one
    start = graph[0][0]
    cnt = len(graph) * len(graph[0])
    temp = 0
    for i in range(len(graph)):
        temp += sum(graph[i])
    if start == 1:
        if temp == cnt:
            ans_one += 1
            return

    elif start == -1:
        if temp == cnt * -1:
            ans_minus += 1
            return
    elif start == 0:
        if haveNotZero(graph):
            ans_zero += 1
            return

    new_graphs = makeNewGraph(graph)
    for g in new_graphs:
        cut(g)



n = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans_minus = 0
ans_zero = 0
ans_one = 0
cut(graph)
print(ans_minus)
print(ans_zero)
print(ans_one)