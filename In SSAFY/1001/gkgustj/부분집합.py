def powerset(n, k):
    '''
    n : 원본 배열의 길이
    k : 트리의 depth
    '''

    if n == k:
        for i in range(len(picked)):
            if picked[i] == 1:
                print(arr[i], end=' ')
        print()
    else:
        # k번째 요소를 뽑은 경우
        picked[k] = 1
        powerset(n, k+1)

        # k번째 요소를 뽑지 않은 경우
        picked[k] = 0
        powerset(n, k+1)


arr = [1, 2, 3]
picked = [0] * len(arr)
powerset(3, 0)