import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    arr = []
    t = int(input())
    for _ in range(100):
        arr.append(list(map(int, input().split())))

    max_r = 0
    max_r1 = 0

    for i in range(100):
        result = 0
        result1 = 0

        for j in range(100):
            # print(arr[99][99])
            result += arr[i][j]
            result1 += arr[j][i]

        if max_r < result:
            max_r = result

        if max_r1 < result1:
            max_r1 = result1

    result2 = 0
    result3 = 0
    max_r2 = arr[0][0]
    for i in range(100):
        result2 += arr[i][i]
        result3 += arr[i][len(arr)-1-i]

    if result2 > result3:
        max_r2 = result2
    else:
        max_r2 = result3

    answer_list = [max_r, max_r1, max_r2]
    answer = 0

    for x in answer_list:
        if x > answer:
            answer = x

    print('#{0} {1}'.format(tc, answer))