import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    building_list = list(map(int, input().split()))
    result = 0

    for i in range(2, N-2):
        max_height = max(building_list[i-2], building_list[i-1], building_list[i+1], building_list[i+2])
        if building_list[i] > max_height:
            result += building_list[i]-max_height

    print('#{0} {1}'.format(tc, result))