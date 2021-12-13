n = int(input())
ans = []
temp = 2
while n != 1:
    if temp > n:
        break
    temp_n, rest = divmod(n, temp)
    if rest:
        temp += 1
        continue
    else:
        n = temp_n
        ans.append(temp)
        continue
if not ans:
    print()
for i in ans:
    print(i)