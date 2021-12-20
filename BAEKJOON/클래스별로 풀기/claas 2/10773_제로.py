n = int(input())
number = []
for _ in range(n):
    num = int(input())
    if num == 0:
        number.pop()
    else:
        number.append(num)
print(sum(number))