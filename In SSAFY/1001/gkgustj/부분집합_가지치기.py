'''
부분 집합의 합이 10이 되는 모든 경우 출력
'''

def powerset(n, k, total):
    if total > 10:
        return

    if n == k:
        if total == 10:
            for i in range(len(picked)):
                if picked[i] == 1:
                    print(nums[i], end=' ')
            print()
    else:
        picked[k] = 1
        powerset(n, k+1, total+nums[k])

        picked[k] = 0
        powerset(n, k+1, total)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
picked = [0] * len(nums)
powerset(len(nums), 0, 0)