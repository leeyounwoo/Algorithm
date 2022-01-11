import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    station = [0] * 5001
    for _ in range(1, N+1):
        start, end = map(int, input().split())

        for i in range(start, end+1):
            station[i] += 1

    result = '#{} '.format(tc)
    P = int(input())
    for _ in range(P):
        result += str(station[int(input())]) + ' '

    print(result)