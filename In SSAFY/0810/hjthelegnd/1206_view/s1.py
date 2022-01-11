import sys
sys.stdin = open('input.txt')
t = 10
for tc in range(1, t + 1):
    test_case = int(input())
    count = 0
    buildings = list(map(int, input().split()))

    for i in range(2, len(buildings) - 2):
        b_list = []
        b_list.extend([buildings[i - 2], buildings[i - 1], buildings[i + 1], buildings[i + 2]])

        if buildings[i] > max(b_list):
            count += buildings[i] - max(b_list)

    print('#{0} {1}'.format(tc, count))