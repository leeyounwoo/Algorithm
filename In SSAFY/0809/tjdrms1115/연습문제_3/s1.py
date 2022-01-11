import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):

    N = int(input())

    heights = list(map(int, input().split()))

    max_h = 0
    max_fall = 0
    for i in range(N):
        if max_h < heights[i]:
            max_h = heights[i]
            tempfall = N-i-1
            for j in range(i+1, N):
                if heights[j] >= max_h:
                    tempfall -= 1
            if max_fall < tempfall:
                max_fall = tempfall

    print(max_fall)


