import sys
sys.stdin = open('1001/woosteelz/1244_최대상금/input.txt')


def change_num(change, idx):
    if not change:
        ans.append(int(''.join(nums)))
        return
    if idx == len(nums):
        return

    for i in range(len(nums)):
        if i == idx:
            continue
        nums[idx], nums[i] = nums[i], nums[idx]
        change_num(change - 1, idx + 1)
        nums[idx], nums[i] = nums[i], nums[idx]
    change_num(change, idx + 1)


for tc in range(int(input())):
    nums, change = input().split()
    nums = list(nums)
    ans = []
    change_num(int(change), 0)

    print(f'#{tc + 1} {max(ans)}')
