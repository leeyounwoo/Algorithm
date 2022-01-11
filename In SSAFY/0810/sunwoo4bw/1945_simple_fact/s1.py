import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):  # 1,2,3,4,5, ... 10
    n = int(input())
    cnt_a, cnt_b, cnt_c, cnt_d, cnt_e = 0, 0, 0, 0, 0

    # N을 나누기 위한 각각의 factor를 리스트로 뽑는다.
    # 그 리스트 값들을 하나하나 뽑아서 N을 나눈다.
    # 나눈 나머지가 0이 될 때까지 반복 - while
    # 그 과정에서 2,3,5,7,11 이 몇 번 등장했는지 cnt

    factor = [2, 3, 5, 7, 11]

    for i in factor:  # 2,3,5,7,11
        while n % i == 0:  # 2먼저
            n = n / i
            if i == 2:      # 2,3,5,7,11 순서대로 다 돌고 그 다음 i로
                cnt_a += 1
            if i == 3:
                cnt_b += 1
            if i == 5:
                cnt_c += 1
            if i == 7:
                cnt_d += 1
            if i == 11:
                cnt_e += 1
            # elif

    print('#{} {} {} {} {} {}'.format(tc, cnt_a, cnt_b, cnt_c, cnt_d, cnt_e))