def permutation(count, k):
    # count == 현재까지 뽑은 개수
    if count == k:
        # 할 일
        result.append(tuple(picked))
    else:
        for i in range(len(arr)):
            if arr[i] not in picked:  # 중복순열을 만들려면 여기를 제거
                picked.append(arr[i])
                permutation(count + 1, k)
                picked.pop()


arr = [1, 2, 3]
result = []  # 전체 순열의 집합
picked = []  # 지금까지 뽑은 원소의 집합
permutation(0, 3)
print(result)

