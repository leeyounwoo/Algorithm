import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    # 예상 가격의 개수와 예상 가격들을 입력받습니다.
    N = int(input())
    price_list = list(map(int, input().split()))

    # 총 판매차익을 result에, 현재 최대 판매가를 cur_max에 저장하기위해 초기화합니다.
    result = 0
    cur_max = 0
    # 맨 마지막날부터 처음날까지 탐색합니다.
    for i in range(N-1, -1, -1):
        # 현재 판매가가 저장된 판매가보다 크면 저장된 판매가를 갱신합니다.
        if cur_max < price_list[i]:
            cur_max = price_list[i]
        else:
            # 현재 판매가가 저장된 판매가보다 크면 팔고 차익을 result에 더합니다.
            result += cur_max - price_list[i]

    # 결과를 출력합니다.
    print('#{} {}'.format(tc, result))
