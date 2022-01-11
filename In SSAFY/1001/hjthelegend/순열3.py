def permutation(count, k):
    '''
    :param k: 뽑아야 하는 개수
    :return:
    '''

    if count == k:
        # 할 일
        result.append(tuple(picked))
    else:
        for i in range(len(arr)):
            if arr[i] not in picked: # 중복순열을 만들려면 여기를 제거
                picked.append(arr[i])
                permutation(count+1, k)
                picked.pop()

result = [] # 전체 순열의 집합
picked = [] # 지금까지 뽑은 원소의 집합
arr = [1, 2, 3]
permutation(0, 3)
print(result)