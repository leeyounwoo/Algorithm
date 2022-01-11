T = int(input())
for tc in range(T):
    P, Pa, Pb = map(int, input().split())    # P: 전체 쪽 수, Pa: a가 찾아야 하는 쪽 수, Pb: b가 찾아야 하는 쪽 수

    std_list = [Pa, Pb]
    result_list = []
    for std in std_list:
        l = 1
        r = P
        cnt = 1
        c = (l + r) // 2

        while True:
            if std == c:
                result_list.append(cnt)
                break

            c = (l + r) // 2
            cnt += 1
            if std > c:
                l = c
            elif std < c:
                r = c

    if result_list[0] > result_list[1]:
        result = 'B'
    if result_list[0] < result_list[1]:
        result = 'A'
    else:
        result = 0

    print('#{0} {1}'.format(tc+1, result))