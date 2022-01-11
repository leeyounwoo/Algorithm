def quicksort(x):
    '''
    퀵소트의 평균 시간 복잡도:O(nlogn)

    :param x:
    :return:
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

nums = [3, 2,1, 4, 7]
result = quicksort(nums)
print(result)