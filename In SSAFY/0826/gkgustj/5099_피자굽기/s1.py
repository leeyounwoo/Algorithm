import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    idx = [i for i in range(1, M+1)]
    fire = []
    fire_idx = []

    for _ in range(N):
        fire.append(cheese.pop(0))
        fire_idx.append(idx.pop(0))

    while fire.count(0) != N - 1:
        for i in range(N):
            fire[i] //= 2

            if fire.count(0) == N - 1:
                break

            if fire[i] == 0 and cheese:
                fire.pop(i)
                fire.insert(i, cheese.pop(0))

                fire_idx.pop(i)
                fire_idx.insert(i, idx.pop(0))



    for j in range(N):
        if fire[j] != 0:
            break

    print('#{} {}'.format(t, fire_idx[j]))