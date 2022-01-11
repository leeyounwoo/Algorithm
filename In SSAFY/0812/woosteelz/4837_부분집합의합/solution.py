import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC + 1):
    n, k = map(int, input().split())
    results = 0
    nums = [i+1 for i in range(12)]

    for i in range(1 << 12):
        temp = []
        for j in range(12):
            if i & (1 << j):
                temp.append(nums[j])
        if sum(temp) == k and len(temp) == n:
            results += 1
    print(f"#{tc} {results}")
