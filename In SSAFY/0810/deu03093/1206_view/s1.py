import sys

sys.stdin = open('input.txt')

for T in range(1, 11):
    building_num = int(input())
    buildings = list(map(int, input().split()))
    left_2 = 0
    left_1 = 1
    right_1 = 3
    right_2 = 4
    count = 0
    for index in range(2, building_num - 2):
        if buildings[index] <= buildings[left_2] or\
                buildings[index] <= buildings[left_1] or\
                buildings[index] <= buildings[right_1] or\
                buildings[index] <= buildings[right_2]:
            pass

        else:
            count += buildings[index] - max(buildings[left_2], buildings[left_1],
                                            buildings[right_1], buildings[right_2])

        left_2 += 1
        left_1 += 1
        right_1 += 1
        right_2 += 1
    print('#{} {}'.format(T, count))