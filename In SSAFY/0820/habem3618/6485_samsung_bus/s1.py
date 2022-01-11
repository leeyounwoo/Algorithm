import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    start = [0] * 5001
    end = [0] * 5001
    stop = [0] * 5001

    for i in range(N):
        A, B = map(int, input().split())
        start[A] += 1
        end[B] += 1

    # 버스 계산 끝
    for i in range(len(stop) - 1):
        stop[i + 1] = stop[i] - end[i] + start[i + 1]

    P = int(input())
    print("#{}".format(tc), end=" ")
    for i in range(P):
        C = int(input())
        print(stop[C], end=" ")
    print()
