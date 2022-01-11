import sys
sys.stdin = open('input.txt')


# 1부터 12까지 숫자를 원소로 가지는 집합 arr
arr = [i for i in range(1, 13)]
n = len(arr)

# 부분집합 리스트
lst = []
for i in range(1 << n):    # 부분집합 만들어지는 부분  2^n
    sub_lst = []                # 부분집합
    for j in range(n):
        if i & (1 << j):          # 부분집합 만들기
            sub_lst.append(arr[j])
    lst.append(sub_lst)         # 리스트에 부분집합 추가하기


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    result = 0

    for s in lst:               # 테스트 케이스에 모든 부분집합 중 길이 N 합 K 적용하여 넣기
        if len(s) == N and sum(s) == K:
            result += 1

    print('#{} {}'.format(tc, result))