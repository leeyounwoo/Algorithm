def permutation(n, k):
    """
    :param n: 배열 arr의 길이
    :param k: depth
    :return:
    """
    if k == n:
        print(arr)
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            permutation(n, k + 1)
            arr[i], arr[k] = arr[k], arr[i]


arr = [1, 2, 3]
permutation(3, 2)
