import sys
sys.stdin = open('input.txt')

T = int(input())

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_num = i
        for j in range(i+1, len(arr)):
            if arr[min_num] > arr[j]:
                min_num = j
        arr[min_num], arr[i] = arr[i], arr[min_num]
    return arr

for tc in range(1, T+1):
    N, length = input().split()
    num_list = list(input().split())
    num_str = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    new_str = []
    for i in range(int(length)):
        new_str.append(num_str.index(num_list[i]))

    selection_sort(new_str)
    # new_str.sort()

    for j in range(int(length)):
        new_str[j] = num_str[new_str[j]]


    print('{}'.format(N), *new_str)


    # result = [0] * 10
    #
    # for i in num_list:
    #     result[num_str.index(i)] += 1
    #
    # print(result)
