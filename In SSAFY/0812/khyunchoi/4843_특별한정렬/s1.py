import sys
sys.stdin = open('input.txt')


def selection_sort(arr):
    for i in range(len(arr)-1):
        min_num = i

        for j in range(i+1, len(arr)):
            if arr[min_num] > arr[j]:
                min_num = j
        arr[i], arr[min_num] = arr[min_num], arr[i]

    return arr


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    sorted_numbers = selection_sort(numbers)

    result = ''
    for i in range(5):
        result += str(sorted_numbers[-1-i]) + ' '
        result += str(sorted_numbers[0+i]) + ' '
    print('#{} {}'.format(tc, result))
