import sys
n = int(input())
numbers = [int(sys.stdin.readline()) for _ in range(n)]
# 1. 산술평균
print(round(sum(numbers)/n))

# 2. 중앙값
print(sorted(numbers)[n//2])

# 3. 최빈값
temp = {}
for i in range(len(numbers)):
    if numbers[i] not in temp:
        temp[numbers[i]] = 1
    else:
        temp[numbers[i]] += 1

ans = 0
candidate = []
for key, value in temp.items():
    if ans < value:
        candidate = [key]
        ans = value
    elif ans == value:
        candidate.append(key)

if len(candidate) >= 2:
    print(sorted(candidate)[1])
else:
    print(candidate[0])

# 4. 범위
print(abs(max(numbers) - min(numbers)))