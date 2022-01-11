import sys
sys.stdin = open('input.txt')

T = int(input())

def bi_search(P, Pa):
    start = 1
    end = P
    cnt = 1
    mid = (start + end) // 2

    while mid != Pa:  # Pa 값이 mid와 다를때까지 실행
        cnt += 1  # count 값 1씩 더해주기
        if mid < Pa:  # mid 가 Pa 보다 작으면 mid 값을 start 값에 주어 오른쪽으로 이동
            start = mid
        else:  # 반대의 경우 왼쪽으로 이동
            end = mid
        mid = (start + end) // 2  # 위 행위를 반복할 수 있도록 지정
    return cnt

for tc in range(1, T+1):
    # 전체 쪽수 : P , 각각 찾을 쪽수 : Pa, Pb
    P, Pa, Pb = map(int, input().split())


    if bi_search(P, Pa) < bi_search(P, Pb):
        print('#{} A'.format(tc))
    elif bi_search(P, Pa) == bi_search(P, Pb):
        print('#{} 0'.format(tc))
    else:
        print('#{} B'.format(tc))