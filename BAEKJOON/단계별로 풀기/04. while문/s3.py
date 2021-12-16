start = input()
ans = 0
if len(start) == 1:
    start = '0' + start
sum_1 = (int(start[0]) + int(start[1])) % 10
new_n = start[1] + str(sum_1)
ans += 1
while new_n != start:
    now = new_n
    if len(now) == 1:
        now = '0' + now
    sum_1 = (int(now[0]) + int(now[1])) % 10
    new_n = now[1] + str(sum_1)
    ans += 1
print(ans)

