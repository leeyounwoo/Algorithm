def powerset(n,k):
    '''
    :param n: 원본 배열의 길이
    :param k: 트리의 depth
    :return:
    '''
    if n == k:
        # 할 일 진행
        for i in range(len(picked)):
            if picked[i] == 1: # 해당 자리가 뽑혔다면...
                print(arr[i], end=" ")
        print()
    else :
        picked[k] = 1
        powerset(n, k+1) # k 번째 요소를 뽑은 경우
        picked[k] = 0
        powerset(n, k+1) # k 번쨰 요소를 뽑지 않은 경우

arr = [1,2,3]
picked = [0] * len(arr)
powerset(3, 0)
