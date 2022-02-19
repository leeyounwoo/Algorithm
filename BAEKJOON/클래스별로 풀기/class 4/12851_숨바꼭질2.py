import sys


def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')
N, K = map(int, input().split())

# 각 위치에 도달하는데 이동한 횟수를 담는다.
discovered = [-1 for _ in range(100001)]

# 각 위치에 도달하는 방법수
paths = [0 for _ in range(100001)]


def bfs():
    queue = [N]  # 시작 위치를 넣어준다.
    discovered[N] = 0  # 첫 번째 위치는 이동 횟수 0번
    paths[N] = 1  # 방법수를 1 채워준다.

    while queue:
        loc = queue.pop(0)

        # 새롭게 움직이는 위치에 대해
        for nloc in [loc + 1, loc - 1, 2 * loc]:
            # 새 위치가 범위안에 있고
            if 0 <= nloc < 100001:
                # 아직 발견이 되지 않았다면
                if discovered[nloc] == -1:
                    # 새로운 위치까지 걸리는 이동횟수 = 이전 위치까지 도달하는데 걸린 이동횟수 +1
                    discovered[nloc] = discovered[loc] + 1
                    # 방법수는 동일하다
                    paths[nloc] = paths[loc]
                    queue.append(nloc)
                # 만약 새위치가 이전에 방문했던 곳이라면 방법수가 늘어난다.
                else:
                    # 이동 횟수가 최소값인지 확인하고
                    if discovered[nloc] == discovered[loc] + 1:
                        # 이전 위치 까지 도달하는 방법수를 더해준다
                        paths[nloc] += paths[loc]

    return


bfs()
print(discovered[K])
print(paths[K])