from itertools import combinations

def powerset(arr, idx, curr):

    # 종료조건(마지막 원소까지 포함 여부를 결정한 경우)
    if idx == len(arr):
        if sum(curr) == 10:
            print(curr)
        return

    if sum(curr) > 10:
        return

    # idx 위치에 해당하는 원소를 뽑는 경우
    powerset(arr, idx + 1, curr + [arr[idx]])

    # idx 위치에 해당하는 원소를 뽑지 않는 경우
    powerset(arr, idx+1, curr)

arr = [i + 1 for i in range(3)]
# print(powerset(arr, 0, []))

for i in range(len(arr) + 1):
    for combi in combinations(arr, i):
        print(combi)