numbers = list(map(int, input().split()))
ans = 0
for i in range(len(numbers)):
    ans += numbers[i] ** 2
print(ans % 10)