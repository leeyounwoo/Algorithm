import sys # 풀고 있는 중...

sys.stdin = open('input.txt')

def dijkstra(start, end):
    pass

T = int(input())

for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    adj_list = [[] for _ in range(N+1)]
    for _ in range(M):
        n1, n2, time = map(int, input().split())
        adj_list[n1].append([n2, time])