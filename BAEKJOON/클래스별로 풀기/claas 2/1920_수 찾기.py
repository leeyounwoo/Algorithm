n = int(input())
nums_n = list(map(int, input().split()))
nums_n.sort()

m = int(input())
nums_m = list(map(int, input().split()))
new_nums_m = sorted(nums_m)

ans = {}
temp = 0
for i in range(m):
    for j in range(temp, n):
        if j == n-1 and new_nums_m[i] > nums_n[j]:
            ans[new_nums_m[i]] = 0
            break
        if new_nums_m[i] == nums_n[j]:
            ans[new_nums_m[i]] = 1
            temp = j
            break
        elif new_nums_m[i] < nums_n[j]:
            ans[new_nums_m[i]] = 0
            break

for i in range(m):
    print(ans[nums_m[i]])