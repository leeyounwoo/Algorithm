import sys
sys.stdin = open('input.txt')

numbers = [n for n in range(1,13)]
length = len(numbers)

total_list = []
for i in range(1 << length):     # 부분 집합의 개수
    sub_list = []      # 부분 집합 리스트
    for j in range(length):      # 원소 숫자들 만큼 비트 비교
        if i & (1 << j):      # i의 j번째 비트가 1이면 j번째 원소를 부분집합에 담는다
            sub_list.append(numbers[j])
    total_list.append(sub_list)

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    result = 0

    # 부분집합들 중 길이가 N이고 합이 K인 것을 더해줌
    # for x in total_list:
    #     if len(x) == N and sum(x) == K:
    #         result += 1

    for x in total_list:
        tmp_len = 0
        tmp_sum = 0
        for j in x:
            tmp_len += 1
            tmp_sum += j
        if tmp_len == N and tmp_sum == K:
            result += 1

    print('#{} {}'.format(tc, result))

