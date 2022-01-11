for tc in range(1, 11):
    N = int(input())
    heights = list(map(int, input().split()))
    count = 0
    for i in range(2, N-2):
        left_2 = heights[i] - heights[i-2]
        left_1 = heights[i] - heights[i-1]
        right_1 = heights[i] - heights[i+1]
        right_2 = heights[i] - heights[i+2]
        if left_2 > 0 and left_1 > 0 and right_1 > 0 and right_2 > 0:
            count += min(left_2, left_1, right_2, right_1)
    print("#{} {}".format(tc, count))

