# 선생님 저는 못 풀었습니다,,,,,,죄송합니다,,,,,DB 열심히 공부할게요,,,,,
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    num, change = input().split()
    numbers = []
    for i in range(len(num)):
        numbers.append(int(num[i]))
    max_num = max(numbers)
    max_idx = numbers.index(max_num)
    for j in range(int(change)):
        if numbers[0] != max_num:
            numbers[0], numbers[max_idx] = numbers[max_idx], numbers[0]
        else:
            for k in range(1, int(change)):
                max_num = max(numbers[k:len(numbers)])
                max_idx = numbers.index(max_num)
                numbers[k], numbers[max_idx] = numbers[max_idx], numbers[k]
    print(numbers)
