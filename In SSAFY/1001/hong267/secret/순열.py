def permutation(n, k):
    """
    :param n: 배열 arr의 길이
    :param k: depth
    :return:
    """
    if k == n:  # ex) 3 == arr의 길이인 3
        # 할 일 진행
        print(arr)
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            permutation(n, k + 1)
            arr[i], arr[k] = arr[k], arr[i]

arr = [1, 2, 3]
permutation(3, 0)