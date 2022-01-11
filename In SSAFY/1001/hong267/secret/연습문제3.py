def powerset(n, k):
    if n == k:
        # 할 일...
        # 이 시점에 picked 배열에 부분집합의 원소들이 담겨있음
        total = 0
        elements = []
        for i in range(len(picked)):
            if picked[i] == 1:
                total += nums[i]
                elements.append(nums[i])
        
        if total == 0:
            print(elements)
    else:
        picked[k] = 1
        powerset(n, k + 1)
        picked[k] = 0
        powerset(n, k + 1)


nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
picked = [0] * len(nums)
powerset(len(nums), 0)
