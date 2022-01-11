def quicksort(x):
    '''
    퀵소트의 평균 시간 복잡도 : O(nlogn)
    퀵소트의 최악 시간 복잡도 : O(n^2)

    성능의 안정성 때문에 Merge Sort를 선호하는 편
    퀵소트는 Merge Sort와 다르게 "불안정 정렬"
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

    return quicksort(less) + equal + quicksort(more)

nums = [3, 2, 1, 4, 7]
result = quicksort(nums)
print(result)