a = int(input())
b = int(input())
c = int(input())
num = str(a * b * c)

ans = [0] * 10
for i in num:
    ans[int(i)] += 1
for answer in ans:
    print(answer)