import sys
sys.stdin = open('input.txt')

def merge(left, right):
    global cnt
    result = []

    if left[-1] > right[-1]:
        cnt +=1
    # 둘 중에 길이가 작은 배열만큼
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else :
            result.append(right.pop(0))

    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)

    return result

def merge_sort(arr):
    if len(arr) <= 1 :
        return arr

    mid = len(arr) //2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    msnums = merge_sort(nums)

    print('#{} {} {}'.format(tc, msnums[N//2], cnt))
'''
시간 초과 미해결
'''