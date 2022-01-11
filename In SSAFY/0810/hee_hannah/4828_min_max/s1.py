import sys
sys.stdin = open('input.txt')

T = int(input())
# 테스트 케이스의 개수
for tc in range(1, T+1):
    # 테스트 케이스 마다
    len_a = int(input())
    # 양수의 개수를 int로 받습니다
    list_a = list(map(int, input().split()))
    # n개의 양수를 빈칸을 기준으로 나눠 리스트에 담습니다
    max_a = list_a[0]
    min_a = list_a[0]
    # max와 min을 구하기 위한 초기값 설정
    for i in list_a: #리스트 안의 i가
        if i > max_a: #max 초기값보다 크다면
            max_a = i #max를 i 값으로 바꿔줍니다
        if i < min_a:
            min_a = i #동일하게 min을 i로 바꿔줍니다.
    total = max_a - min_a 
    # for문을 마치고 나온 결과값들의 차이를 구합니다

    print('#{} {}'.format(tc, total))
    # f-string 대신 포맷 사용