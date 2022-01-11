def quicksort(x):
    '''
    퀵소트의 평균 시간 복잡도: O(nlogn)
    퀵소트의 최악 시간 복잡도: O(n^2)

    성능의 안정성 때문에 Merge Sort를 선호하는 편
    (혹은 언어에 내장된 정렬 함수를 사용하는 것이 바람직
<<<<<<< HEAD:0823/hong267/practice/quicksort_easy.py
<<<<<<< HEAD
     파이썬의 경우 tim sort를 사용)
    퀵소트 Merge Sort와 다르게 "불안정 정렬"
=======
     파이썬의 경우 tim sort를 사용).
    퀵소트는 Merge Sort와 다르게 "불안정 정렬".
>>>>>>> 548daa4abe5e97aacab0c6d163197eb688f08bf3
=======
     파이썬의 경우 tim sort를 사용)
    퀵소트 Merge Sort와 다르게 "불안정 정렬"
>>>>>>> 6a5708a070fc805f72c442bd1a4554b1ef977e3e:0823/quicksort_easy.py
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
<<<<<<< HEAD:0823/hong267/practice/quicksort_easy.py
<<<<<<< HEAD
print(quicksort(nums))
=======
result = quicksort(nums)
print(result)

>>>>>>> 548daa4abe5e97aacab0c6d163197eb688f08bf3
=======
print(quicksort(nums))
>>>>>>> 6a5708a070fc805f72c442bd1a4554b1ef977e3e:0823/quicksort_easy.py
