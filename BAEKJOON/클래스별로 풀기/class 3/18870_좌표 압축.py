import sys

sys.stdin = open('input.txt')
n = int(input())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
sorted_numbers = sorted(list(set(numbers)))
ans_dict = {}
temp = 0
for i in range(len(sorted_numbers)):
    ans_dict[sorted_numbers[i]] = temp
    temp += 1
for num in numbers:
    print(ans_dict[num], end=' ')