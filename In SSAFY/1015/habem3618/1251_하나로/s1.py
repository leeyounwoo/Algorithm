import sys
sys.stdin = open('input.txt')


def find_MST(s):
    key[s] = 0

    for _ in range(N):
        min_idx = -1
        min_val = float('inf')
        for i in range(N):
            if not visited[i] and key[i] < min_val:
                min_idx = i
                min_val = key[i]
        visited[min_idx] = 1

        for i in range(N):
            if visited[i]: continue
            island_ax, island_ay = x_list[min_idx], y_list[min_idx]
            island_bx, island_by = x_list[i], y_list[i]

            # E * (L^2)
            distance = (island_ax - island_bx) ** 2 + (island_ay - island_by) ** 2
            env_cost = distance * E
            if env_cost < key[i]:
                key[i] = env_cost

    return sum(key)


t = int(input())
for tc in range(1, 1 + t):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())

    mat = [[0 for _ in range(N)] for _ in range(N)]

    key = [float('inf')] * N
    visited = [0] * N
    result = find_MST(0)

    print(f'#{tc} {result:.0f}')
