import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    containers = sorted(list(map(int, input().split())))
    trucks = sorted(list(map(int, input().split())))
    total = 0

    while containers and trucks:
        truck = trucks.pop()

        while containers:
            container = containers.pop()

            if truck >= container:
                total += container
                break
    print('#{} {}'.format(tc, total))
