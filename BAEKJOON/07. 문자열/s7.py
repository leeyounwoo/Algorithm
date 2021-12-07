numbers = list(map(list, input().split()))
for i in range(len(numbers)):
    numbers[i].reverse()
    numbers[i] = int(''.join(numbers[i]))
print(max(numbers))

