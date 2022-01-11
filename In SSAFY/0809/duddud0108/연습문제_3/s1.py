import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    N = int(input())
    block = list(map(int, input().split()))
    max_gravity = 0

    for i in range(N):
        gravity = 0
        for j in range(i+1, N):
            if block[i] > block[j]:
                gravity += 1
        if max_gravity < gravity:
            max_gravity = gravity

    print(max_gravity)