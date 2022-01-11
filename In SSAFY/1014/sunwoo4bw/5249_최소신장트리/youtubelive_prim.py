import sys
sys.stdin = open('input.txt')

def prim():
    key = [987654321] * (V+1)
    visited = [0] * (V+1)
    key[0] = 0

    for _ in range(V):
        min_idx = -1
        min_value = 987654321
        # 최솟값을 찾자
        for i in range(V+1):
            if not visited[i] and key[i] < min_value:
                min_idx = i
                min_value = key[i]

        visited[min_idx] = 1
        # 갱신할 수 있으면 전부다 갱신
        for i in range(V+1):
            if not visited[i] and adj_arr[min_idx][i] < key[i]:
                key[i] = adj_arr[min_idx][i]
    return sum(key)

T = int(input())
for tc in range(1, T +1):
    V, E = map(int, input().split()) # V: 정점의 마지막 번호!(0번 부터 시작), 정점의 개수는 V+1
    # 임의 큰값으로 초기화된 값을 넣어보자
    adj_arr = [[987654321] * (V+1) for _ in range(V+1)]

    for i in range(E):
        n1, n2, w = map(int, input().split())
        adj_arr[n1][n2] = adj_arr[n2][n1] = w

    print('#{} {}'.format(tc, prim()))



