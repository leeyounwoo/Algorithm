import sys


def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')
n = int(input())
nums = list(map(int, input().split()))
ans = []
flag = -1
for i in range(n-1):
    if flag <= nums[i]:
        if max(nums[i+1:]) <= nums[i]:
            ans.append(-1)
        else:
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    flag = nums[j]
                    ans.append(nums[j])
                    break
    else:
        ans.append(flag)
ans.append(-1)
for num in ans:
    print(num, end=" ")