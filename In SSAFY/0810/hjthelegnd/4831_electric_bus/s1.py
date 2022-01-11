import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t + 1):
    k, n, m = map(int, input().split())
    stations = list(map(int, input().split()))

    target = 0
    count = 0
    temp = 0

    for i in range(len(stations) - 1):
        for j in range(len(stations) - 1 - i):
            if stations[j] < stations[j + 1]:
                # > 부등호표시를 바꾸니 역순으로 정렬
                stations[j], stations[j + 1] = stations[j + 1], stations[j]

    for _ in range(m):
        for i in stations:
            if target >= n:
                break

            elif temp + k >= i:
                temp = i
                target = temp + k
                count += 1
                break

    if target >= n:
        print('#{0} {1}'.format(tc, count))
    else:
        print('#{0} 0'.format(tc))