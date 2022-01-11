def permutation(k):
    """
    :param k: 뽑아야 하는 개수
    :return:
    """
    result = []  # 전체 순열의 집합
    picked = []  # 지금까지 뽑은 원소의 집합

    def recursion(count):
        # count == 현재까지 뽑은 개수
        if count == k:
            # 할 일
            result.append(tuple(picked))
        else:
            for i in range(len(arr)):
                if arr[i] not in picked:  # 중복순열을 만들려면 여기를 제거
                    picked.append(arr[i])
                    recursion(count + 1)
                    picked.pop()

    recursion(0)  # count 0부터 시작
    return result


arr = [1, 2, 3]
print(permutation(3))
