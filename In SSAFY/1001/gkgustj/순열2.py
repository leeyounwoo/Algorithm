def permutation(k):
    '''
    k : 뽑아야하는 개수
    '''

    result = [] # 전체 순열 집합
    picked = [] # 지금까지 뽑은 원소 집합

    def recursion(count):
        # count : 현재까지 뽑은 개수
        if count == k:
            result.append(tuple(picked))
        else:
            for i in range(len(arr)):
                if arr[i] not in picked:
                    picked.append(arr[i])
                    recursion(count + 1)
                    picked.pop()
    
    recursion(0)
    return result


arr = [1, 2, 3]
print(permutation(3))