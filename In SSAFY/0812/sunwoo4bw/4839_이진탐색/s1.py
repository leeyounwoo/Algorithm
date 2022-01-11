'''
#1 A
#2 0
#3 A
'''

import sys
sys.stdin = open('input.txt')
#이진 검색- 자료가 정렬된 상태 필수
# 이긴 사람 출력, 비기면 0

def binary_search(page, tada):
    left = 1
    right = page  # 전체쪽수

    cnt = 0
    while left <= right:
        middle = (left + right) // 2

        if middle == tada:
            return cnt
        elif middle > tada:
            right = middle
            cnt += 1
        else:
            left = middle
            cnt += 1

T = int(input())
for tc in range(1, T + 1):
    # P 책 전체 쪽 수, A, B가 찾을 쪽 번호
    P, Pa, Pb = map(int, input().split())
    cnt_a = binary_search(P, Pa)
    cnt_b = binary_search(P, Pb)

    if cnt_a < cnt_b:
        result = 'A'
    elif cnt_a > cnt_b:
        result = 'B'
    else :
        result = 0
    print('#{} {}'.format(tc, result))
