ans = 0
T = int(input())
numbers = list(map(int, input().split()))
for n in numbers:
    if n == 1:
        continue
    for j in range(2, n):
        if n % j == 0:
            break
    else:
        ans += 1
print(ans)