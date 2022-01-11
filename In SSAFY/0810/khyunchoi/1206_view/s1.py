import sys
sys.stdin = open('input.txt')

for tc in range(10):
    width = int(input())
    buildings = list(map(int, input().split()))

    result = 0
    for i in range(2, width - 2):
        side_building_list = [buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2]]
        side_max_height = 0
        for building in side_building_list:
            if side_max_height < building:
                side_max_height = building

        height_diff = buildings[i] - side_max_height

        if height_diff > 0:
            result += height_diff

    print('#{} {}'.format(tc+1, result))