import sys

sys.stdin = open('input.txt')
n = int(input())
ans = []
numbers = []
push_max = 0
for i in range(n):
    temp = int(input())
    if temp > push_max:
        ans += ['+'] * (temp - push_max)
        ans += ['-']
        for j in range(push_max+1, temp):
            numbers.append(j)
        push_max = temp
    else:
        if numbers and numbers[-1] == temp:
            ans += ['-']
            numbers.pop()
        else:
            ans = "NO"
            break
if ans == 'NO':
    print(ans)
else:
    for i in ans:
        print(i)