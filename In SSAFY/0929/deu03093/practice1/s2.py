'''
입력)
0000000111100000011000000111100110000110000111100111100111111001100111

출력)
0,120,12,7,76,24,60,121,124,103
'''
import sys
sys.stdin = open('input.txt')
n = input()
print(n)
numbers = []
for i in range(len(n)-7, -2, -7):
    temp = list(n[i:i+7])
    num = 1
    sum_temp = 0
    for j in range(len(temp)-1, -1, -1):
        # print(temp[j])
        if temp[j] == '1':
            sum_temp += num
        num *= 2
    numbers.append(sum_temp)
    if i < 0:
        temp = list(n[0:i+7])
        num = 1
        sum_temp = 0
        for j in range(len(temp) - 1, -1, -1):
            # print(temp[j])
            if temp[j] == '1':
                sum_temp += num
            num *= 2
        numbers.append(sum_temp)
numbers.reverse()
print(numbers)