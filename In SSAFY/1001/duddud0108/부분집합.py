def powerset(n, k):
    '''
    :param n: 원본 배열의 길이
    :param k: 트리의 depth
    :return:
    '''
    if n == k:
        for i in range(len(picked)):
            if picked[i] == 1:
                print(arr[i], end=" ")
        print()
    else:
        picked[k] = 1
        powerset(n, k + 1)
        picked[k] = 0
        powerset(n, k + 1)


arr = [1, 2, 3]
picked = [0] * len(arr)
powerset(3, 0)