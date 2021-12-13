import math

min_num, max_num = map(int, input().split())
ans = []
for num in range(min_num, max_num + 1):
    if num == 1:
        continue
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            break
    else:
        ans.append(num)

for i in range(len(ans)):
    print(ans[i])