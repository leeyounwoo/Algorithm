# 교수님 풀이


def powerset(arr, idx, curr):
    # arr: 전체 배열
    # idx: 전체 배열에서 현재 뽑거나 뽑지 않을 위치
    # curr: 현재까지의 부분집합

    if idx == len(arr):
        # 각각의 부분집합이 완성되는 시점
        # 여기서 하고 싶은 일
        if sum(curr) == 10:
            print(curr)
        return

    # idx 위치에 해당하는 원소를 뽑는 경우
    powerset(arr, idx+1, curr + [arr[idx]])

    # idx 위치에 해당하는 원소를 뽑지 않는 경우
    powerset(arr, idx+1, curr)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
powerset(arr, 0, [])



# from pprint import pprint


# def powerset(result, i, N, input_set, element_check, s, t, n):
#     if s == n:
#         temp = []
#         for j in range(i):
#             if element_check[j]:
#                 temp.append(input_set[j])
#         result.append(temp)
#     elif i == N:
#         pass
#     elif s > n:
#         pass
#     elif t < n:
#         pass
#     else:
#         element_check[i] = 1
#         powerset(result, i + 1, N, input_set, element_check, s + input_set[i], t, n)
#         element_check[i] = 0
#         powerset(result, i + 1, N, input_set, element_check, s, t - input_set[i], n)
#
#
# input_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num = 20
#
# total = 0
# for i in input_set:
#     total += i
# element_check = [0] * len(input_set)
#
# result = []
# powerset(result, 0, len(input_set), input_set, element_check, 0, total, num)
# pprint(result)
