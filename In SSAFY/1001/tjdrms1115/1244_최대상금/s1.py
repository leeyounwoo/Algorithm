import sys
sys.stdin = open('input.txt')


def find_max(nums, N, i, k):
    global result
    if k == N:
        num = int(''.join(map(str, nums)))
        if result < num:
            result = num
    else:
        max_num = max(nums[i:])
        if nums[i] < max_num:
            for j in range(i+1, len(nums)):
                if nums[j] == max_num:
                    nums[i], nums[j] = nums[j], nums[i]
                    find_max(nums, N, i + 1, k + 1)
                    nums[i], nums[j] = nums[j], nums[i]
        else:
            if i < len(nums) - 2:
                find_max(nums, N, i + 1, k)
            else:
                compare = set(nums)
                if len(compare) != len(nums):
                    find_max(nums, N, i, k + 1)
                else:
                    nums[len(nums) - 2], nums[len(nums) - 1] = nums[len(nums) - 1], nums[len(nums) - 2]
                    find_max(nums, N, i, k + 1)
                    nums[len(nums) - 2], nums[len(nums) - 1] = nums[len(nums) - 1], nums[len(nums) - 2]


T = int(input())
for tc in range(1, T+1):

    nums, N = input().split()
    N = int(N)
    nums = list(map(int, nums))
    if tc == 3:
        a=0
    result = 0
    find_max(nums, N, 0, 0)

    print(f'#{tc} {result}')
