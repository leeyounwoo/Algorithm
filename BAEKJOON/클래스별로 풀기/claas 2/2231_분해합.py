n = int(input())
ans = 0
# temp = list(map(int, n))
# print(temp)
for i in range(n-1, -1, -1):
    temp_str = str(i)
    temp_int = int(temp_str)
    flag = sum(list(map(int, temp_str))) + temp_int
    if flag == n:
        ans = temp_int
print(ans)
