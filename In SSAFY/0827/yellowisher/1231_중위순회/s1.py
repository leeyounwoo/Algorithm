def in_order(s: int):
    if s <= N:
        in_order(2 * s)
        print('{}'.format(word[s]), end='')
        in_order(2 * s + 1)


T = 10
for tc in range(1, T + 1):
    N = int(input())
    word = [0] * (N + 1)

    for i in range(N):
        data = input().split()
        word[i + 1] = data[1]

    print('#{}'.format(tc), end=' ')
    in_order(1)