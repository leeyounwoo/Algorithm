import sys
sys.stdin = open('input.txt')


# 이진 탐색하여 횟수를 반환하는 함수입니다.
def binary_search(l, r, n):

    count = 1
    # 이진 탐색을 합니다.
    while True:
        # 중앙값을 정의하고 찾고자 하는 숫자와 비교합니다.
        middle = (l + r)//2
        # 찾았으면 멈추고, 아니면 왼쪽 및 오른쪽 값을 조정합니다.
        if n > middle:
            l = middle
        elif n < middle:
            r = middle
        else:
            break
        # 횟수를 1 올리고 탐색을 반복합니다.
        count += 1

    # 횟수를 반환합니다.
    return count


T = int(input())

answer = []
for tc in range(1, T+1):

    # 총 페이지 P, 찾고자 하는 페이지 A, B를 입력받습니다.
    P, A, B = map(int, input().split())

    # 페이지를 찾는데 필요한 횟수를 구합니다.
    na = binary_search(1, P, A)
    nb = binary_search(1, P, B)

    # 결과를 출력합니다.
    result = 0
    if na < nb:
        result = 'A'
    elif nb < na:
        result = 'B'

    answer.append(result)


for tc in range(1, T+1):
    print('#{0} {1}'.format(tc, answer[tc-1]))
