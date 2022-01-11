import random
from timeit import default_timer as timer
from datetime import timedelta

def partition(arr, start, end):
    pivot = arr[end]
    store_index = start

    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1

    arr[store_index], arr[end] = arr[end], arr[store_index]
    return store_index


def quicksort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quicksort(arr, start, pivot-1)
        quicksort(arr, pivot+1, end)


def quicksort_easy(x):
    '''
    퀵소트의 평균 시간 복잡도: O(nlogn)
    퀵소트의 최악 시간 복잡도: O(n^2)

    성능의 안정성 때문에 Merge Sort를 선호하는 편
    (혹은 언어에 내장된 정렬 함수를 사용하는 것이 바람직
     파이썬의 경우 tim sort를 사용).
    퀵소트는 Merge Sort와 다르게 "불안정 정렬".
    '''
    if len(x) <= 1:
        return x

    pivot = x[len(x) // 2]
    less = []
    more = []
    equal = []
    for a in x:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)

    return quicksort_easy(less) + equal + quicksort_easy(more)


arr = random.sample(range(0, 1000000), 1000000)

print('====== 퀵소트 쉬운 버전 ======')
start = timer()
sorted_arr = quicksort_easy(arr)
end = timer()
print(timedelta(seconds=end-start))


print('====== 퀵소트 일반 버전 ======')
start = timer()
quicksort(arr, 0, len(arr)-1)
end = timer()
print(timedelta(seconds=end-start))


print('====== 팀소트 일반 버전 ======')
start = timer()
arr.sort()
end = timer()
print(timedelta(seconds=end-start))