'''
부분집합의 합이 10이 되는 모든 경우를 출력하시오.
'''


def powerset(n, k, sum):
    # 가지치기 (prunning)
    if sum > 10:
        return

    if n == k:
        # 할 일...
        # 이 시점에 picked 배열에 부분집합의 원소들이 담겨있음
        total = 0
        elements = []
        for i in range(len(picked)):
            if picked[i] == 1:
                total += nums[i]
                elements.append(nums[i])

        if total == 10:
            print(elements)
    else:
        picked[k] = 1
        powerset(n, k+1, sum + nums[k])
        picked[k] = 0
        powerset(n, k+1, sum)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
picked = [0] * len(nums)
powerset(len(nums), 0, 0)
