import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    P, Pa, Pb = map(int, (input().split()))    # P: 전체 쪽 수, Pa: a가 찾아야 하는 쪽 수, Pb: b가 찾아야 하는 쪽 수

    std_list = [Pa, Pb]

    for std in std_list:
        l = 1
        r = P                  # 쪽수 초기화
        c = int((l + r) / 2)
        cnt = 0

        while True:
            cnt += 1
            c = (l + r) // 2

            if std > c:
                l = c

            if std < c:
                r = c

            if Pa == c:
                result_A = cnt
                Pa = 0
                break

            if Pb == c:
                result_B = cnt
                break

    if result_A > result_B:
        result = 'B'
    if result_A < result_B:
        result = 'A'
    else:
        result = 0

    print('#{0} {1}'.format(tc+1, result))