year = int(input())
ans = 0
if not year % 4:
    ans = 1

if not year % 100:
    ans = 0

if not year % 400:
    ans = 1
print(ans)