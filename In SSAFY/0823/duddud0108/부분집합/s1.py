def powerset(arr, idx, curr):
    if idx == len(arr):
        return

    if sum(curr) == 10:
        print(curr)
    # idx 위치에 해당하는 원소를 뽑는 경우
    powerset(arr, idx+1, curr+[arr[idx]])

    # idx 위치에 해당하는 원소를 뽑지 않는 경우
    powerset(arr, idx+1, curr)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
powerset(arr, 0, [])

# from itertools import combinations
#
# nums = [1, 2, 3]
#
# for i in range(len(nums)):
#