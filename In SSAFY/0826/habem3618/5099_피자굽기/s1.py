import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheeze = list(map(int, input().split()))

    fire_pit = []

    for i in range(N):
        fire_pit.append([cheeze[i], i])

    count = 0
    while len(fire_pit) != 1:
        fire_pit[0][0] //= 2

        if fire_pit[0][0] == 0:

            if N + count < M:
                fire_pit.pop(0)
                fire_pit.append([cheeze[N+count], N+count])
                count += 1

            else:
                fire_pit.pop(0)

        else:
            fire_pit.append(fire_pit.pop(0))

    print('#{} {}'.format(tc, fire_pit[0][1]+1))
