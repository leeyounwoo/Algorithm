import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    N = int(input())
    block = list(map(int, input().split()))

    result = 0


    max_num = 0

    for n in range(N, 0, -1):
        for g_num in g_arr:
            if n-g_num+1 > max_num:
                max_num = n-g_num+1

    print(max_num)