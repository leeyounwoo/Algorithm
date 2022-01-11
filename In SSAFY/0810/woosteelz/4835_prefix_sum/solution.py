import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(TC):
    a, m = map(int, input().split())
    nums = list(map(int, input().split()))
    results = []
    for i in range(len(nums)-m+1):
        results.append(sum(nums[i:i+m]))

    print(f"#{tc} {max(results) - min(results)}")
