def permutation(n, k):
    '''
    n : 배열 arr의 길이
    k : depth
    '''
    if k == n:
        print(arr)
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            permutation(n, k+1)
            arr[k], arr[i] = arr[i], arr[k]


arr = [1, 2, 3]

permutation(3, 0)