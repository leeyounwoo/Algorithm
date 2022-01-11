import sys
sys.stdin = open('input.txt')

for tc in range(10):
    width = int(input())
    buildings = list(map(int, input().split()))

    result = 0
    for i in range(2, width - 2):
        height_diff = buildings[i] - max(max(buildings[i-2], buildings[i-1]), max(buildings[i+1], buildings[i+2]))

        if height_diff > 0:
            result += height_diff

    print('#{} {}'.format(tc+1, result))