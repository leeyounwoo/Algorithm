def powerset(n, k):
    if n == k:
        total = 0
        elelments = []
        for i in range(len(picked)):
            if picked[i] == 1:
                total += nums[i]
                elelments.append(nums[i])
        
        if total == 0:
            print(elelments)
    else:
        picked[k] = 1
        powerset(n, k+1)

        picked[k] = 0
        powerset(n, k+1)


nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
picked = [0] * len(nums)
powerset(len(nums), 0)