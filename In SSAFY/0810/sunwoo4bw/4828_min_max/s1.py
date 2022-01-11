import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):  #1,2,3
    n = int(input())      # 5
    nums_arr = list(map(int, input().split()))    # [477162 658880 ...]

    # 최대, 최소 먼저 구하고
    # 그 둘을 빼면 돼
    # 그걸 어떻게 해...?

    # 최대, 최소
    max= nums_arr[0]
    min= nums_arr[0]
    for num in nums_arr:
        if max < num :
            max = num
        if num < min :
            min = num

    result = max - min

    print('#{0} {1}'.format(tc, result))



