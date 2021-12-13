min_num = int(input())
max_num = int(input())
ans = []
for num in range(min_num, max_num + 1):
    if num == 1:
        continue
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        ans.append(num)

if not ans:
    print(-1)
else:
    print(sum(ans))
    print(ans[0])