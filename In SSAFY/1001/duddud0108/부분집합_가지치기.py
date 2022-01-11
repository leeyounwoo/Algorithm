def powerset(n, k, sum):
    if sum > 10:
        return

    if n == k:
        result = []
        for i in range(len(picked)):
            if picked[i] == 1:
                result.append(nums[i])
        if sum == 10:
            print(*result)

    else:
        picked[k] = 1
        powerset(n, k + 1, sum + nums[k])
        picked[k] = 0
        powerset(n, k + 1, sum)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
picked = [0] * len(nums)
powerset(len(nums), 0, 0)