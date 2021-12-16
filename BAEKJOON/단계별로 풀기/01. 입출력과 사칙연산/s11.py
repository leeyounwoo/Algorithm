a = int(input())
b = input()
nums = []
for i in range(len(b)):
    nums.append(a * int(b[i]))
nums.reverse()
result = 0
temp = 1
for num in nums:
    result += temp * num
    temp *= 10
    print(num)
print(result)