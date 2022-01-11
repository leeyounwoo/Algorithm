# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이출력
import sys
sys.stdin = open('input.txt')

# T 는 테스트 케이스 번호
T = int(input())

# 1 부터 T+1 까지 range 범위 설정
for tc in range(1, T+1):
    # 양수의 개수 N개 입력받기
    n = int(input())
    n_list = list(map(int, input().split()))
    # max, min 초기값 리스트로 세우기
    max_result = n_list[0]
    min_result = n_list[0]

    for i in n_list:
        if max_result < i:
            max_result = i
        elif min_result > i:
            min_result = i
    result = max_result - min_result

    print('#{} {}'.format(tc, result))



    # for i in range(n):
    #     a = set(i)
    #     result = list[a][len(a)] - list[a][0]
    # print(result)




    # max_result = 0
    # min_result = 0
    # for num1 in n:
    #     if num1 > max_result:
    #         max_result = num1


