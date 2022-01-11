import sys

sys.stdin = open('input.txt')

number = input()

numbers = []
i = 0
while i < len(number) // 7:
    numbers.append(number[i*7:i*7+7])
    i += 1

result = []
for i in numbers:
    n = 6
    temp = 0
    for j in i:
        temp += (2 ** n) * int(j)
        n -= 1
    result.append(temp)

print(*result)