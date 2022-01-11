import sys
sys.stdin = open('input.txt')

# append랑 len때문에 시간초과난대,,!

def merge(left, right):
    global cnt
    if left[-1] > right[-1]: # 왼쪽의 끝 > 오른쪽의 끝
        cnt += 1  # 오른쪽 원소가 먼저 복사되는 경우의 수
    left_n = len(left)
    right_n = len(right)
    left_i, right_i = 0, 0
    i = 0
    result = [0] * (left_n + right_n) # 빈리스트 대신 0으로
    while left_i != left_n and right_i != right_n: # 한쪽이라도 길이가 같아질 때까지
        # 한쪽이라도 나눈 것들 다 result 에 더할때까지
        if left[left_i] <= right[right_i]: # 왼쪽이 더 작으면
            result[i] += left[left_i] # 왼쪽 더하기
            i += 1 # result 인덱스 하나 올려주기
            left_i += 1
        else: # 오른쪽이 더 작으면
            result[i] += right[right_i]  # 오른쪽 더하기
            i += 1
            right_i += 1

    if left_i != left_n: # 길이가 같지 않으면
        while left_i != left_n: # 같아질 때까지
            result[i] += left[left_i] # 마저 더하기
            i += 1
            left_i += 1

    if right_i != right_n:
        while right_i != right_n:
            result[i] += right[right_i]
            i += 1
            right_i += 1
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0 # 오른쪽 원소가 먼저 복사되는 경우의 수
    a = merge_sort(arr)
    print('{} {}'.format(a[n//2], cnt)) # N//2 번째 원소와 오른쪽 원소가 먼저 복사되는 경우의 수
