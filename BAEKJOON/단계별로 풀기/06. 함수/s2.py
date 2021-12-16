
def sol(n):
    # print(n)
    if n >= 10001:
        return
    if check[n]:
        return
    check[n] = True
    temp = str(n)
    new_n = n
    for i in range(len(temp)):
        new_n += int(temp[i])
    sol(new_n)

check = [False] * 10001
ans = []
for i in range(1, 10001):
    if not check[i]:
        ans.append(i)
        sol(i)

for i in range(len(ans)):
    print(ans[i])
