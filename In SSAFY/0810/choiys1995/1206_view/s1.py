import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N = int(input())
    buildings = list(map(int, input().split()))
    count = 0

    for i in range(2, len(buildings)-2):
        b_max = max([buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2]])
        if buildings[i] > b_max:
            count += buildings[i] - b_max

    print('#{} {}'.format(tc+1, count))