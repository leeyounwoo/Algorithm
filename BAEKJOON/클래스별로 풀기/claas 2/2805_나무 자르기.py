import sys

sys.stdin = open('input.txt')
def binarySearch(start, end, find):
    global ans
    # print(start, end)
    if start > end:
        return
    mid = (start + end) // 2
    flag = 0
    for i in range(len(trees)):
        if trees[i] > mid:
            flag += trees[i] - mid
    # print(mid, flag)
    if flag >= find:
        if ans < mid:
            ans = mid
        binarySearch(mid+1, end, find)
    else:
        binarySearch(start, mid-1, find)

tree_cnt, want = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
ans = 0
binarySearch(1, max(trees), want)
print(ans)