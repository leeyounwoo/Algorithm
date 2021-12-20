import sys

n = int(input())
nums = {}
for i in range(n):
    num = int(sys.stdin.readline())
    if num not in nums:
        nums[num] = 1
    else:
        nums[num] += 1
sorted_key = sorted(list(nums.keys()))
# print(sorted_key)
for key in sorted_key:
    for i in range(nums[key]):
        print(key)
