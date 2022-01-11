import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    weight.sort(reverse=True)
    trucks.sort(reverse=True)

    load = 0
    i = 0
    for truck in trucks:
        while i < len(weight):
            if weight[i] <= truck:
                load += weight[i]
                i += 1
                break
            else:
                i += 1

    print('#{} {}'.format(t, load))